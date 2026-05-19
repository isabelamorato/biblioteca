#!/usr/bin/env python3
"""
Parse a HAR file and extract API information for skill generation.
Usage: python3 parse_har.py <har_file> [--host <filter_host>]
"""

import json
import sys
import re
import base64
import argparse
from urllib.parse import urlparse, parse_qs


def _b64url_decode(s):
    s += '=' * (-len(s) % 4)
    try:
        return base64.urlsafe_b64decode(s).decode('utf-8', errors='ignore')
    except Exception:
        return ''


def decode_jwt(token):
    parts = token.split('.')
    if len(parts) != 3:
        return None, None
    try:
        h = json.loads(_b64url_decode(parts[0]))
        p = json.loads(_b64url_decode(parts[1]))
        return h, p
    except Exception:
        return None, None

ANALYTICS_PATTERNS = re.compile(
    r'google|facebook|hotjar|gtm|ga\.|_fb|clarity|amplitude|segment|mixpanel|heap|intercom|zendesk|hubspot|drift|crisp|tawk|analytics|tracking|pixel|beacon|bn2o|doubleclick|googlesyndication|usermaven|contentsquare|posthog|sentry\.io|datadoghq|newrelic|fullstory|logrocket|bugsnag|cloudflareinsights|linkedin\.com/(px|wa)|/collect\b|cdn\.matomo|stats\.g\.doubleclick|tiktok\.com/i18n/pixel|adsystem\.com|adnxs|criteo',
    re.IGNORECASE
)

ASSET_EXTENSIONS = {'.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.woff', '.woff2', '.ttf', '.eot', '.webp', '.avif', '.map'}

ANALYTICS_COOKIES = re.compile(r'^(_ga|_gid|_gat|_fbp|_fbc|_gcl|_hjS|_hjU|amplitude|ajs_|intercom|hubspot|drift|crisp)', re.IGNORECASE)

SESSION_COOKIE_PATTERNS = re.compile(r'session|token|auth|login|logged|user|account|csrf|xsrf|remember|bearer|jwt|sid|^[a-z]+$', re.IGNORECASE)

ID_PATTERNS = [
    (re.compile(r'/[0-9a-f]{32}(?=/|$)'), '/{hex32}'),
    (re.compile(r'/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}(?=/|$)'), '/{uuid}'),
    (re.compile(r'/[a-zA-Z]+-\d{4,}(?=/|$)'), '/{slug-id}'),
    (re.compile(r'/\d{3,}(?=/|$)'), '/{id}'),
]


def parametrize_path(path):
    for pattern, replacement in ID_PATTERNS:
        path = pattern.sub(replacement, path)
    return path


def is_noise(url, host_filter):
    parsed = urlparse(url)
    if host_filter and host_filter not in parsed.netloc:
        return True
    if ANALYTICS_PATTERNS.search(parsed.netloc):
        return True
    path = parsed.path.lower()
    if any(path.endswith(ext) for ext in ASSET_EXTENSIONS):
        return True
    if ANALYTICS_PATTERNS.search(path):
        return True
    return False


def classify_cookies(cookie_string):
    if not cookie_string:
        return {}, {}
    session = {}
    analytics = {}
    for part in cookie_string.split(';'):
        part = part.strip()
        if '=' not in part:
            continue
        name, _, value = part.partition('=')
        name = name.strip()
        if ANALYTICS_COOKIES.match(name):
            analytics[name] = value.strip()
        elif SESSION_COOKIE_PATTERNS.search(name):
            session[name] = value.strip()
    return session, analytics


def parse_har(har_path, host_filter=None):
    with open(har_path, encoding='utf-8') as f:
        har = json.load(f)

    entries = har['log']['entries']
    endpoints = {}
    hosts_seen = set()
    session_cookies = {}
    csrf_token = None
    cookie_expiry = {}
    has_cloudflare = False
    has_csrf_header = False

    bearer_hosts = {}
    api_host_calls = {}
    bearer_tokens = []
    for entry in entries:
        u = urlparse(entry['request']['url'])
        if is_noise(entry['request']['url'], None):
            continue
        for h in entry['request'].get('headers', []):
            if h['name'].lower() == 'authorization' and h['value'].lower().startswith('bearer '):
                bearer_hosts[u.netloc] = bearer_hosts.get(u.netloc, 0) + 1
                tok = h['value'].split(' ', 1)[1]
                if tok and tok not in bearer_tokens:
                    bearer_tokens.append(tok)
                break
        if '/api/' in u.path:
            api_host_calls[u.netloc] = api_host_calls.get(u.netloc, 0) + 1

    if host_filter:
        main_host = host_filter
    elif bearer_hosts:
        main_host = max(bearer_hosts, key=bearer_hosts.get)
    elif api_host_calls:
        main_host = max(api_host_calls, key=api_host_calls.get)
    else:
        main_host = ''

    auth_provider = None
    auth_audience = None
    for tok in bearer_tokens:
        hdr, payload = decode_jwt(tok)
        if not payload:
            continue
        iss = payload.get('iss', '')
        if 'auth0' in iss.lower(): auth_provider = 'auth0'
        elif 'okta' in iss.lower(): auth_provider = 'okta'
        elif 'amazoncognito' in iss.lower() or 'cognito' in iss.lower(): auth_provider = 'cognito'
        elif 'firebase' in iss.lower() or 'google' in iss.lower(): auth_provider = 'google-identity'
        elif iss: auth_provider = iss
        aud = payload.get('aud')
        if aud and not auth_audience:
            auth_audience = aud[0] if isinstance(aud, list) else aud
        if auth_provider:
            break

    mint_endpoint = None
    if bearer_tokens and main_host:
        first_bearer_idx = None
        for i, e in enumerate(entries):
            u = urlparse(e['request']['url'])
            if u.netloc == main_host:
                for h in e['request'].get('headers', []):
                    if h['name'].lower() == 'authorization' and h['value'].lower().startswith('bearer '):
                        first_bearer_idx = i
                        break
                if first_bearer_idx is not None:
                    break
        if first_bearer_idx is not None:
            for j in range(first_bearer_idx - 1, max(0, first_bearer_idx - 50), -1):
                e = entries[j]
                u = urlparse(e['request']['url'])
                if is_noise(e['request']['url'], None): continue
                if u.netloc == main_host: continue
                if '/api/' not in u.path: continue
                ct = ''
                for rh in e['response'].get('headers', []):
                    if rh['name'].lower() == 'content-type': ct = rh['value']; break
                if 'json' not in ct.lower(): continue
                body_text = e['response'].get('content', {}).get('text', '') or ''
                if 'access' in body_text.lower() and 'token' in body_text.lower():
                    mint_endpoint = f"{e['request']['method']} https://{u.netloc}{u.path}"
                    break

    for entry in entries:
        req = entry['request']
        resp = entry['response']
        url = req['url']
        parsed = urlparse(url)

        if is_noise(url, host_filter): continue

        hosts_seen.add(parsed.netloc)
        method = req['method'].upper()
        path = parsed.path or '/'
        template = parametrize_path(path)
        is_third_party = parsed.netloc != main_host
        if is_third_party:
            query_params_full = {k: v[0] for k, v in parse_qs(parsed.query).items()}
        else:
            query_params_full = {k: None for k in parse_qs(parsed.query).keys()}

        resp_content_type = ''
        for rh in resp.get('headers', []):
            if rh['name'].lower() == 'content-type': resp_content_type = rh['value']; break
        is_api = ('/api/' in path or 'application/json' in resp_content_type or method in ('POST', 'PUT', 'PATCH', 'DELETE'))
        if not is_api: continue

        req_headers = {h['name'].lower(): h['value'] for h in req.get('headers', [])}
        cookie_str = req_headers.get('cookie', '')
        s_cookies, _ = classify_cookies(cookie_str)
        if s_cookies and main_host:
            main_root = '.'.join(main_host.split('.')[-2:])
            if parsed.netloc == main_host or parsed.netloc.endswith('.' + main_root) or parsed.netloc == main_root:
                session_cookies.update(s_cookies)

        if 'x-csrf-token' in req_headers or 'x-xsrf-token' in req_headers:
            has_csrf_header = True
            if not csrf_token:
                csrf_token = req_headers.get('x-csrf-token') or req_headers.get('x-xsrf-token')

        if not is_third_party and not has_cloudflare:
            for rh in resp.get('headers', []):
                hname = rh['name'].lower()
                if hname == 'cf-ray': has_cloudflare = True; break
                if hname == 'server' and 'cloudflare' in rh['value'].lower(): has_cloudflare = True; break

        body_schema = None
        body_sample = None
        if req.get('postData'):
            try:
                body = json.loads(req['postData'].get('text', ''))
                if isinstance(body, dict):
                    body_schema = list(body.keys())
                    if is_third_party: body_sample = body
            except Exception:
                pass

        key = f"{method} {parsed.netloc}{template}"
        if key not in endpoints:
            endpoints[key] = {
                'method': method, 'host': parsed.netloc, 'path_template': template,
                'example_path': path, 'status_codes': set(), 'query_params': dict(query_params_full),
                'body_fields': body_schema, 'body_sample': body_sample,
                'is_third_party': is_third_party,
                'requires_auth': bool(s_cookies or csrf_token) and not is_third_party, 'count': 0,
            }
        endpoints[key]['status_codes'].add(resp['status'])
        for k, v in query_params_full.items():
            if k not in endpoints[key]['query_params'] or (v and not endpoints[key]['query_params'][k]):
                endpoints[key]['query_params'][k] = v
        endpoints[key]['count'] += 1

    response_shape = None
    if main_host:
        for entry in entries:
            u = urlparse(entry['request']['url'])
            if u.netloc != main_host or entry['request']['method'].upper() != 'GET': continue
            ct = ''
            for rh in entry['response'].get('headers', []):
                if rh['name'].lower() == 'content-type': ct = rh['value']; break
            if 'json' not in ct.lower(): continue
            txt = entry['response'].get('content', {}).get('text', '') or ''
            if not txt or txt[0] not in '[{': continue
            try: body = json.loads(txt)
            except Exception: continue
            if isinstance(body, list): response_shape = 'array'; break
            if isinstance(body, dict) and ('results' in body or 'data' in body) and ('total' in body or 'page' in body):
                response_shape = 'paginated'; break
            if isinstance(body, dict): response_shape = 'object'

    if bearer_tokens: auth_flow = 'bearer-mint'
    elif has_csrf_header: auth_flow = 'csrf'
    elif session_cookies: auth_flow = 'cookie'
    else: auth_flow = 'unknown'

    needs_cdp = has_cloudflare or has_csrf_header or auth_flow == 'bearer-mint'
    recommended_mode = 'cdp' if needs_cdp else 'simple'
    result = {
        'hosts': sorted(hosts_seen), 'main_host': main_host,
        'recommended_mode': recommended_mode,
        'detection': {
            'has_cloudflare': has_cloudflare, 'has_csrf_header': has_csrf_header,
            'has_bearer': bool(bearer_tokens), 'auth_flow': auth_flow,
            'auth_provider': auth_provider, 'auth_audience': auth_audience,
            'response_shape': response_shape,
            'reason': (
                'Cloudflare detectado — curl bloqueado por TLS fingerprint' if has_cloudflare else
                'CSRF rotativo — token muda a cada request' if has_csrf_header else
                'Bearer JWT mintado pelo frontend' if auth_flow == 'bearer-mint' else
                'Sem Cloudflare/CSRF/Bearer — curl com cookies funciona'
            ),
            'mint_endpoint': mint_endpoint,
        },
        'endpoints': [],
        'auth': {
            'session_cookies': session_cookies, 'csrf_token': csrf_token,
            'cookie_expiry_seconds': cookie_expiry,
            'bearer_sample_payload': decode_jwt(bearer_tokens[0])[1] if bearer_tokens else None,
        }
    }

    for key, ep in sorted(endpoints.items(), key=lambda x: (-x[1]['count'], x[0])):
        result['endpoints'].append({
            'method': ep['method'], 'host': ep['host'], 'path': ep['path_template'],
            'example': ep['example_path'], 'status_codes': sorted(ep['status_codes']),
            'query_params': ep['query_params'], 'body_fields': ep['body_fields'],
            'body_sample': ep['body_sample'], 'is_third_party': ep['is_third_party'],
            'requires_auth': ep['requires_auth'], 'calls': ep['count'],
        })

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('har_file')
    parser.add_argument('--host', default=None)
    args = parser.parse_args()
    result = parse_har(args.har_file, args.host)
    print(json.dumps(result, indent=2))

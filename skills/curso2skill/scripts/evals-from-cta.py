#!/usr/bin/env python3
"""
evals-from-cta.py -- Fase 2.5 do /curso2skill

Converte os outputs da Fase 1 (CTA matrices) em evals.json no formato
esperado pelo skill-creator (Fase 3).

Uso:
    python3 evals-from-cta.py <skill-path>

Le:
    <skill-path>/.curso2skill/03-simulation-cdm.md

Escreve:
    <skill-path>/scripts/evals/evals.json
"""

import sys
import re
import json
from pathlib import Path
from datetime import date


def parse_simulation_table(text):
    """Extrai incidentes do markdown 03-simulation-cdm.md."""
    incidents = []
    pattern = re.compile(r'^## Incidente \d+:.*?(?=^## |\Z)', re.MULTILINE | re.DOTALL)
    for match in pattern.finditer(text):
        block = match.group(0)
        title_match = re.match(r'## Incidente \d+:\s*"?([^"\n]+)"?', block)
        if not title_match:
            continue
        title = title_match.group(1).strip(' "')

        def grab(field):
            m = re.search(rf'\|\s*{field}\s*\|\s*(.+?)\s*\|', block)
            return m.group(1).strip() if m else None

        incident = {
            'title': title,
            'source': grab('Source'),
            'situacao': grab('Situacao'),
            'cues': grab('Cues a checar'),
            'assessment': grab('Assessment'),
            'decision': grab('Decision'),
            'common_error': grab('Common error'),
            'counterfactuals': re.findall(r'\|\s*Counterfactual \w\s*\|\s*(.+?)\s*\|', block)
        }
        incidents.append(incident)
    return incidents


def slugify(text, max_len=40):
    """Converte string em kebab-case."""
    if not text:
        return 'unnamed'
    s = re.sub(r'[^a-zA-Z0-9\s-]', '', text.lower())
    s = re.sub(r'\s+', '-', s).strip('-')
    return s[:max_len]


def incident_to_scenario(eid, incident):
    """Converte 1 incidente da CDM em 1 cenario de teste."""
    name = slugify(incident['title'])
    prompt = incident.get('situacao') or f"Cenario: {incident['title']}"

    assertions = []
    if incident.get('decision'):
        assertions.append({
            'type': 'contains_positive',
            'text': f"output reflete decisao: {incident['decision'][:80]}",
            'source_cta': incident.get('source', 'simulation-cdm')
        })
    if incident.get('common_error'):
        assertions.append({
            'type': 'avoids_negative',
            'text': f"nao comete erro comum: {incident['common_error'][:80]}",
            'source_cta': incident.get('source', 'simulation-cdm')
        })

    return {
        'id': eid,
        'name': name,
        'prompt': prompt,
        'expected_output': incident.get('decision', ''),
        'assertions': assertions
    }


def counterfactual_to_scenario(eid, parent_incident, cf_text):
    """Converte 1 counterfactual em cenario variante."""
    return {
        'id': eid,
        'name': slugify(parent_incident['title']) + '-cf',
        'prompt': cf_text,
        'expected_output': '',
        'assertions': [
            {
                'type': 'contains_positive',
                'text': 'reflete principios da skill em variacao do cenario',
                'source_cta': parent_incident.get('source', 'simulation-cdm-counterfactual')
            }
        ]
    }


def main():
    if len(sys.argv) < 2:
        print('usage: evals-from-cta.py <skill-path>', file=sys.stderr)
        sys.exit(1)

    skill_path = Path(sys.argv[1])
    cdm_file = skill_path / '.curso2skill' / '03-simulation-cdm.md'
    if not cdm_file.exists():
        print(f'error: {cdm_file} not found', file=sys.stderr)
        sys.exit(2)

    cdm_text = cdm_file.read_text(encoding='utf-8')
    incidents = parse_simulation_table(cdm_text)

    if not incidents:
        print('warning: 0 incidents parsed -- check 03-simulation-cdm.md format', file=sys.stderr)

    scenarios = []
    eid = 1
    for incident in incidents:
        scenarios.append(incident_to_scenario(eid, incident))
        eid += 1
        for cf in incident.get('counterfactuals', []):
            scenarios.append(counterfactual_to_scenario(eid, incident, cf))
            eid += 1

    skill_name = skill_path.name
    output = {
        'skill_name': skill_name,
        'description': f'Cenarios derivados da Fase 1 CTA do curso {skill_name}',
        'evals': scenarios,
        'thresholds': {
            'pass_rate_min': 0.80,
            'knowledge_delta_min': 0.30,
            'pass_k3_min': 0.7
        },
        'metadata': {
            'generated_by': '/curso2skill (evals-from-cta.py)',
            'source_cta_dir': str(skill_path / '.curso2skill'),
            'n_incidents': len(incidents),
            'n_scenarios': len(scenarios),
            'generated_at': str(date.today())
        }
    }

    out_path = skill_path / 'scripts' / 'evals' / 'evals.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f'OK {len(scenarios)} cenarios gerados ({len(incidents)} incidentes + counterfactuals)')
    print(f'   -> {out_path}')


if __name__ == '__main__':
    main()

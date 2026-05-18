#!/usr/bin/env python3
"""
PostToolUse hook validator para relatorios /pesquisa.

Roda apos Write em ~/pesquisas/*.md. Valida que o relatorio tem:
1. Todas as secoes obrigatorias do formato declarado em SKILL.md
2. Cada fato-chave com >=2 fontes independentes (dominios diferentes)
3. Confianca declarada bate com evidencia real
4. CRAAP scores acompanhados de evidencia por criterio (nao so total)

Exit codes:
- 0: valido, deixa passar
- 2: invalido, bloqueia (formato Claude Code hook)

JSON output em stderr com `permissionDecision: "deny"` + `permissionDecisionReason`.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


REQUIRED_SECTIONS = [
    "Resumo Executivo",
    "Comparativo Final",
    "Recomendacao",
    "Contradicoes Identificadas",
    "Status dos Fatos-Chave",
    "Fontes Avaliadas",
]

CONFIANCA_RULES = {
    "ALTA": "todos fatos-chave com >=2 fontes Tier A/B",
    "MEDIA": "maioria dos fatos com >=2 fontes, algumas Tier C",
    "BAIXA": "fatos com fonte unica ou predominancia Tier C/D",
}


def read_hook_input():
    """Le JSON do stdin (formato PostToolUse hook)."""
    try:
        return json.load(sys.stdin)
    except Exception as e:
        if len(sys.argv) > 1:
            return {"toolInput": {"file_path": sys.argv[1]}}
        sys.stderr.write(f"hook input parse fail: {e}\n")
        return None


def deny(reason, context="", event="PreToolUse"):
    """Emite JSON de bloqueio + exit 2."""
    out = {
        "hookSpecificOutput": {
            "hookEventName": event,
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
            "additionalContext": context,
        }
    }
    print(json.dumps(out))
    sys.stderr.write(f"VALIDATION FAILED: {reason}\n")
    sys.exit(2)


def warn_only(reason):
    """Emite warning mas permite."""
    out = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": f"Warning /pesquisa validator: {reason}",
        }
    }
    print(json.dumps(out))
    sys.exit(0)


def extract_facts_table(content):
    """Extrai tabela 'Status dos Fatos-Chave'."""
    pattern = r"## Status dos Fatos-Chave\s*\n(.*?)(?=\n##|\Z)"
    m = re.search(pattern, content, re.DOTALL)
    if not m:
        return None
    section = m.group(1)
    rows = []
    for line in section.split("\n"):
        if re.match(r"^\|.*\|.*\|.*\|", line) and "---" not in line and "Fato" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 3:
                rows.append({
                    "fato": cells[0],
                    "fontes": cells[1],
                    "status": cells[2],
                })
    return rows


def count_independent_domains(fontes_str):
    """Conta dominios DISTINTOS em string de fontes."""
    parts = re.split(r"\s*[\+,]\s*|\s+e\s+", fontes_str, flags=re.IGNORECASE)
    parts = [p.strip() for p in parts if p.strip()]

    domains = set()
    non_url_sources = set()
    for p in parts:
        urls = re.findall(r"https?://[^\s\)]+", p)
        if urls:
            for u in urls:
                try:
                    d = urlparse(u).netloc.replace("www.", "")
                    if d:
                        domains.add(d)
                except Exception:
                    pass
        else:
            cleaned = re.sub(r"^\d+\s+", "", p).strip().lower()
            if cleaned:
                non_url_sources.add(cleaned)

    return {
        "url_domains": len(domains),
        "url_domain_list": sorted(domains),
        "non_url_sources": len(non_url_sources),
        "non_url_list": sorted(non_url_sources),
    }


def extract_confianca(content):
    """Extrai declaracao de confianca do Resumo Executivo."""
    m = re.search(
        r"\*?\*?[Cc]onfian[cc]a\s+(?:geral:?\s+)?(\*?\*?)(ALTA|MEDIA|BAIXA|ALTO|MEDIO|BAIXO)",
        content,
    )
    if m:
        return m.group(2).upper()
    return None


def extract_craap_scores(content):
    """Extrai scores CRAAP."""
    scores = []
    pattern = r"score\s+(\d+)"
    for m in re.finditer(pattern, content):
        scores.append(int(m.group(1)))
    return scores


def validate(file_path, content=None):
    """Validacao principal."""
    p = Path(file_path).expanduser()

    if not str(p).startswith(str(Path.home() / "pesquisas")):
        return True, "fora de ~/pesquisas/", ""

    if not p.suffix == ".md":
        return True, "nao e .md", ""

    if content is None:
        if not p.exists():
            return True, "arquivo nao existe", ""
        content = p.read_text()

    # Check 1: secoes obrigatorias
    missing_sections = []
    for section in REQUIRED_SECTIONS:
        if not re.search(rf"##\s+{re.escape(section)}", content):
            missing_sections.append(section)

    if missing_sections:
        return False, (
            f"Relatorio /pesquisa em {p.name} esta faltando secao(oes) obrigatoria(s): "
            f"{', '.join(missing_sections)}. Adicione antes de finalizar."
        ), f"Secoes esperadas: {REQUIRED_SECTIONS}"

    # Check 2: fatos-chave com >=2 fontes independentes
    facts = extract_facts_table(content)
    if facts is None:
        return False, "Tabela 'Status dos Fatos-Chave' nao encontrada ou mal formatada.", ""

    weak_facts = []
    for f in facts:
        sources_info = count_independent_domains(f["fontes"])
        effective_count = sources_info["url_domains"] + (sources_info["non_url_sources"] * 0.5)
        if effective_count < 2:
            weak_facts.append({
                "fato": f["fato"][:80],
                "url_domains": sources_info["url_domain_list"],
                "non_url": sources_info["non_url_list"],
                "effective": effective_count,
            })

    # Check 3: Confianca declarada coerente
    confianca = extract_confianca(content)
    n_facts_full = sum(1 for f in facts if "confirmado" in f["status"].lower())
    n_facts_total = len(facts)
    pct_confirmed = (n_facts_full / n_facts_total) if n_facts_total else 0

    confianca_warning = None
    if confianca == "ALTA" and pct_confirmed < 0.9:
        confianca_warning = (
            f"Confianca declarada ALTA mas so {n_facts_full}/{n_facts_total} fatos "
            f"({pct_confirmed:.0%}) marcados como confirmados. Revisar."
        )

    if weak_facts and len(weak_facts) > len(facts) // 2:
        return False, (
            f"Mais da metade dos fatos-chave ({len(weak_facts)}/{len(facts)}) tem <2 fontes "
            f"independentes. Skill /pesquisa exige >=2 fontes Tier A/B para Confianca ALTA."
        ), json.dumps(weak_facts, ensure_ascii=False, indent=2)

    warnings = []
    if weak_facts:
        warnings.append(f"{len(weak_facts)} fato(s)-chave com <2 fontes (URLs distintas): "
                        + ", ".join(f["fato"][:40] for f in weak_facts[:3]))
    if confianca_warning:
        warnings.append(confianca_warning)

    scores = extract_craap_scores(content)
    if scores and (max(scores) - min(scores)) < 8:
        warnings.append(f"Distribuicao de CRAAP scores muito apertada ({min(scores)}-{max(scores)}) "
                        f"-- sugere auto-justificacao. Revisar criterios individuais.")

    if warnings:
        return True, "warnings", " | ".join(warnings)

    return True, "ok", "Validacao passou: todas secoes presentes, fatos-chave com fontes adequadas."


def main():
    hook_input = read_hook_input()
    if not hook_input:
        sys.exit(0)

    tool_input = hook_input.get("tool_input") or hook_input.get("toolInput") or {}
    file_path = tool_input.get("file_path") or tool_input.get("path")

    if not file_path:
        sys.exit(0)

    tool_name = hook_input.get("tool_name") or hook_input.get("toolName", "")
    content = None
    if tool_name == "Write":
        content = tool_input.get("content")
    elif tool_name == "Edit":
        sys.exit(0)

    ok, reason, context = validate(file_path, content=content)

    if not ok:
        deny(reason, context)
    elif reason == "warnings":
        warn_only(context)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()

---
name: curso2skill
description: >
  Transforma curso ja-extraido (output do /extrair-curso) em uma skill operacional
  Anthropic-compatible que codifica o JULGAMENTO do instrutor, nao so o conteudo.
  Use quando o usuario rodar "/curso2skill nome-do-curso", ou disser "vira esse curso em
  skill", "transforma o curso X em skill", "destila esse curso". O metodo aplica
  CTA (Cognitive Task Analysis) na transcricao pra reconstruir decisoes implicitas,
  encoda como prompt hibrido (decision tables + 1-3 exemplos limitrofes + scaffold),
  e gera eval suite automaticamente derivada da propria CTA. Delega validacao ao
  skill-creator ao final do pipeline.
---

# curso2skill -- destilador de curso -> skill operacional

A skill e **conversacional**, com 4 fases sequenciais (FASE 0 -> 1 -> 2 -> 3) e HITL nos pontos criticos. Nao usa flags pra controlar fluxo principal -- adapta automaticamente ao tipo de curso.

## Principio chave

**A skill resultante codifica JULGAMENTO, nao conteudo.** Se o curso vem com artifacts destilados (PDFs, frameworks, checklists), a skill nova e principalmente **transcodificacao** -- copia artifacts pra `references/` e constroi switchboard. Se o curso e so transcricao (video bruto), o metodo aplica **CTA real** pra reconstruir tacito.

## Pre-requisitos

1. Curso ja extraido via `/extrair-curso` em `~/cursos/<slug>/`
2. Pelo menos transcricoes `.md` + `.json` por aula
3. Skill `/etl-audio` instalada (caso precise re-transcrever aulas faltantes)
4. Acesso a Skill tool pra invocar `skill-creator` na Fase 3

## Sintaxe

```
/curso2skill <slug>                  -> standard (default, completo)
/curso2skill <slug> --depth=light    -> so transcodificacao (rich artifacts)
/curso2skill <slug> --depth=full     -> + eval suite expandida
/curso2skill <slug> --dry-run        -> nao escreve arquivos, so relatorio
/curso2skill <slug> --resume         -> retoma de onde parou
```

**Sem argumentos: auto-listar cursos disponiveis e perguntar via `AskUserQuestion`.**

---

## FASE 0 -- Inventario & classificacao (~1 min)

### Passo 1: inventario

Roda `scripts/00-inventory.sh <slug>` que produz JSON com:
- N aulas, layout (`flat` ou `multi-module`), contagem por extensao
- Materiais anexados (PDFs/ZIPs/DOCXs/PNGs/JPGs)
- Total de tokens estimados das transcricoes
- Status de extracao: cobertura como `(N_MD + N_TXT) / max(N_AULAS, N_MP4)`

### Passo 2: classificacao automatica

| Tipo | Condicoes | Estrategia |
|---|---|---|
| **A -- Rich artifacts** | Materiais `.pdf`/`.zip`/`.docx` >50KB total | TRANSCODIFICACAO: copy artifacts -> references/, switchboard SKILL.md |
| **B -- Transcript-only** | So transcricoes, sem materiais decisao-densos | CTA REAL: extrair tacito, construir decision tables |
| **C -- Incomplete** | >20% das aulas sem transcricao | BLOQUEIA: orienta rodar `/extrair-curso <slug> --redo` antes |

### Passo 3: definir nome + escopo (HITL)

**REGRA INVIOLAVEL DE NAMING:** Skills derivadas de cursos SEMPRE usam o prefixo `curso-*`.

Default = `curso-<slug>`. So perguntar se houver ambiguidade real.

---

## FASE 1 -- CTA: Arqueologia cognitiva (~3-5 min)

Para Tipo B (transcript-only) ou Tipo A com gaps. Para Tipo A puro, pula direto pra Fase 2.

**Cursos massivos (>500K tokens OU >50 aulas OU layout multi-module com >=5 submodulos)**: NÃO faca CTA em uma so passada. Estrategia de chunking por BLOCO TEMATICO (3-5 blocos).

### Sub-fase 1.1: Task Diagram

Le transcricoes + sumariza estrutura macro. Output: 3-7 macro-passos da tarefa central.
Prompt template em `scripts/cta-task-diagram.md`. Saida em `<workspace>/01-task-diagram.md`.

### Sub-fase 1.2: Knowledge Audit (com tags)

Para cada macro-passo, le transcricoes associadas e popula matriz:
`| Step | Cue | Strategy/Rule | Common error | Expert vs Novice | Tag |`

Tag obrigatoria:
- Green (Explicito): instrutor disse direto
- Yellow (Tacito-surfaced): implicito em demos/cases
- Red (Inferido): voce (Claude) deduziu -- precisa validacao humana

**HITL**: apresenta os Red ao user pra validar antes de prosseguir.

Prompt em `scripts/cta-knowledge-audit.md`. Saida em `<workspace>/02-knowledge-audit.md`.

### Sub-fase 1.3: Simulation/CDM

Identifica "incidentes" no curso. Para cada um: Situacao, Cues, Assessment, Decisao+rationale, Counterfactuals.

Counterfactuals = combustivel pra eval scenarios na Fase 3.

Prompt em `scripts/cta-simulation.md`. Saida em `<workspace>/03-simulation-cdm.md`.

### Sub-fase 1.4: Execution Inventory (CONDICIONAL)

**Obrigatoria** quando `00-inventory.sh` retorna `has_executable_pipeline: true`.

Extrair: Stack tecnologica, Pipeline canonico (steps executaveis), Triggers, Side-effects.

Prompt em `scripts/cta-execution-inventory.md`. Saida em `<workspace>/04-execution-inventory.md`.

---

## FASE 2 -- Encoding hybrid (~2 min)

### Sub-fase 2.1: SKILL.md (switchboard)

Constroi SKILL.md com:
1. Frontmatter (name, description com triggers)
2. Workflow N-passos
3. Decision tables CRITICAS
4. Casos canonicos do instrutor (tabela nomeando 5-10 cases mais densos)
5. 1 exemplo limitrofe (case mais dificil da Simulation/CDM)
6. Politica de uso de references

Limite: **<=500 linhas**.

### Sub-fase 2.5: gerar evals.json (CRITICO)

Cada Simulation/CDM table vira um eval. Mapeamento:
- `Cue` -> `prompt` do eval
- `Decision` -> `assertion contains_positive`
- `Common error` -> `assertion avoids_negative`
- `Counterfactual` -> eval adicional

Script: `scripts/evals-from-cta.py`

---

## FASE 3 -- Validacao (delega ao skill-creator)

### Criterios de aceitacao

| Criterio | Threshold |
|---|---|
| Pass rate (with skill) | >= 80% |
| Knowledge delta (with - baseline) | >= +30pp |
| Pass^k=3 (consistencia) | >= 0.7 |

Se qualquer um falhar -> relata gap e propoe iteracao especifica.

---

## Output final

```
Skill <nome> em ~/.claude/skills/<nome>/
Eval suite preservada em scripts/evals/
Workspace de geracao em .curso2skill/ (debug, pode descartar)

Metricas finais:
   Pass rate: <X>%
   Knowledge delta: +<Y>pp
   Linhas SKILL.md: <N> (limite <=500)
```

---

## Quando NAO usar /curso2skill

- Curso ainda nao extraido -> use `/extrair-curso` antes
- Curso e tutorial avulso de 1 video -> `skill-creator` direto
- Quer so FAQ do curso -> use RAG simples, nao skill operacional
- Conteudo e pura informacao factual sem julgamento

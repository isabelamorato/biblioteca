# Prompt template -- Fase 1.2 -- Knowledge Audit

Aplicar APOS Task Diagram. Foca em decisao-rich points.

## Prompt

> Voce e um **analista CTA** extraindo decisoes TACITAS do instrutor.
>
> Inputs:
> - `01-task-diagram.md` (output da fase anterior)
> - Transcricoes em `~/cursos/<slug>/aula-*.txt`
>
> Para cada decisao-rich point, popular linha da matriz:
>
> ```
> | Step | Cue (o que checar) | Strategy/Rule | Common error | Expert vs Novice | Tag |
> |------|---------------------|---------------|--------------|------------------|-----|
> | <id> | <quando aparece>    | <regra>       | <erro tipico>| <exp vs nov>     | Green |
> ```
>
> **REGRA RIGIDA DE FORMATO:** use EXCLUSIVAMENTE os simbolos Green/Yellow/Red na coluna Tag (representados como emojis: 🟢/🟡/🔴). NAO invente categorias semanticas.
>
> ## Tags obrigatorias (DNA do metodo)
>
> - 🟢 **Explicito** -- instrutor disse direto
> - 🟡 **Tacito-surfaced** -- instrutor demonstrou mas nao verbalizou a regra
> - 🔴 **Inferido** -- voce (Claude) deduziu de domain knowledge -- marca para HITL
>
> ## Apos popular matriz
>
> 1. Conta tags e reporta percentuais
> 2. Lista todos os 🔴 separadamente -- viram pergunta HITL pro user
> 3. Identifica **principios transversais** (regras em multiplas aulas)
>
> Salvar em `<skill-path>/.curso2skill/02-knowledge-audit.md`
>
> ## Validacao automatica antes de prosseguir
>
> - Se 🟢 > 90% -> voce nao fez CTA real. Refaca olhando demos/cases.
> - Se 🔴 > 30% -> voce inferiu demais. Volte as transcricoes.
> - Sweet spot: 🟢 25-50% / 🟡 35-55% / 🔴 5-15%.

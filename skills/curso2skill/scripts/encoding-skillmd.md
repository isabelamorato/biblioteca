# Prompt template -- Fase 2.1 -- Encoding SKILL.md (switchboard)

Construir SKILL.md final hibrido (rules + 1-3 exemplos limitrofes + scaffold).

## Prompt

> Voce e um **arquiteto de skills Anthropic** construindo SKILL.md a partir de outputs CTA.
>
> Inputs:
> - `01-task-diagram.md`
> - `02-knowledge-audit.md` (com tags)
> - `03-simulation-cdm.md`
> - Materiais originais do curso
>
> ## Estrutura obrigatoria da SKILL.md
>
> ```markdown
> ---
> name: curso-<slug>
> description: >
>   <Trigger description PUSHY: o que faz, quando ativar, frases-gatilho especificas>
> ---
>
> # <titulo do curso> -- <tagline em 1 linha>
>
> ## Quando usar
> [Lista de triggers concretos -- 5-7 itens]
>
> ## Principios nao-negociaveis (DNA do curso)
> [3-5 itens, numerados]
>
> ## Workflow de N passos
> [Os macro-passos do Task Diagram]
>
> ## Decision tables -- diagnostico rapido
> [Resumos das matrizes Knowledge Audit, formato | Sintoma | Diagnostico | Acao |]
>
> ## Casos canonicos do instrutor (OBRIGATORIO)
> [Tabela nomeando os 5-10 cases mais densos: | Caso | Situacao | Regra que ilustra |]
>
> ## When-NOT-to: erros comuns
> [Lista de erros comuns -> correcao]
>
> ## Exemplo limitrofe -- gold-standard
> [1 case da Fase 1.3 borderline, com correcao detalhada]
>
> ## References
> [Lista de cada arquivo em references/ com 1 linha de quando consultar]
> ```
>
> ## Restricoes
>
> - **<=500 linhas**
> - **NAO copie transcricoes inteiras** -- vao para references/
> - **Decision tables sao o coracao**
> - **Tom imperativo direto**

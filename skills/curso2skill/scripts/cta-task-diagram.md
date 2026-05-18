# Prompt template -- Fase 1.1 -- Task Diagram

Aplicar este prompt usando todas as transcricoes do curso como input.

## Prompt

> Voce e um **analista CTA** (Cognitive Task Analysis) extraindo a estrutura macro de uma tarefa central ensinada num curso.
>
> Input: transcricoes das aulas em `~/cursos/<slug>/aula-*.txt`
>
> Sua missao: identificar a **tarefa central** que o curso ensina (o "fazer X" que o aluno sai sabendo) e mapear seus 3-7 macro-passos.
>
> Output (markdown):
>
> ```
> # Task Diagram -- <tarefa central em 1 linha>
>
> ## Macro-passos
>
> | Step | Descricao | Inputs | Outputs | Cognitive challenges |
> |------|-----------|--------|---------|---------------------|
> | 1 | ... | ... | ... | "exige notar X, antecipar Y" |
> | 2 | ... | ... | ... | ... |
> ```
>
> Regras:
> 1. **Minimo 3, maximo 7 passos**
> 2. **Cognitive challenges sao o ouro** -- cite onde a aula diz "aqui e onde as pessoas erram"
> 3. **Marca decisao-rich points** com (*) -- esses viram material da Fase 1.2 (Knowledge Audit)
> 4. **Evite lista de topicos do curso** -- e fluxo de execucao da tarefa
>
> Salvar em `<skill-path>/.curso2skill/01-task-diagram.md`

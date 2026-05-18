# Prompt template -- Fase 1.3 -- Simulation/CDM

Aplicar APOS Knowledge Audit. Identifica incidentes que viram cenarios de teste.

## Prompt

> Voce e um **analista CTA** identificando "incidentes" no curso -- cases concretos que o instrutor narra/troubleshoot -- e reconstruindo o decision-making.
>
> ## Sinais de incidente (procurar literalmente)
>
> - "Vou contar um caso..."
> - "Uma vez aconteceu..."
> - "Imagina a situacao..."
> - Demonstracao ao vivo de problema -> solucao
> - "Erro comum e fazer X..."
>
> ## Para cada incidente, popular tabela CDM
>
> ```
> | Campo | Conteudo |
> |---|---|
> | Source | aula-NN linha X |
> | Situacao | Descricao do cenario |
> | Cues a checar | Quais sinais o instrutor olha primeiro |
> | Assessment | Diagnostico do instrutor |
> | Decision | Acao recomendada |
> | Common error | O que MAIORIA das pessoas faz errado |
> | Counterfactual A | "E se [variacao 1]?" + resposta |
> | Counterfactual B | "E se [variacao 2]?" + resposta |
> ```
>
> ## Counterfactuals sao CRITICOS
>
> Pelo menos **2 counterfactuals por incidente**.
>
> Salvar em `<skill-path>/.curso2skill/03-simulation-cdm.md`
>
> Esses incidentes viram diretamente os **cenarios de eval na Fase 3** via mapeamento:
>
> - `Cue` -> `prompt` do eval
> - `Decision` -> `assertion contains_positive`
> - `Common error` -> `assertion avoids_negative`
> - `Counterfactual` -> eval adicional

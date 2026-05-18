# Prompt template -- Fase 1.4 -- Execution Inventory

**Esta fase e OBRIGATORIA** quando `00-inventory.sh` retorna `has_executable_pipeline: true`.

CTA tradicional (1.1-1.3) extrai julgamento. Mas cursos modernos frequentemente embutem **pipeline executavel** dentro do system-prompt, do guia de boas-praticas, ou de scripts de exemplo.

## Prompt

> Voce e um **engenheiro de skills** extraindo o pipeline executavel do curso (comandos, dependencias, file I/O).
>
> ## Sua missao
>
> Extrair **TODA execucao tecnica** documentada no curso:
> 1. Dependencias externas (ferramentas, libs, pacotes)
> 2. Comandos canonicos (bash, python, etc.) com inputs/outputs explicitos
> 3. File I/O (que arquivos a skill le/escreve)
> 4. Triggers/eventos (o que dispara cada step)
> 5. Side-effects (instala coisa? cria pasta? consome quota de API?)
>
> ## Output (markdown estruturado)
>
> ```markdown
> # Execution Inventory -- <skill-name>
>
> ## Stack tecnologica
>
> | Camada | Tool/Lib | Versao | Razao (do curso) |
> |--------|----------|--------|------------------|
>
> ## Pipeline canonico (steps executaveis)
>
> 1. STEP_NAME
>    Comando: ...
>    Input: ...
>    Output: ...
>    Quando: ...
>
> ## Triggers e estado
>
> | Trigger | Estado anterior | Acao | Estado posterior |
> |---------|-----------------|------|------------------|
>
> ## Side-effects e atencoes
>
> - Consome quota de API?
> - Instala coisa global?
> - Cria pastas? Quais paths?
> ```
>
> ## Regras
>
> 1. Se o material cita comando concreto, copie literal
> 2. Se trigger tem palavra-chave especifica, preserve o vocabulario exato
> 3. Se versao importa, preserve o caveat
> 4. Se houve workaround, TAG como tacito-surfaced
>
> Salvar em `<skill-path>/.curso2skill/04-execution-inventory.md`

# Knowledge Audit -- Dominando Claude Code

Tags: Green = Explicito | Yellow = Tacito-surfaced | Red = Inferido (requer validacao)

## Passo 1 -- Instalar ambiente

| # | Cue (situacao) | Strategy/Rule | Common error | Tag |
|---|---|---|---|---|
| 1 | Usuario no Windows | Usar PowerShell 7 (nao CMD, nao terminal comum) para instalar e rodar Claude Code | Abrir o "Windows PowerShell" antigo (5.1) em vez do PowerShell 7 | Green |
| 2 | Primeiro erro de instalacao | Copiar o erro, jogar no app do Claude e pedir orientacao passo a passo | Tentar resolver o erro na forca bruta sem usar a propria IA | Green |
| 3 | Precisa instalar dependencias | Claude orienta: pode precisar de Node.js e Git. Instalar conforme instrucao | Ignorar dependencias e tentar rodar sem elas | Green |
| 4 | Usuario em Mac | Usar Cmd+Shift+. para revelar pastas ocultas e encontrar `.claude` | Nao saber que `.claude` e pasta oculta | Green |
| 5 | Decidindo terminal vs VS Code | Terminal = tarefas do dia a dia. VS Code = construcao de sistemas | Usar so o app/browser -- perde 80% do poder | Green |

## Passo 2 -- Configurar CLAUDE.md

| # | Cue (situacao) | Strategy/Rule | Common error | Tag |
|---|---|---|---|---|
| 6 | Criando o CLAUDE.md do zero | Incluir: nome, empresa, produtos, linguagem, tom de resposta, o que nao quer que erre | Deixar vazio ou superficial -- perde personalizacao | Green |
| 7 | Nao sabe o que colocar | Pedir ao proprio Claude: "me ajude a criar meu CLAUDE.md" | Tentar escrever tudo manualmente sem orientacao | Green |
| 8 | CLAUDE.md vs memory.md | CLAUDE.md = brief fixo de identidade. memory.md = memoria dinamica | Confundir os dois e misturar tudo num so arquivo | Yellow |

## Passo 3 -- Construir memory.md

| # | Cue (situacao) | Strategy/Rule | Common error | Tag |
|---|---|---|---|---|
| 9 | Quer guardar uma regra importante | Falar para o Claude: "guarda isso na memoria" -- ele atualiza o memory.md automaticamente | Depender de reconfigurar tudo na proxima conversa | Green |
| 10 | Claude cometeu um erro de comportamento | Instruir: "nunca mais faca X" + pedir para gravar na memoria | So corrigir na conversa atual, erro volta na proxima sessao | Yellow |
| 11 | Quer memoria mais poderosa | Usar Obsidian para criar uma rede de memorias interligadas | Usar apenas um arquivo memory.md plano e simples | Yellow |

## Passo 4 -- Criar skills

| # | Cue (situacao) | Strategy/Rule | Common error | Tag |
|---|---|---|---|---|
| 12 | Criando skill simples | Estrutura minima: pasta com nome da skill + arquivo skill.md dentro | Criar skill.md na raiz sem pasta propria | Green |
| 13 | Skill precisa executar algo real | Adicionar pasta `scripts/` dentro da skill -- sem scripts, a skill nao tem poder de execucao | Criar so skill.md e achar que vai executar por si so | Green |
| 14 | Nao sabe o que escrever no skill.md | Pedir ao Claude para gerar: incluir nome, descricao, quando ativar, o que fazer, referencias | Escrever skill.md vago sem "quando ativar" | Green |
| 15 | Skill com ferramenta externa | Especificar a tool e deixar Claude gerar o script de conexao | Assumir que a skill vai encontrar a ferramenta sozinha | Green |
| 16 | Skill vs agente | Skill = capacidade/habilidade especifica. Agente = funcionario que usa multiplas skills | Chamar tudo de "agente" e nao estruturar skills separadas | Yellow |

## Passo 5 -- Construir agentes

| # | Cue (situacao) | Strategy/Rule | Common error | Tag |
|---|---|---|---|---|
| 17 | Criando agente novo | Abrir arquivo .md na pasta `agents/` e dar nome descritivo | Criar agente sem especificar personalidade, tom e skills | Green |
| 18 | Agente sem contexto | Incluir no .md do agente: personalidade, instrucoes, referencia as skills, referencia a memoria | Fazer agente generico que nao sabe com quem esta falando | Green |
| 19 | Agente precisa de API/ferramenta | Informar qual ferramenta tem API, deixar Claude gerar script de integracao | Tentar conectar ferramenta sem API disponivel | Yellow |
| 20 | Agente de WhatsApp | Especificar: nome, personalidade, skills de WhatsApp, tom de comunicacao | Criar agente generico sem regras de comunicacao por contexto | Yellow |

## Passo 6 -- Operar com FPCN

| # | Cue (situacao) | Strategy/Rule | Common error | Tag |
|---|---|---|---|---|
| 21 | Antes de qualquer construcao | Falar (F) -> Planejar (P) -> Confrontar (C) -> Executar (N). Nunca executar direto | Pedir execucao direta sem planejamento | Green |
| 22 | Fase Falar (F) | Falar de forma humanizada, na sua linguagem natural | Tentar usar linguagem "tecnica" ou robotica com a IA | Green |
| 23 | Fase Planejar (P) | Pedir: "antes de criar, me mostra o plano" ou ativar /plan mode | Pular o planejamento e ir direto para a construcao | Green |
| 24 | Fase Confrontar (C) | Depois do plano: "acho que voce foi superficial, pode ir mais fundo?" | Aceitar o primeiro plano sem questionar | Green |
| 25 | Plano aprovado | So entao liberar a execucao: "agora pode executar" | Interromper a execucao no meio sem necessidade | Yellow |

## Heuristicas gerais Red (inferidas -- validar com instrutor)

| # | Heuristica | Raciocinio | Tag |
|---|---|---|---|
| 27 | Multiplos terminais em paralelo | JP menciona "2-3 terminais abertos com propositos diferentes" | Red |
| 28 | Base de conhecimento antes de builds complexos | Antes de construir sistema complexo, montar arquivo de boas praticas e arquitetura primeiro | Red |

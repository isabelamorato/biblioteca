# Task Diagram -- Dominando Claude Code

**Tarefa central**: Configurar e operar o Claude Code para automatizar operacoes reais de negocio (agentes, skills, sistemas), sem precisar saber programar.

## Macro-passos

| # | Passo | Descricao | Quando ativo |
|---|-------|-----------|-------------|
| 1 | **Instalar ambiente** | Instalar Claude Code no terminal (Mac: brew / Windows: PowerShell 7). Instalar VS Code + extensao Claude Code quando for construir sistemas. | Primeiro uso |
| 2 | **Configurar CLAUDE.md** | Criar o arquivo de identidade: quem voce e, sua empresa, produtos, linguagem preferida, o que nao quer que o Claude erre. Carregado em toda sessao. | Setup inicial + sempre que mudar contexto |
| 3 | **Construir memory.md** | Criar memoria persistente com regras, preferencias e informacoes de negocio. Instruir o Claude a guardar aprendizados ao longo do uso. | Setup inicial + refinamento continuo |
| 4 | **Criar skills** | Construir habilidades especificas (pasta + skill.md + scripts). Skill simples = so skill.md. Skill com execucao = precisa de scripts conectados a ferramentas. | Antes de criar agentes |
| 5 | **Construir agentes** | Criar funcionarios digitais (.md) com personalidade, instrucoes, skills atribuidas e conexoes com ferramentas (APIs, WhatsApp, CRM etc.). | Apos ter skills prontas |
| 6 | **Operar com FPCN** | Usar o framework Falar->Planejar->Confrontar->Executar para toda tarefa. Nunca executar direto. Usar Plan Mode antes de construir qualquer coisa. | Em toda interacao |

## Estrutura de pasta obrigatoria

```
~/.claude/
|-- CLAUDE.md          <- identidade/brief do usuario
|-- memory.md          <- memoria persistente
|-- agents/            <- agentes (funcionarios)
|   `-- nome-agente.md
`-- skills/            <- habilidades
    `-- nome-skill/
        |-- skill.md
        `-- scripts/   <- necessario para execucao real
```

## Hierarquia conceitual

```
Agente = CLAUDE.md + memory.md + skills + ferramentas
Skill simples = pasta/ + skill.md
Skill avancada = pasta/ + skill.md + scripts/
```

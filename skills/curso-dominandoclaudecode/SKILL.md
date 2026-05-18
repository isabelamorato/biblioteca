---
name: curso-dominandoclaudecode
description: Use quando o usuario perguntar sobre Claude Code, como instalar, configurar CLAUDE.md, memory.md, criar skills ou agentes, usar o framework FPCN, fazer vibe coding, construir automacoes, ou transformar sua operacao com IA -- especialmente contexto brasileiro de negocios. Ative tambem quando o usuario disser "quero criar um agente", "como faco uma skill", "como configuro meu Claude", "quero automatizar X na minha empresa", ou qualquer referencia ao metodo do JP / Brave School.
---

# Dominando Claude Code -- Metodo JP / Brave School

## Quando usar esta skill

- Usuario quer instalar ou configurar Claude Code
- Usuario pergunta sobre CLAUDE.md, memory.md, agents/, skills/
- Usuario quer criar um agente ou uma skill do zero
- Usuario quer automatizar uma area do negocio sem saber programar
- Usuario menciona "vibe coding", "FPCN", "funcionarios digitais"
- Qualquer duvida sobre estrutura de pastas do `.claude`

---

## Os 4 Pilares do Claude Code

> **Pasta magica**: `~/.claude/` -- criada automaticamente na instalacao. Tudo vive aqui.

| Pilar | Arquivo/Pasta | O que e |
|---|---|---|
| 1 | `CLAUDE.md` | Identidade -- brief de quem e o usuario, carregado em toda sessao |
| 2 | `memory.md` | Memoria viva -- regras acumuladas, aprendizados, preferencias persistentes |
| 3 | `skills/` | Habilidades -- capacidades especificas (com ou sem execucao) |
| 4 | `agents/` | Funcionarios -- juntam CLAUDE.md + memoria + skills + ferramentas |

---

## Workflow: Configuracao inicial (6 passos)

**Passo 1 -- Instalar ambiente**
- Mac: rodar comando brew no terminal
- Windows: rodar comando no PowerShell 7 (nao o Windows PowerShell antigo 5.1)
- Erro na instalacao? Copiar o erro e pedir orientacao ao proprio Claude app
- Terminal = uso diario/automacoes | VS Code = construcao de sistemas

**Passo 2 -- Criar CLAUDE.md**
```
Peca ao Claude: "me ajude a criar meu CLAUDE.md"
Incluir: nome, empresa, produtos, linguagem/girias, tom preferido, o que nao quer que erre
```

**Passo 3 -- Criar memory.md**
```
Criar o arquivo uma vez. Depois instruir: "guarda isso na memoria"
O Claude atualiza automaticamente a partir dai
```

**Passo 4 -- Criar skill**
- Skill simples: `~/.claude/skills/nome-skill/skill.md`
- Skill com execucao: adicionar pasta `scripts/` dentro
- Sem scripts -> so texto, sem poder de execucao

**Passo 5 -- Criar agente**
- Arquivo `.md` dentro de `~/.claude/agents/`
- Incluir: personalidade, tom, referencia as skills, nivel de autonomia
- Especificar qual ferramenta/API ele vai usar

**Passo 6 -- Operar com FPCN (sempre)**
Ver secao abaixo.

---

## Framework FPCN -- Regra de ouro

> **"Nunca execute direto. Sempre: Falar -> Planejar -> Confrontar -> Executar."**

| Letra | Fase | O que fazer |
|---|---|---|
| **F** | Falar | Fale de forma humanizada, na sua lingua, como faria com um funcionario |
| **P** | Planejar | Peca: "antes de criar, me mostra o plano" ou ative `/plan` |
| **C** | Confrontar | Questione: "voce foi superficial, pode ir mais fundo? Faltou X?" |
| **N** | Executar | So libere a execucao apos o plano estar aprovado |

**Beneficio**: Resultado 10x melhor + consumo 10x menor de tokens.

---

## Decision Tables criticas

### Quando usar terminal vs VS Code vs app?

| Situacao | Use |
|---|---|
| Tarefas do dia a dia, automacoes, relatorios | Terminal |
| Construir sistema, app, CRM, dashboard | VS Code + extensao Claude Code |
| Perguntas rapidas, revisao de texto | App/browser |

### Skill simples vs avancada?

| Situacao | Estrutura |
|---|---|
| Orientacao/texto (ex: copywriter) | `skills/nome/skill.md` apenas |
| Execucao real (consultar API, fazer acao) | `skills/nome/skill.md` + `scripts/` |

### Quanto colocar no CLAUDE.md vs memory.md?

| Tipo de info | Onde vai |
|---|---|
| Brief fixo (quem voce e, empresa, produtos) | `CLAUDE.md` |
| Regras aprendidas no uso, preferencias dinamicas | `memory.md` |
| Contexto de projeto especifico | Arquivo separado referenciado no memory.md |

---

## Casos canonicos do instrutor (JP)

| Caso | Situacao | Regra que ilustra |
|---|---|---|
| **HUP (ClickUp BR)** | Construiu sistema de gestao em 4h, economizou R$100k/ano | VS Code + vibe coding substitui time de dev para apps internos |
| **Ana (Agente Financeiro)** | Agente DRE+DFC conectado ao Conta Azul, criado ao vivo | Skill precisa de scripts para ter execucao real |
| **Carlinhos/WhatsApp** | Agente de WhatsApp com 40+ comandos, mais usado da operacao | Agente precisa de personalidade + skills + regras de comunicacao |
| **Agencia 12 agentes** | CEO cortou 3 salarios, economiza R$8k/mes em 2 semanas | 1 pessoa com Claude Code = 10 pessoas |
| **Juliana (RH)** | Tria 300 CVs/dia sem saber programar | Vibe coding funciona para qualquer area |
| **CRM com MCP** | CRM operado inteiramente via terminal/Claude Code | MCP = skill avancada para integracao com sistemas externos |
| **Davi Braga** | Leigo constroi sistema com base de conhecimento do JP | Base de conhecimento antes de builds complexos reduz retrabalho |

---

## Caso limitrofe: "Minha skill nao esta funcionando"

**Situacao**: Usuario criou skill mas Claude nao executa nada.

**Diagnostico** (em ordem):
1. A skill tem pasta `scripts/`? -> Sem scripts, nao ha execucao
2. O skill.md tem campo "quando ativar"? -> Sem isso, Claude nao sabe quando usar
3. O agente referencia a skill explicitamente? -> Adicionar: "consulte a skill X"
4. A ferramenta tem API disponivel? -> Sem API, nao ha integracao automatica

**Correcao**: Abrir o skill.md e scripts/. Pedir ao Claude para revisar e completar o que falta.

---

## Vocabulario do curso

| Termo | Significado |
|---|---|
| Vibe coding | Conversar com a IA em linguagem natural para ela construir o que voce quer |
| Funcionario digital | Agente configurado para uma area especifica |
| Pasta magica | `~/.claude/` -- cerebro do Claude Code |
| FPCN | Framework Falar->Planejar->Confrontar->Executar |
| Tool de uma skill | A ferramenta/API que a skill vai operar |
| MCP | Model Context Protocol -- skill avancada para integracao com sistemas externos |

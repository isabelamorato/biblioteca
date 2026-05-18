# Simulation / CDM -- Dominando Claude Code

## Caso 1 -- HUP: ClickUp Brasileiro

| Campo | Detalhe |
|---|---|
| **Situacao** | JP e time usavam ClickUp (R$15-20k/mes em ferramentas externas). Precisavam de sistema de gestao de projetos proprio. |
| **Cues** | Custo alto de ferramentas SaaS; time crescendo; necessidade de controle de projetos; Claude Code disponivel |
| **Assessment** | "Posso construir isso com vibe coding em poucos dias" |
| **Options** | Continuar pagando ClickUp / Contratar dev time / Construir com Claude Code |
| **Decisao** | Construir com Claude Code via VS Code |
| **Rationale** | Velocidade (4-6h vs semanas de dev), custo zero de licenca, 100% adaptado a operacao |
| **Resultado** | Sistema funcional em 4h. Economizou >R$100k/ano em ferramentas e contratacoes. Hoje vendido como produto (HUP) |
| **What-ifs** | E se nao tivesse usado Plan Mode? -> Teria mais retrabalho. E se tivesse contratado dev? -> Meses de espera e custo alto |

---

## Caso 2 -- Ana: Agente Financeiro (DRE + DFC)

| Campo | Detalhe |
|---|---|
| **Situacao** | Criar agente financeiro que gera DRE e DFC integrado ao Conta Azul, ao vivo durante webinar |
| **Cues** | Precisa de funcionario digital para financeiro; tool disponivel e Conta Azul (tem API) |
| **Assessment** | "Vou criar o agente + skill + conexao com ferramenta numa so instrucao" |
| **Decisao** | Pediu ao Claude: agente "Ana", DRE+DFC, tool = Conta Azul. Claude propoe estrutura: agents/ana.md + skills/conta-azul/skill.md + scripts/ |
| **Rationale** | Claude perguntou: credenciais do Conta Azul, escopo da Ana, nivel de autonomia -- necessario para geracao correta dos scripts |
| **Resultado** | Claude gerou: ana.md, skill.md conta-azul, scripts de conexao com API |
| **Regra ilustrada** | Skill sem scripts = so texto; skill com scripts = execucao real |
| **What-ifs** | E se nao tivesse especificado a tool? -> Skill generica sem poder de execucao |

---

## Caso 3 -- Agente de WhatsApp

| Campo | Detalhe |
|---|---|
| **Situacao** | JP tem agente de WhatsApp em producao na Brave. Mais usado do dia a dia. |
| **Cues** | Precisa monitorar grupos, responder clientes, ver mensagens nao lidas, contextualizar por lead/cliente |
| **Assessment** | Agente precisa: saber com quem esta falando, historico, como falar com cada pessoa |
| **Decisao** | Criou arquivo em agents/ com: personalidade "assessor de comunicacao", skill whatsapp com 40+ comandos, regras de tom por tipo de contato |
| **Resultado** | 40+ comandos: triagem, envio de copy, gestao de grupos, status de conversa, etc. |
| **Regra ilustrada** | Agente = funcionario com personalidade + skill + memoria de contexto |
| **What-ifs** | E se fosse so skill.md sem regras de comunicacao? -> Responderia de forma generica |

---

## Caso 4 -- Agencia de Marketing: 12 agentes em 2 semanas

| Campo | Detalhe |
|---|---|
| **Situacao** | CEO de agencia de marketing entra no treinamento Dominando Claude Code |
| **Cues** | Time grande, custo alto, processos repetitivos de marketing e atendimento |
| **Decisao** | Montou 12 agentes em 2 semanas usando o metodo FPCN |
| **Resultado** | Cortou 3 salarios, economiza >R$8k/mes, mantem mesma operacao com menos pessoas |
| **Regra ilustrada** | 1 pessoa com Claude Code bem configurado = 10 pessoas; agentes sao funcionarios digitais 24/7 |

---

## Caso 5 -- Juliana: IA de triagem de curriculos (RH)

| Campo | Detalhe |
|---|---|
| **Situacao** | Consultora de RH no Rio. Sem conhecimento de programacao. |
| **Cues** | Precisa triar ~300 curriculos/dia; tarefa repetitiva e manual |
| **Decisao** | Construiu um agente/skill de triagem de curriculos com Claude Code |
| **Resultado** | IA tria 300 CVs/dia automaticamente. Operacao transformada sem escrever uma linha de codigo |
| **Regra ilustrada** | Nao precisa ser programador; vibe coding funciona para qualquer area profissional |

---

## Caso 6 -- Davi Braga: base de conhecimento para builds

| Campo | Detalhe |
|---|---|
| **Situacao** | Davi Braga quer construir sistema, pede a JP a base de conhecimento/boas praticas |
| **Assessment** | "Com base de conhecimento certa, iniciante entrega resultado melhor que expert sem ela" |
| **Decisao** | JP enviou arquivo de boas praticas e arquitetura antes de Davi comecar a construir |
| **Resultado** | Davi inicia sistema ja prevenindo erros comuns que um leigo sem orientacao cometeria |
| **Regra ilustrada** | Base de conhecimento = prevencao de retrabalho; quanto mais contexto o Claude tem, melhor a entrega |

---

## Caso 7 -- CRM com MCP

| Campo | Detalhe |
|---|---|
| **Situacao** | Brave precisava de CRM proprio, construido com Claude Code, operavel via terminal |
| **Decisao** | Construiu CRM + MCP (Model Context Protocol) para operacao via Claude Code |
| **Resultado** | Toda operacao do CRM e feita pelo terminal via comandos ao Claude |
| **Regra ilustrada** | MCP = skill avancada que conecta Claude Code a sistemas externos via protocolo padrao |

---

## Counterfactuals para Evals

1. **Se o usuario pular a fase Planejar** -> Claude vai executar algo sem contexto suficiente -> retrabalho alto
2. **Se criar agente sem skills** -> Agente e como "funcionario sem capacidade" -- so conversa, nao executa
3. **Se criar skill sem scripts** -> Skill sem poder de execucao -- so texto, nao faz nada real
4. **Se nao usar CLAUDE.md** -> Claude nao conhece o contexto do negocio -> respostas genericas
5. **Se nao guardar na memory.md** -> Erros se repetem, Claude "esquece" regras importantes

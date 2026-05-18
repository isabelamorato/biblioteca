---
name: pesquisa
description: "Pesquisa profunda em funil multi-nível com fontes verificadas. Use SEMPRE que o usuário pedir para comparar opções com dados reais (X vs Y, framework A vs B, produto/carro/plano), decidir entre alternativas com stakes (migração de stack, escolha de fornecedor, mudança de plataforma), validar afirmações contra fontes (segunda opinião médica, estudos científicos, benchmarks), fazer análise de mercado/competitiva, deep dive em estado da arte de um domínio, ou pesquisar impacto de mudanças (regulação, reforma, tendência). Dispare também quando o pedido envolver TCO, benchmarks reais, gotchas, comparativos com dados concretos, ou qualquer pesquisa que valha a pena gastar 60-90s para obter resposta defensável com citações. CASO MÉDICO/FARMACOLÓGICO: dispare SEMPRE que o usuário quiser pesquisar literatura sobre medicamentos, sintomas, interações ou diagnóstico — INCLUSIVE quando ele já consultou profissional e quer fontes adicionais para validar/discutir (ex: 'validar o que o médico disse', 'pesquisar interações reportadas em estudos', 'sintomas após começar X medicação'). O pedido é por PESQUISA, não por triagem clínica. NÃO use para: debugar erro de código, operações de arquivo (renomear, abrir .env), responder email, instalar pacote, pergunta factual rápida ('qual a fórmula de X'), how-to de instalação, ou referência a invocação passada. Comando: /pesquisa [tema], com flags opcionais -f (funil automático sem paradas) e -a (modo anônimo, não salva relatório)."
---

# Pesquisa em Funil v3

Evolução do `/pesquisa` (v2) com 3 técnicas roubadas de skills do marketplace:

| Técnica | Origem | O que muda |
|---------|--------|------------|
| CRAAP scoring | claim-investigation | Score 0-100 por critério, não só tier |
| Phase Gate por fatos-chave | claim-investigation | ≥2 fontes independentes por fato central |
| Domain filters | Tavily pattern | Queries restritas a domínios confiáveis |

## O Funil v3

```
Nível 1: Varredura (perplexity_search paralelo)
    | Apresentar → usuário aprova direção (HITL)
    v
Nível 2: Análise (perplexity_reason) + identificar fatos-chave + sub-tópicos
    | Apresentar + listar sub-tópicos + fatos-chave → usuário escolhe (HITL)
    v
Nível 3: Deep Dive PARALELO (N x perplexity_research + firecrawl)
    | Phase Gate v3: sub-perguntas respondidas? + fatos-chave em >=2 fontes? + CRAAP?
    | Se não → gap filling focado
    v
Relatório final → salvo como ~/pesquisas/[tema]-[data].md
```

**Regra inviolavel:** human-in-the-loop entre cada nível. Não pular sem aprovação.

## v3.1 — defesa em profundidade pos-incidente 2026-04-29

Esta skill foi auditada apos dogfood que revelou `/pesquisa` rodando "internamente" (modelo se autovigia), gerando relatorios com secoes obrigatorias ausentes e CRAAP inflacionado. Mudancas:

- **Phase Gate via subagent independente** (Passo 5): nao e mais `executar internamente`, e `Agent({subagent_type: Explore, ...})` produzindo `verification_report.json`
- **CRAAP rubric calibrada** com 3 exemplos por Tier (Passo 4) -- sem isso, scores convergem pra 88-95
- **Definicao programatica de "fonte independente"**: dominios distintos + nao-duplicacao de paper primario
- **PostToolUse hook validador** em `~/.claude/skills/pesquisa/scripts/validate-report.py` -- bloqueia Write em `~/pesquisas/*.md` se relatorio nao tiver todas secoes obrigatorias OU se >50% fatos tem <2 fontes

## Preparacao -- carregar `AskUserQuestion`

O skill usa `AskUserQuestion` nos HITLs dos Niveis 1 e 2. Essa tool e **deferred** na harness atual -- o schema nao e carregado por padrao. **Antes** de rodar qualquer query do Nivel 1, executar:

```
ToolSearch({ query: "select:AskUserQuestion", max_results: 1 })
```

Sem esse passo a tool nao e invocavel e o HITL falha silenciosamente. Pode rodar em paralelo com as queries do Nivel 1 (nao bloqueia).

## Flags

### `-f` (full) -- funil automatico

Se o usuario passar `-f`, rodar o funil completo (1->2->3) sem parar para perguntar entre os niveis. O unico HITL mantido e a escolha de sub-topicos antes do Nivel 3.

### `-a` (anonymous) -- nao salva em disco

Se o usuario passar `-a`, **pular o passo de salvar o relatorio** em `~/pesquisas/`. O relatorio e apresentado normalmente na conversa, mas nao persiste como arquivo `.md`.

Ao detectar a flag, avisar logo no inicio (antes do Nivel 1):

```
Modo anonimo: relatorio nao sera salvo em ~/pesquisas/.
   Nota: queries ainda aparecem no historico da sua conta Perplexity.
```

---

## Nivel 1 -- Varredura

**Ferramenta:** `perplexity_search`
**Velocidade:** ~5 segundos por query
**Objetivo:** Mapear o terreno com 3-5 angulos paralelos.

### Como executar

1. Decompor o tema em 3-5 angulos complementares
2. Rodar TODAS em paralelo no mesmo turno
3. Usar `sources` estrategicamente: `web`, `scholar`, `social`

### Entrega do Nivel 1

```
Varredura: [tema]

Pesquisei [N] angulos:

1. [Rotulo curto] -- [achado em 1 frase, ~15 palavras max]
2. [Rotulo curto] -- [achado em 1 frase]
3. [Rotulo curto] -- [achado em 1 frase]

Padroes: [1-2 frases curtas]

Gaps: [o que ainda nao sei]
```

Depois chamar AskUserQuestion com opcoes: "Nivel 2 (Recommended)", "Ajustar foco", "Nivel 1 basta".

**Nao prosseguir sem resposta do usuario.**

---

## Nivel 2 -- Analise + Fatos-Chave

**Ferramenta:** `perplexity_reason`
**Velocidade:** ~15 segundos

**Diferenca v3:** Alem de comparar e identificar sub-topicos, identificar explicitamente **3-5 fatos-chave** -- afirmacoes factuais centrais para a conclusao que precisarao ser verificadas por >=2 fontes independentes no Phase Gate.

### Entrega do Nivel 2

```
Analise: [tema]

Comparativo:
| Criterio | Opcao A | Opcao B | Opcao C |
|----------|---------|---------|---------- |
...

Recomendacao preliminar: [opcao] porque [razao]

Fatos-chave a verificar no Nivel 3:
- [ ] [Fato 1] -- precisa de >=2 fontes independentes
- [ ] [Fato 2] -- precisa de >=2 fontes independentes
```

Depois chamar AskUserQuestion sobre quais sub-topicos quer no deep dive paralelo.

**Nao prosseguir sem resposta.**

---

## Nivel 3 -- Deep Dive Paralelo com Domain Filters

**Ferramentas:** N x `perplexity_research` em paralelo + `firecrawl_scrape`

### Passo 1 -- Inferir domain filters (opcional)

| Tipo de tema | Domain hints |
|--------------|---------------------------|
| Tecnologia/frameworks | `site:github.com OR site:arxiv.org` |
| Mercado/business | `site:statista.com` |
| Saude/medicina | `site:pubmed.ncbi.nlm.nih.gov OR site:who.int` |
| Regulacao/legal | `site:gov.br` |
| Geral | Nao filtrar |

### Passo 2 -- Disparar em paralelo

Para cada sub-topico aprovado, criar uma query especifica. Disparar TODAS no mesmo turno.

### Passo 3 -- Scraping de URLs identificadas

Apos receber resultados, identificar 2-3 URLs de maior valor e raspar. Ordem de fallback:

1. `firecrawl_scrape(url)`
2. Bash: `npx -y @teng-lin/agent-fetch "<url>" --json`
3. Bash: `curl -s "https://r.jina.ai/<url>"`
4. `WebFetch(url)` -- ultimo recurso: resume/parafraseeia, nao extrai
5. Pular a URL, anotar como indisponivel

### Passo 4 -- CRAAP Scoring

| Criterio | O que avaliar | Score |
|----------|--------------|-------|
| **C**urrency | Data de publicacao/atualizacao | 0-20 |
| **R**elevance | Fit direto com a pergunta? | 0-20 |
| **A**uthority | Quem publicou? Credenciais? | 0-20 |
| **A**ccuracy | Corroborada por outras fontes? | 0-20 |
| **P**urpose | Informar, vender, persuadir? | 0-20 |

**Bandas de confianca:**
- 80-100: Tier A
- 60-79: Tier B
- 40-59: Tier C
- <40: Tier D

**Exemplos calibrados:**

- Tier A (92): paper ICLR peer-reviewed
- Tier B (72): community blog post de autor identificado
- Tier C (52): LinkedIn pulse post

**Definicao programatica de "fonte independente":** dominios distintos + nao-duplicacao de paper primario.

### Passo 5 -- Phase Gate v3.1 (External Verifier)

Phase Gate NÃO e mais executado "internamente". E delegado a um **subagent verifier independente** via `Agent({subagent_type: "Explore", ...})`.

O verifier produz `verification_report.json` com: checklist (C1-C5), weak_facts[], craap_inflation_warning, verdict (pass|fail), required_fixes.

- Se **verdict: pass**: prosseguir pra relatorio final
- Se **verdict: fail**: aplicar fixes e re-rodar gate
- Se subagent indisponivel: usar checklist manual, MAS rebaixar Confianca final 1 nivel

---

## Entrega do Nivel 3

```
Relatorio: [tema]
Gerado em: [data] | Sub-topicos: [N] | Fontes avaliadas: [N] | Fatos-chave verificados: [N/total]

## Resumo Executivo
[2-3 frases com conclusao principal e nivel de confianca explicito]

## [Sub-topico A]
[Achados com dados concretos]
Fatos verificados: [lista com status >=2 fontes ou "fonte unica"]
Fontes principais: [CRAAP score >=60 com URLs]

## [Sub-topico B]
...

## Comparativo Final
| Criterio | Opcao A | Opcao B |
|----------|---------|----------|

## Recomendacao
[Opcao recomendada + justificativa + nivel de confianca: ALTO/MEDIO/BAIXO]

## Contradicoes Identificadas
[Pontos onde fontes divergem]

## Status dos Fatos-Chave
| Fato | Fontes | Verificado? |
|------|--------|-------------|
| [fato 1] | [fonte A] + [fonte B] | confirmado |
| [fato 2] | [fonte A] apenas | fonte unica |

## Fontes Avaliadas (CRAAP)
**Tier A (80-100):**
- [fonte -- score -- URL -- data]
...
```

---

## Salvar como arquivo

**Se a flag `-a` foi passada:** pular este passo. **Caso contrario (default):** salvar em `~/pesquisas/pesquisa-[tema]-[data].md` usando Write tool.

---

## Ferramentas

| Ferramenta | Quando usar |
|-----------|-------------|
| `perplexity_search` | Nivel 1, gap filling analitico |
| `perplexity_ask` | Phase Gate: gaps factuais com resposta unica |
| `perplexity_reason` | Nivel 2, analise/comparacao/trade-offs |
| `perplexity_research` | Nivel 3, por sub-topico (paralelo) |
| `firecrawl_scrape` | Nivel 3, URLs especificas |
| `Write` | Salvar relatorio final como .md |

---

## Fallback: tokens expirados

Se `perplexity_search` falhar com erro de autenticacao:

1. Abrir perplexity.ai no browser (logado)
2. Usar extensao Perplexity Keys (Chrome) para copiar os 2 tokens
3. Atualizar tokens no arquivo de configuracao do MCP
4. Sair e entrar de novo no Claude Code

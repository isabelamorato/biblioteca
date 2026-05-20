# Biblioteca — Skills & Plugins do Claude Code

Repositório pessoal com todas as skills e plugins instalados no Claude Code.

---

## Como usar uma skill

No Claude Code, basta digitar `/nome-da-skill` no chat. Exemplo: `/pesquisa inteligência artificial`.

---

## Skills

### Hospedadas neste repositório

| Skill | O que faz |
|---|---|
| [arquiteto-academico](skills/arquiteto-academico/SKILL.md) | Gera cursos completos prontos para gravação: blueprint estratégico, roteiros para teleprompter e materiais de apoio em PDF. Opera como 3 entidades cognitivas (Arquiteto, Roteirista, Revisor). |
| [auditoria-de-sites](skills/auditoria-de-sites/SKILL.md) | Pipeline completo: audita um site gerando score 0–100 em Design, SEO, GEO e Copy → constrói site novo otimizado → faz deploy no Cloudflare Pages com URL pública. |
| [brainstorming](skills/brainstorming/SKILL.md) | Obrigatório antes de qualquer trabalho criativo ou novo feature. Explora intenção, requisitos e design em diálogo colaborativo antes de escrever qualquer código. |
| [copywriting](skills/copywriting/SKILL.md) | Escreve ou melhora copy de marketing para páginas web (home, landing page, pricing, sobre). Foco em conversão: headlines, CTAs, proposta de valor. |
| [curso2skill](skills/curso2skill/SKILL.md) | Transforma um curso já extraído em uma skill operacional do Claude, codificando o julgamento do instrutor (não só o conteúdo) via Análise Cognitiva de Tarefas. |
| [curso-dominandoclaudecode](skills/curso-dominandoclaudecode/SKILL.md) | Guia completo para instalar, configurar e dominar o Claude Code: CLAUDE.md, memory, skills, agentes, automações e vibe coding — método JP / Brave School. |
| [etl-audio](skills/etl-audio/SKILL.md) | Transcreve áudio ou vídeo com separação de speakers (diarization) via Mistral Voxtral. Suporta reuniões, calls, podcasts, voice notes do WhatsApp, Zoom. Output JSON estruturado. |
| [etl-ocr](skills/etl-ocr/SKILL.md) | Extrai texto de imagens e PDFs via OCR (Mistral OCR). Suporta documentos escaneados, notas fiscais, contratos, recibos, manuscritos. Output markdown por página. |
| [extrair-curso](skills/extrair-curso/SKILL.md) | Baixa curso online (vídeo, MP3 e transcrição com timestamps) de plataformas como Hotmart, Kiwify, Teachable, Memberkit etc., usando o próprio browser autenticado do usuário. |
| [find-skills](skills/find-skills/SKILL.md) | Ajuda a descobrir e instalar novas skills do ecossistema de agentes quando você pergunta "tem uma skill que faz X?" ou quer expandir as capacidades do Claude. |
| [frontend-design](skills/frontend-design/SKILL.md) | Cria interfaces frontend de produção com alta qualidade visual — componentes, páginas, dashboards, landing pages. Evita o estético genérico de IA, gera design memorável. |
| [pesquisa](skills/pesquisa/SKILL.md) | Pesquisa profunda em funil multi-nível com fontes verificadas. Ideal para comparar opções, validar afirmações, análise de mercado, TCO, benchmarks e literatura médica/científica. |
| [pesquisa-profunda](skills/pesquisa-profunda/SKILL.md) | Levantamento completo de cliente para gestores de tráfego: briefing, análise de mercado, concorrentes e estratégia antes de iniciar campanhas de tráfego pago. |
| [planejar](skills/planejar/SKILL.md) | Metodologia em 8 fases para planejar produtos digitais (web app, SaaS, API, mobile) antes de escrever código — do brainstorm ao plano de implementação auditado. |
| [polish](skills/polish/SKILL.md) | Faz um passe final de qualidade antes de entregar: alinhamento, espaçamento, consistência e micro-detalhes que separam um trabalho bom de um trabalho excelente. |
| [resumo-whatsapp](skills/resumo-whatsapp/SKILL.md) | Resume conversas exportadas de grupos do WhatsApp destacando decisões tomadas, pendências e temas em debate. Ideal para quando você perdeu mensagens ou voltou de férias. |
| [site2skill](skills/site2skill/SKILL.md) | Gera automaticamente uma skill cliente de API para qualquer site. Você exporta um HAR do Chrome, ela detecta o modo correto (simples com curl+cookies, ou CDP com Chrome real para sites com Cloudflare/CSRF) e cria a skill pronta para uso. |
| [social-content](skills/social-content/SKILL.md) | Cria e otimiza conteúdo para redes sociais: LinkedIn, Twitter/X, Instagram, TikTok. Posts, threads, carrosséis, calendário de conteúdo e estratégias de engajamento. |
| [supabase-postgres-best-practices](skills/supabase-postgres-best-practices/SKILL.md) | Guia completo de otimização de performance no Postgres (Supabase). Cobre queries, schema, conexões, índices, locks, segurança (RLS) e monitoramento — 8 categorias de regras. |

### Skills externas instaladas via `npx skills add`

| Skill | Fonte | O que faz |
|---|---|---|
| [tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) | [mattpocock/skills](https://github.com/mattpocock/skills) | TDD com loop red-green-refactor. Abordagem vertical (tracer bullet): um teste → uma implementação por ciclo. Testa comportamento via interfaces públicas, não detalhes de implementação. |

---

## Plugins

### Hospedados neste repositório

| Plugin | O que é |
|---|---|
| [superpowers](plugins/superpowers/) | Conjunto de skills de processo: brainstorming, TDD, debugging, planejamento, code review, worktrees e mais. Base do workflow de desenvolvimento. |
| [frontend-design](plugins/frontend-design/) | Plugin de design frontend de alta qualidade para criar interfaces de produção. |
| [code-review](plugins/code-review/) | Revisão automatizada de pull requests com feedback estruturado. |
| [code-simplifier](plugins/code-simplifier/) | Simplifica e refina código recém-modificado para clareza e manutenibilidade. |
| [github](plugins/github/) | Integração com GitHub: issues, PRs, branches e repositórios direto do Claude. |
| [playwright](plugins/playwright/) | Automação de browser para testes e scraping via Playwright. |
| [claude-md-management](plugins/claude-md-management/) | Audita e melhora arquivos CLAUDE.md em repositórios. |
| [claude-code-setup](plugins/claude-code-setup/) | Analisa um codebase e recomenda automações para o Claude Code (hooks, subagentes, skills). |
| [security-guidance](plugins/security-guidance/) | Orientações de segurança para código e infraestrutura. |
| [warp](plugins/warp/) | Integração com o terminal Warp — notificações e hooks de sessão. |
| [knowledge-work-plugins](plugins/knowledge-work-plugins/) | Skills para trabalho financeiro e contábil: reconciliação GL×subrazão, conciliação bancária, reconciliação intercompany, categorização de itens e análise de aging. |

### Marketplace externo — [thaleslaray/plugins](https://github.com/thaleslaray/plugins)

| Plugin | O que é |
|---|---|
| [rh](https://github.com/thaleslaray/plugins/tree/main/plugins/rh) | RH automatizado scorecard-first. Pipeline de contratação com `/rh:contratar`: infere scorecard, descobre candidatos via GitHub e registries, curadoria item-a-item. |
| [pesquisa](https://github.com/thaleslaray/plugins/tree/main/plugins/pesquisa) | Pesquisa profunda em funil multi-nível — versão evoluída com nível 3 paralelo por sub-tópico e reflection gate antes de fechar o relatório. |
| [hotmart](https://github.com/thaleslaray/plugins/tree/main/plugins/hotmart) | MCP server da API Hotmart — vendas, assinaturas, club, produtos, cupons, tickets e negociação. Auto-gerado do OpenAPI oficial. |
| [clint](https://github.com/thaleslaray/plugins/tree/main/plugins/clint) | MCP server do CRM Clint (brasileiro) — 46 endpoints em 14 categorias: contatos, deals, tags, chats, mensagens WhatsApp, dashboards e mais. |

---

## Estrutura do repositório

```
biblioteca/
├── skills/          # Skills customizadas instaladas no Claude
└── plugins/         # Plugins hospedados neste repositório
```

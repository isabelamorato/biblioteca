---
name: auditoria-de-sites
description: >
  Pipeline completo em 3 fases: (1) Audita sites institucionais gerando score 0–100 em Design, SEO, GEO e Copy, (2) Constrói um site novo bonito e otimizado baseado nos problemas encontrados, (3) Faz deploy no Cloudflare Pages com URL pública em minutos. Use SEMPRE que o usuário mencionar: analisar site, auditar site, site ruim, site de dentista, site médico, site institucional, quero refazer site, construir site, criar landing page, hospedar site, deploy cloudflare, cloudflare pages, site novo para cliente, prospecção de clientes com site ruim, diagnóstico digital, "meu site está bom?", "faz um site pra mim", ou qualquer combinação de análise + criação + hospedagem de site.
---

# Auditoria → Construção → Deploy de Sites

Você é um consultor digital completo. O fluxo tem 3 fases, mas o usuário pode entrar em qualquer ponto:

- **Só a auditoria?** Execute a Fase 1 e pare.  
- **Auditar e criar o site?** Fases 1 + 2.  
- **O pacote completo?** Fases 1 + 2 + 3.  
- **Só criar/hospedar?** Fases 2 + 3.

Se não ficou claro o que o usuário quer, pergunte antes de começar.

---

## FASE 1 — AUDITORIA (Score 0–100)

O objetivo é **quantificar o problema** de forma específica e vendável. Se o site for ruim, o relatório deve deixar óbvio o que está sendo perdido — e abrir a conversa para um site novo.

### Coleta de dados (execute em paralelo)

**A) Fetch das páginas principais:**
- Homepage + página de serviços + contato (quando existirem)
- Extraia: title tag, meta description, H1/H2/H3, CTAs, copy completo, schema markup (`application/ld+json`), meta viewport, Open Graph, scripts externos, telefone/WhatsApp visíveis, depoimentos, FAQs

**B) Pesquisa de apoio (WebSearch):**
- Reputação: `"[empresa] avaliações google"` → nota, volume de reviews
- Concorrente: `"[segmento] [cidade] site"` → pega o 1º resultado orgânico que seja site de concorrente
- Palavras-chave: `"[segmento] [cidade]"` → que termos o público busca?

**C) Verificações técnicas no HTML:**
`<meta viewport>`, `<title>`, `<meta description>`, `<h1>`, HTTPS, JSON-LD schema, Open Graph, canonical tag, robots meta, sitemap link, imagens com alt text

**D) Teste de Primeira Impressão (2 segundos):**
- O que primeiro chama a atenção? É o correto?
- Em 5 segundos: dá para entender o que a empresa faz, para quem e por que escolher?
- O fluxo de leitura (olho do usuário) está guiando para o CTA?

**Fallback se o site não carregar:** Use WebSearch. Aplique –5 pts no Design. Indique o que foi estimado vs. verificado.

---

### Rubrica de pontuação

Cada dimensão vale **25 pontos** (total: 100). Avalie com rigor — 20+ pontos deve ser mérito real.

#### 🎨 Design (0–25)

| Critério | Pts | Como avaliar |
|----------|-----|------------------|
| **Modernidade visual** — sem layout de tabela, fontes datadas, cores de 2010 | 5 | Fontes são web modernas? Grid CSS ou Flexbox? |
| **Mobile responsivo** — viewport + layout adaptável, touch targets ≥ 44×44px | 5 | Redimensione para 375px. Quebra? Botões são clicáveis no polegar? |
| **Hierarquia visual clara** — H1 evidente, CTA destacado, usuário sabe o que fazer em 5s | 5 | Qual elemento chama mais atenção? Deveria ser o CTA ou o H1 |
| **Performance / Acessibilidade** — contraste WCAG AA (4.5:1), sem scripts pesados desnecessários | 5 | Cores primárias têm contraste suficiente em fundo branco/claro? |
| **Credibilidade visual** — fotos reais (não stock genérico), logo profissional, paleta coerente | 5 | Parece uma empresa real ou template de 2008? |

**Penalidades de design (deduz pontos):**
- Layout quebrado no mobile: –5
- Nenhum CTA visível acima da dobra: –3
- Contraste insuficiente em texto principal (< 4.5:1): –3
- Fonte genérica como única escolha (Arial, Times, Courier): –2

#### 🔍 SEO (0–25)

| Critério | Pts | Como avaliar |
|----------|-----|------------------|
| **Title tag** — presente, 50-60 chars, inclui keyword + localidade | 5 | Ausente = 0. Presente mas sem keyword = 2. Otimizado = 5. |
| **Meta description** — presente, 150-160 chars, inclui call to action implícito | 4 | Ausente = 0. Presente = 2. Com CTA e keyword = 4. |
| **H1** — existe, é único, inclui keyword principal do negócio | 4 | Mais de um H1 = –2. Ausente = 0. Presente e keyword = 4. |
| **Estrutura H2/H3** — hierarquia lógica, cobre temas de busca do setor | 4 | Sem estrutura = 0. Estrutura lógica com keywords = 4. |
| **Conteúdo indexável** — texto real no HTML (não só em imagens), keywords naturalmente presentes | 4 | Texto mínimo ou todo em imagem = 0. Rico e indexável = 4. |
| **Infraestrutura técnica** — HTTPS, URLs limpas, sem parâmetros excessivos, canonical presente | 4 | HTTP = –2. URLs com `?id=123` = –1. Limpo = 4. |

**Checks técnicos extras (não pontuam, mas aparecem no relatório):**
- Core Web Vitals: LCP, CLS, INP — sinalizar se há scripts render-blocking
- Robots.txt configurado corretamente?
- Sitemap XML presente?
- Imagens sem compressão excessiva?

#### 🤖 GEO — Generative Engine Optimization (0–25)

*(Quando alguém pergunta ao ChatGPT/Perplexity: "melhor dentista em [cidade]?", esse site aparece?)*

| Critério | Pts | Como avaliar |
|----------|-----|------------------|
| **Schema markup** — JSON-LD LocalBusiness/MedicalBusiness com nome, endereço, telefone, horário, especialidade | 6 | Ausente = 0. Básico sem campos = 2. Completo = 6. |
| **NAP consistente** — Nome, Endereço, Telefone visíveis no HTML e coerentes com Google Business | 5 | Inconsistente = 1. Visível e correto = 5. |
| **FAQ estruturado** — seção de perguntas reais do setor + schema FAQPage | 5 | Sem FAQ = 0. FAQ sem schema = 2. Com FAQPage schema = 5. |
| **Entidade inequívoca** — quem é, o que faz, onde fica, como contatar (claro para uma IA ler) | 5 | Confuso = 0. Claro e completo = 5. |
| **Reputação citável** — depoimentos nomeados, certificações, número de pacientes, anos de experiência | 4 | Nenhum = 0. Genérico = 2. Específico e verificável = 4. |

**Técnicas GEO avançadas (Princeton Research — adicionam pontos bonus):**
- Cita fontes autoritativas (CFM, CRO, publicações científicas): +2 pts potenciais
- Usa estatísticas específicas ("92% dos pacientes" vs "muitos pacientes"): +1
- Inclui citações de profissionais nomeados: +1
- Estrutura de autoridade clara (quem é o médico, CRM, titulação): +1

#### ✍️ Copy (0–25)

| Critério | Pts | Como avaliar |
|----------|-----|------------------|
| **Proposta de valor** — em 5s: o quê, para quem, por quê escolher. Orientada a benefício, não só nome | 6 | "Bem-vindo à Clínica X" = 0. "Sorriso que transforma em [cidade]" = 3. Específico + diferenciador = 6. |
| **Headline** — orientada a resultado/benefício, usa fórmula testada, inclui keyword | 5 | Nome da empresa como H1 = 0. Benefício claro = 3. Fórmula + keyword + localidade = 5. |
| **CTAs** — WhatsApp/"Agende"/"Marque agora", visíveis acima da dobra, texto de ação com verbo | 5 | Sem CTA = 0. CTA genérico = 2. Múltiplos CTAs diretos com verbo = 5. |
| **Prova social** — depoimentos reais e nomeados, números específicos, certificações, anos | 5 | Ausente = 0. Genérico = 2. Específico + nomeado + verificável = 5. |
| **Clareza e scanneabilidade** — parágrafos curtos, bullets, textos não densos, fácil de escanear | 4 | Muro de texto = 0. Escaneável e estruturado = 4. |

**Análise narrativa do copy (Villain/Hero/Transformation/Stakes):**
Identifique se o copy responde:
- **Vilão** (problema que o cliente enfrenta): "Sente dor ao sorrir?", "Dentes manchados te travam?"
- **Herói** (quem resolve): o paciente é o herói, a clínica é o guia
- **Transformação** (antes/depois): resultado claro e específico
- **Stakes** (o que acontece sem agir): sem urgência = sem conversão

---

### Análise de Concorrência

Para o concorrente encontrado na pesquisa, compare:

| Dimensão | Site Auditado | Concorrente | Vantagem |
|----------|--------------|-------------|----------|
| Tagline / Headline | | | |
| Proposta de valor | | | |
| CTAs principais | | | |
| Prova social | | | |
| SEO on-page (title+H1) | | | |
| Schema/GEO | | | |
| Design visual | | | |
| Score estimado | /100 | /100 | |

---

### Tabela de Problemas por Severidade

Para cada problema encontrado, classifique:

| Problema | Dimensão | Severidade | Impacto | Correção |
|----------|----------|------------|---------|----------|
| [ex: Sem title tag] | SEO | 🔴 Crítico | Não aparece nas buscas | Adicionar title com keyword + cidade |
| [ex: Layout quebrado mobile] | Design | 🔴 Crítico | 60%+ do tráfego perdido | Adicionar viewport + CSS responsivo |
| [ex: Sem FAQ] | GEO | 🟡 Importante | Invisível para IA | Adicionar 5+ perguntas com FAQPage schema |
| [ex: CTA genérico "Saiba mais"] | Copy | 🟡 Importante | Baixa conversão | Trocar por "Agendar pelo WhatsApp" |
| [ex: Fonte Arial] | Design | 🟢 Melhoria | Parece datado | Trocar por Google Font com caráter |

Severidade: 🔴 Crítico (prejudica diretamente conversões/rankings) | 🟡 Importante (oportunidade significativa perdida) | 🟢 Melhoria (diferença de percepção)

---

### Formato do relatório

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  AUDITORIA DIGITAL — [NOME DA EMPRESA]
  [URL]  |  Analisado em: [DATA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  PONTUAÇÃO GERAL: [SCORE]/100  [EMOJI_VEREDITO]

  🎨 Design      [X]/25   [██████░░░░]
  🔍 SEO         [X]/25   [████░░░░░░]
  🤖 GEO         [X]/25   [███░░░░░░░]
  ✍️  Copy        [X]/25   [██████░░░░]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Para cada dimensão, apresente:
- **✅ O que funciona** (com exemplos reais do site — cite o texto exato)
- **❌ Problemas encontrados** (cite o elemento real: "o title tag diz '...' mas deveria...")
- **💡 Para atingir 25/25** (ações concretas e específicas)

**Plano de Ação — separado em 2 horizontes:**

**⚡ Quick Wins (esta semana, < 2h cada):**
- Ações de alto impacto, baixo esforço
- Ex: corrigir title tag, adicionar meta description, corrigir H1, adicionar schema básico

**🏗️ Investimentos Estratégicos (este mês):**
- Ações de impacto alto mas que exigem mais trabalho
- Ex: refazer estrutura do site, criar seção FAQ completa, produzir depoimentos reais

**Resumo Executivo:**
- Diagnóstico direto em 2-3 frases
- "O que este site está custando": clientes perdidos, invisibilidade em IA, credibilidade prejudicada
- Recomendação objetiva: otimizar vs. refazer

| Score | Veredito |
|-------|----------|
| 0–29  | 🔴 CRÍTICO — prejudica ativamente o negócio |
| 30–49 | 🟠 URGENTE — oportunidades sérias sendo perdidas |
| 50–69 | 🟡 REGULAR — funcional, longe do potencial |
| 70–84 | 🟢 BOM — base sólida, otimizações fariam diferença |
| 85+   | ⭐ EXCELENTE — referência no segmento |

**Após o relatório**, sempre pergunte:
> "Quer que eu construa uma versão nova do site baseada nesses problemas? Posso gerar o HTML completo agora e hospedar no Cloudflare Pages pra você ter uma URL pública em minutos."

---

## FASE 2 — CONSTRUÇÃO DO SITE

Antes de começar, leia **`references/design-web.md`** e **`references/copy-frameworks.md`** para os princípios que devem guiar a criação.

### O que construir

Crie um arquivo `index.html` completo, autocontido (CSS e JS embutidos), que resolva todos os problemas encontrados na auditoria.

#### 1. SEO técnico obrigatório
- Title tag: 50-60 chars, formato `[Especialidade] em [Cidade] | [Nome]`
- Meta description: 150-160 chars, inclui keyword, benefício e CTA implícito
- H1 único, orientado a benefício (ver `references/copy-frameworks.md` para fórmulas)
- Estrutura H2/H3 cobrindo: serviços, diferenciais, FAQ, contato
- Canonical tag apontando para si mesmo
- Open Graph tags (title, description, image)

#### 2. GEO — estrutura para ser citado por IA
- JSON-LD com schema correto (ver `references/design-web.md` para templates)
- Campos obrigatórios: name, description, url, telephone, address, openingHours, priceRange, sameAs
- Schema FAQPage com mínimo 5 perguntas reais do setor
- NAP visível em texto corrido (não só no rodapé)
- Seção "Sobre" com dados verificáveis: CRM/CRO, formação, anos de experiência
- Citação de pelo menos 1 fonte autoritativa (CFM, SBD, etc.)

#### 3. Design de alta qualidade (ver `references/design-web.md`)
- Google Fonts não genéricas (Playfair + Lato, Nunito + Open Sans, etc.) — nunca Inter sozinho
- Paleta de cores coesa: máximo 3 cores + neutros, contraste WCAG AA (4.5:1)
- Touch targets ≥ 44×44px em todos os elementos clicáveis
- Mobile-first, layout responsivo, sem grid 3 colunas genérico
- Micro-animações sutis (fade-in ao scroll, hover nos cards)
- Botão WhatsApp fixo no mobile

#### 4. Copy que converte (ver `references/copy-frameworks.md`)
- Hero section: headline com fórmula testada + subheadline com contexto + CTA primário
- Proposta de valor clara: o quê + para quem + por quê escolher aqui
- Seção de serviços: benefícios (não lista de procedimentos)
- Prova social: depoimentos nomeados + números específicos + certificações
- FAQ: 5+ perguntas reais que pacientes fazem
- Copy dos CTAs: verbos de ação ("Agendar agora", "Falar pelo WhatsApp") — nunca "Saiba mais" ou "Clique aqui"

### Estrutura de seções (ordem recomendada)

```
[HEAD: meta tags, schema JSON-LD, Google Fonts]
├── NAV: logo + CTA de agendamento no mobile
├── HERO: headline + subheadline + CTA primário + prova rápida (ex: "4.9 ⭐ 500+ pacientes")
├── SOBRE: quem é, credenciais, humanização
├── SERVIÇOS: 3-6 serviços com benefício, não só nome
├── DIFERENCIAIS: por que escolher (3-4 pontos com ícone)
├── PROVA SOCIAL: depoimentos nomeados + números em destaque
├── FAQ: 5+ perguntas + schema FAQPage
├── CONTATO: WhatsApp prominente + endereço + horário + mapa embed
└── FOOTER: NAP completo + links redes sociais + direitos
[WHATSAPP FIXO: botão flutuante no mobile]
```

### Placeholders quando não tiver dados reais

Se informações específicas não foram fornecidas:
- Use comentários HTML: `<!-- INSERIR: foto da clínica -->`
- Explique ao usuário o que precisa preencher
- Gere o design com CSS puro (gradientes, formas SVG, cores da paleta) sem imagens externas

### Entrega da Fase 2

Salve o arquivo em `site-output/index.html` no workspace e mostre ao usuário. Depois pergunte:
> "Site pronto! Quer que eu faça o deploy no Cloudflare Pages agora? Você vai ter uma URL pública tipo `seu-negocio.pages.dev` em menos de 2 minutos."

---

## FASE 3 — DEPLOY NO CLOUDFLARE PAGES

Leia **`references/cloudflare-deploy.md`** para o processo detalhado.

### Resumo do fluxo

1. **Verificar pré-requisitos** (Node.js, wrangler instalado, conta Cloudflare)
2. **Configurar credenciais** (`wrangler login` ou API token)
3. **Criar projeto** (primeira vez) ou usar projeto existente
4. **Deploy** com `wrangler pages deploy ./site-output`
5. **Retornar URL pública** ao usuário — `https://[projeto].pages.dev`

Se o cliente tiver domínio próprio, mostre como configurar o CNAME no DNS.

---

## Contexto: Segmento Médico/Dentista

Atenção especial para clínicas e consultórios:

**Schema:** Use `Dentist`, `MedicalOrganization`, `Physician` com `medicalSpecialty`

**Restrições legais de copy (CFM/CRO):**
- Proibido: "melhor", "garantido", "o mais completo", superlativos sem respaldo
- Permitido: conforto, tecnologia, equipe, experiência, humanização, localidade
- Foco em: processo, cuidado, resultado esperado (não garantido)

**GEO para saúde:** Inclua se aceita planos de saúde — campo altamente relevante nas buscas por IA

**Design:** Fotos reais da clínica > stock photos de sorrisos perfeitos genéricos

**CTA:** WhatsApp é o canal preferido no Brasil — deve estar visível no mobile acima da dobra, com texto de pré-mensagem:
```
https://wa.me/55[número]?text=Olá!%20Vim%20pelo%20site%20e%20gostaria%20de%20agendar%20uma%20consulta.
```

**Palavras-chave locais de alta intenção:**
- `dentista em [cidade]` / `dentista perto de mim`
- `clareamento dental [cidade]` / `implante dentário [cidade]`
- `dentista que aceita [plano]`
- `clínica odontológica [bairro]`

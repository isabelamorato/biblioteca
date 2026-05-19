---
name: pesquisa-profunda
description: Use when a traffic manager needs to do a complete client onboarding research before starting paid traffic campaigns. Always trigger this skill when the user mentions "levantamento do cliente", "onboarding cliente", "novo cliente tráfego", "briefing cliente", "análise de mercado cliente", "pesquisar concorrentes do cliente", or any variation of starting research for a new advertising client. Use even if the user just says "vou começar com um cliente novo" or "preciso pesquisar o mercado do cliente".
---

# Levantamento Completo de Cliente — Gestor de Tráfego

## Passo 1 — Briefing do Cliente

Apresente o formulário abaixo e **aguarde o preenchimento completo** antes de prosseguir:

```
📋 BRIEFING DO CLIENTE

1. Nome da empresa / marca:
2. Nicho / segmento de mercado:
3. Produto ou serviço principal:
4. Localização de atuação:
5. Ticket médio / faixa de preço:
6. Investimento mensal em tráfego pago: (R$)
7. Plataformas desejadas: (Meta Ads, Google Ads, TikTok Ads…)
8. Diferenciais competitivos que o cliente percebe em si:
9. Público-alvo na visão do cliente:
10. Concorrentes conhecidos: (mínimo 3, com URL se possível)
11. Presença online atual: (site, Instagram, Facebook, YouTube…)
12. Histórico com tráfego pago: (nunca anunciou / já anunciou — resultados?)
13. Objetivo principal: (leads, vendas, awareness, cadastros…)
14. Informações adicionais:
```

## Passo 2 — Pesquisa Profunda (6 subagentes em paralelo)

Com o briefing completo, dispare os subagentes abaixo **simultaneamente**.

### Subagente A — Mercado, Tendências e Restrições

Use Perplexity ou `/pesquisa` para levantar:

- Tamanho do mercado: volume, crescimento, projeções
- Tendências dos últimos 12 meses e sazonalidade / picos de compra
- Oportunidades não exploradas e ameaças emergentes
- Comportamento do consumidor com fontes (IBGE, Sebrae, Statista, relatórios setoriais)

**Restrições por plataforma:**
- Meta Ads: categorias sensíveis (saúde, emagrecimento, financeiro, suplementos, crédito, imóveis)
- Google Ads: conteúdo sensível, certificações exigidas (ex: LegitScript)
- TikTok Ads: categorias proibidas ou com aprovação especial
- Para cada restrição encontrada, documente o impacto prático na estratégia

### Subagente B — Público-Alvo, Personas e Padrões Criativos

**Público-alvo:** perfil demográfico (idade, gênero, renda, escolaridade, localização) e psicográfico (valores, estilo de vida, interesses). Mapeie: dores principais, desejos de compra, objeções mais comuns, duração da jornada de decisão e plataformas digitais preferidas.

**Construa 2 personas** com: nome fictício, idade, profissão, renda, localização, estado civil — e para cada uma: 3 dores, 2 desejos, 2 objeções, comportamento digital (plataformas, tipo de conteúdo, influenciadores), e uma frase que representa seu mindset.

**Padrões criativos do nicho:** formatos que performam (UGC, carrossel, vídeo curto, depoimento, antes/depois), hook visual/verbal dominante, duração média dos vídeos, paleta de cores predominante, tom (formal/informal/técnico/emocional) e ângulos de venda mais usados (dor, desejo, prova social, autoridade).

### Subagente C — Análise de Concorrentes (Diretos e Indiretos)

Comece pelos concorrentes do briefing, depois identifique novos **diretos** (mesmo produto/público) e **indiretos** (soluções alternativas ao mesmo problema).

Para cada concorrente analise: site (proposta de valor, CTA, prova social, oferta), Instagram, Facebook, YouTube, posicionamento (premium/popular/especialista), como ancora preço, oferta principal (garantia, bônus, trial, parcelamento), prova social (reviews, certificações), pontos fortes e vulnerabilidades.

### Subagente D — Funil e Landing Pages dos Concorrentes

Para cada concorrente, trace o funil: como captam atenção (entrada) → proposta e oferta da LP (CTA, prova social, urgência, garantia) → mecanismo de conversão (compra direta, formulário, WhatsApp, agendamento) → pós-clique (e-mail/WhatsApp, remarketing) → estrutura topo/meio/fundo percebida.

Documente URLs reais das landing pages encontradas.

### Subagente E — Referências de Anúncios dos Concorrentes

Busque anúncios ativos em:
- Meta Ads Library: `https://www.facebook.com/ads/library/?q=[NOME]&search_type=keyword_unordered&media_type=all&country=BR`
- Google Ads Transparency: `https://adstransparency.google.com/?region=BR&query=[NOME]`

Para cada anúncio relevante documente: concorrente e tipo (imagem/vídeo/carrossel), link direto, tom e pessoa do discurso, palavras-chave recorrentes, CTA e urgência, formato criativo (problema→solução / antes→depois / depoimento / educativo), ângulo de venda, por que provavelmente está funcionando, e oportunidade de diferenciação para o cliente.

### Subagente F — Palavras-chave e Benchmark de KPIs

**Palavras-chave:** termos bottom-funnel (intenção de compra), mid-funnel (problema/dor), top-funnel (educação), termos de concorrentes (conquista), negativos óbvios. Para os principais: estimativa de CPC e volume de busca. Identifique quais termos os concorrentes parecem estar comprando via Google Ads Transparency.

**Benchmark de KPIs do nicho** para as plataformas escolhidas: CTR médio, CPM, CPL, CPA/CPV, taxa de conversão da LP, ROAS (se e-commerce). Se dados específicos não existirem, use o setor mais próximo e sinalize claramente.

## Passo 3 — Análise Estratégica Final

Com todos os dados coletados, execute diretamente:

**SWOT do cliente:** monte a matriz com 3–5 itens por quadrante — Forças e Fraquezas (internas) e Oportunidades e Ameaças (externas) — baseada no briefing e na pesquisa real, não em conselhos genéricos.

**Distribuição de budget:** com base no investimento informado e nos objetivos, sugira alocação por plataforma (valor em R$ e %) com justificativa, divisão por etapa do funil dentro de cada plataforma e premissas/observações relevantes.

## Passo 4 — Gerar Relatório HTML

Salve como `levantamento-[nome-cliente]-[YYYY-MM-DD].html` com:
- Sidebar fixa com âncoras para cada seção
- Header: nome do cliente, nicho, data, gestor
- Design profissional: fonte Inter (Google Fonts), responsivo, cards para personas e SWOT, tabelas para concorrentes e KPIs, blocos de anúncio com link clicável, badge de fonte em cada dado

**19 seções:** Resumo Executivo · Análise de Mercado · Restrições e Conformidade · Público-Alvo · Personas · Tendências do Setor · Padrões Criativos · Concorrentes Diretos · Concorrentes Indiretos · Posicionamento Online dos Concorrentes · Funil e Landing Pages · Análise de Oferta · Referências de Anúncios · Palavras-chave Estratégicas · Benchmark de KPIs · SWOT do Cliente · Oportunidades e Recomendações · Distribuição de Budget · Fontes e Referências

## Notas Operacionais

- Dados reais e específicos — nunca inventar; se não encontrou, indicar explicitamente
- Se `/pesquisa` não estiver disponível, use Perplexity com múltiplas queries paralelas
- Para screenshots de anúncios: forneça o link direto e instrua o usuário a capturar manualmente

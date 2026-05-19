---
name: site2skill
description: >
  Cria automaticamente uma skill cliente de API para qualquer site web. Use
  sempre que o usuário invocar /site2skill, ou disser "cria uma skill pra
  [site]", "quero integrar com [site]", "analisa o tráfego de [site]". O
  fluxo: usuário exporta um arquivo HAR pelo DevTools do Chrome dele, Claude
  parseia o HAR e gera a skill. O parser detecta automaticamente se o site
  tem Cloudflare/CSRF e escolhe entre 2 modos: (1) modo simples — curl com
  cookies em .env, sem Chrome rodando; (2) modo CDP — Chrome real faz as
  chamadas, pra sites com Cloudflare ou CSRF rotativo.
---

# site2skill — gerador de skill conversacional

A skill é **conversacional**, não baseada em flags. O fluxo é uma conversa em português entre você (Claude) e o usuário. Você guia, captura, gera. O usuário não precisa saber o que é HAR, endpoint, fetch, ou cookie.

## Princípio chave

A skill gerada **nunca armazena cookies ou tokens**. Ela manda o Chrome (que já está logado) executar `fetch()` dentro da aba do site. Cookies + TLS + auth são providos pelo browser. Isso resolve Cloudflare, sessão expirada e tokens rotativos automaticamente.

---

## Passo 0 — verificar pré-requisito (Python)

A geração da skill depende só de Python 3 (pro `parse_har.py`). Verifique antes de tudo:

```bash
python3 --version 2>&1
```

Se faltar, oriente: "Você precisa do Python 3 instalado. No Mac já vem; no Windows: `winget install python3`."

> **Não confunda:** os pré-requisitos da **skill gerada** (Node.js, Chrome dedicado, função `chrome-debug` no shell) ficam documentados na própria skill filha — o template `references/skill-template.md` já cobre isso. Aqui no `/site2skill` o foco é só *gerar*.

---

## Fluxo conversacional (passo a passo)

### Passo 1 — pedir o HAR

Pergunte ao user uma vez:

> "Pra capturar o tráfego, exporta um arquivo HAR do seu Chrome. Faz assim:
>
> 1. Abre o site no seu Chrome (logado, se for área autenticada)
> 2. Aperta **F12** pra abrir o DevTools
> 3. Clica na aba **Network**
> 4. Marca a checkbox ✅ **Preserve log** (importante!)
> 5. Limpa o log com 🚫 (canto superior esquerdo)
> 6. Navega no site fazendo as ações que você quer expor pro agente: busca, abre detalhes, vê pedidos. (1-3 min)
> 7. Botão direito em qualquer linha → **Save all as HAR with content**
> 8. Salva o arquivo (vai pro Downloads) e me passa o caminho"

Espere o user mandar o caminho. Quando mandar, pule direto pro Passo 2 (parse).

**Por que HAR e não captura ao vivo:**
- Chrome principal do user já tem trust score do Cloudflare (cookies, JS challenges resolvidos historicamente). Bot Fight Mode não dispara — coisa que dogfood real em 2026-05-04 mostrou ser problema crítico em sites BR (Clubinho de Ofertas bloqueou perfil dedicado de cara).
- Login real do user, com 2FA/captcha já resolvidos no histórico do Chrome principal.
- HAR contém TUDO: requests + responses + headers + cookies + timing. Nada se perde.
- Aluno pode revisar o HAR antes de mandar, pra checar dado sensível.
- Funciona em qualquer OS sem precisar Chrome dedicado.

**"Save all as HAR with content"** vs **"Save as HAR"** simples: a primeira inclui response bodies, a segunda não. **Sempre peça a "with content"** — sem o body de response, o parser não consegue inferir shapes.

Espere alguns segundos pro capture flushar o JSON.

### Passo 2 — parsear e decidir o modo

```bash
python3 ~/.claude/skills/site2skill/scripts/parse_har.py <caminho-do-har>
```

O parser retorna:
- `main_host` — host principal da API
- `recommended_mode` — **`simple`** ou **`cdp`**
- `detection.has_cloudflare`, `detection.has_csrf_header`, `detection.has_bearer`
- `detection.auth_flow` — `cookie` / `csrf` / `bearer-mint` / `unknown`
- `detection.auth_provider`, `detection.auth_audience`
- `detection.response_shape` — `array` / `paginated` / `object`
- `detection.mint_endpoint` — endpoint que minta o Bearer
- `endpoints[]` — método, path parametrizado, status codes, `is_third_party`
- `auth.session_cookies` — cookies de sessão filtrados pelo domínio do main_host

**Decisão de modo:**
- `cdp` se: `has_cloudflare` OR `has_csrf_header` OR `auth_flow == 'bearer-mint'`
- `simple` caso contrário

### Passo 3 — gerar a skill auto-contida

**Se `recommended_mode == "simple"`:** Use `references/skill-template-simple.md`.
**Se `recommended_mode == "cdp"`:** Use `references/skill-template.md`.

### Passo 4 — confirmar e ensinar

> "✓ Skill /<slug> criada! Mapeei N endpoints (X principal + Y de APIs auxiliares)."

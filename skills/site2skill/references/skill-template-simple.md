# Template para skill gerada pelo /site2skill (modo simples — curl + cookies)

Use este template quando o site **NÃO tem Cloudflare nem CSRF rotativo**.

Substitua tudo entre `{{ }}`. Crie 3 arquivos: `SKILL.md`, `.env` (com cookies) e `.gitignore`.

---

```
---
name: {{slug}}
description: >
  Cliente para a API de {{nome-amigavel}} ({{host}}). Use quando o usuário
  quiser {{tipos-de-acao-que-o-site-faz-em-portugues}}. Aceita pedidos em
  português livre. {{exemplos-naturais-de-pedidos}}.
---

# {{nome-amigavel}} — Cliente de API (modo simples)

**Host principal:** `https://{{host}}`
**Auth:** cookies de sessão lidos de `.env` ao lado deste arquivo

## Pré-requisito

Arquivo `.env` ao lado deste `SKILL.md`:
```
COOKIES="nome1=valor1; nome2=valor2"
```

## Padrão de execução

```bash
source ~/.claude/skills/{{slug}}/.env
curl -s "https://{{host}}/api/PATH" -H "Accept: application/json" -b "$COOKIES"
```

## Tratamento de erro

- **401/403** → cookies expiraram. Rode `/site2skill` de novo com HAR novo.
- **`.env` faltando** → recriar via `/site2skill`.
```

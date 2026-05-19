# Template para skill gerada pelo /site2skill (modo chrome-cdp via skill compartilhada)

Substitua tudo entre `{{ }}`.

---

```
---
name: {{slug}}
description: >
  Cliente para a API de {{nome-amigavel}} ({{host}}). Use quando o usuário
  quiser {{tipos-de-acao-que-o-site-faz-em-portugues}}. Aceita pedidos em
  português livre. {{exemplos-naturais-de-pedidos}}.
---

# {{nome-amigavel}} — Cliente de API

**Host principal:** `https://{{host}}` (acessado via Chrome principal do usuário, usando o CDP embutido no `/site2skill`)

## Pré-requisito (uma vez por máquina)

1. **Skill `/site2skill` instalada** (essa skill usa o `cdp.mjs` que vem embutido nela).
2. **Toggle de remote debugging do Chrome ligado.** Abra `chrome://inspect/#remote-debugging` no seu Chrome **principal** e ligue o switch.
3. **Aba aberta em `https://{{host}}`** no Chrome principal, com login feito.

## Como usar

1. Liste abas: `cdp.mjs list`
2. Pegue o targetId da aba do `{{host}}`
3. Rode `cdp.mjs eval <target> "<fetch JS>"` — retorna JSON
4. Apresente o resultado em português, nunca JSON bruto.

## Endpoints — site principal (via chrome-cdp)

{{tabela-endpoints-do-host-principal}}

## Tratamento de erro

- **`cdp.mjs list` falha** → toggle de remote debugging desligado
- **Status 401/403** → sessão expirou no Chrome, faça login de novo
- **`TypeError: Failed to fetch`** → targetId errado, confirme com `cdp list`
```

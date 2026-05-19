# Deploy no Cloudflare Pages — Guia Completo

Deploy de sites estáticos (HTML/CSS/JS) no Cloudflare Pages via Wrangler CLI.
Tempo estimado: 2-5 minutos após configuração inicial.

---

## Pré-requisitos

### 1. Node.js instalado?

```bash
node --version
```
Se não: https://nodejs.org (instalar LTS)

### 2. Wrangler CLI instalado?

```bash
wrangler --version
```
Se não:
```bash
npm install -g wrangler
```

### 3. Conta Cloudflare?

Se não tem: https://dash.cloudflare.com/sign-up (gratuito, não precisa cartão)

---

## Autenticação

### Opção A — Login interativo (recomendado para primeira vez)

```bash
wrangler login
```
Abre o browser, o usuário autoriza, token salvo automaticamente.

### Opção B — API Token (para automação)

1. Acessar: https://dash.cloudflare.com/profile/api-tokens
2. Criar token com permissão: **Cloudflare Pages: Edit**
3. Exportar:
```bash
export CLOUDFLARE_API_TOKEN=seu_token_aqui
```

---

## Deploy Passo a Passo

### Estrutura de arquivos esperada

O site deve estar em um diretório com pelo menos `index.html`:

```
site-output/
├── index.html       ← obrigatório
├── style.css        ← opcional (se separado)
└── script.js        ← opcional (se separado)
```

Se o site é um único `index.html` autocontido (CSS e JS embutidos), funciona perfeitamente.

---

### Primeiro deploy (projeto novo)

```bash
# 1. Criar projeto no Cloudflare Pages (só na primeira vez)
wrangler pages project create nome-do-projeto

# 2. Fazer o deploy
wrangler pages deploy ./site-output --project-name nome-do-projeto
```

O `nome-do-projeto` vira a URL: `https://nome-do-projeto.pages.dev`

**Escolha um nome descritivo e sem espaços:**
- `clinica-silva` → clinica-silva.pages.dev
- `dr-antonio-odonto` → dr-antonio-odonto.pages.dev
- `fisio-curitiba-demo` → fisio-curitiba-demo.pages.dev

---

### Deploys seguintes (atualizar o site)

```bash
# Só o deploy, sem criar projeto
wrangler pages deploy ./site-output --project-name nome-do-projeto
```

---

### Verificar o deploy

```bash
# Listar deployments
wrangler pages deployment list --project-name nome-do-projeto
```

---

## Resultado Esperado

Após deploy bem-sucedido:

```
✨ Deployment complete! Take a peek over at https://abc123.nome-do-projeto.pages.dev
```

A URL final será: `https://nome-do-projeto.pages.dev`

---

## Configurar Domínio Próprio (opcional)

Se o cliente tiver um domínio:

### No Cloudflare Dashboard:
1. Abrir: https://dash.cloudflare.com → Pages → [projeto] → Custom Domains
2. Adicionar `www.dominio.com.br` ou `dominio.com.br`
3. Cloudflare configura o DNS automaticamente se o domínio estiver no Cloudflare

### Se o domínio estiver em outro registrador (GoDaddy, Locaweb, Registro.br):
Adicionar registro CNAME:
```
www  →  nome-do-projeto.pages.dev
```
E registro CNAME apex ou redirecionamento:
```
@    →  nome-do-projeto.pages.dev
```

---

## Troubleshooting

### "Authentication error" ou "Not logged in"
```bash
wrangler logout
wrangler login
```

### "Project not found"
```bash
# Verificar projetos existentes
wrangler pages project list
```

### "Directory not found"
Verificar se está no diretório correto e se `site-output/` existe:
```bash
ls site-output/
```

### Site carregando mas sem estilos
Verificar se o CSS está embutido no HTML ou se os caminhos estão corretos:
- Embutido: `<style>...</style>` dentro do `<head>` — funciona sempre
- Arquivo separado: `<link href="./style.css">` — precisa do arquivo junto

### Wrangler não encontrado após npm install
```bash
# Verificar PATH
which wrangler
# Se não encontrar, usar npx:
npx wrangler pages deploy ./site-output --project-name nome-do-projeto
```

---

## Limites do Plano Gratuito Cloudflare Pages

| Recurso | Gratuito |
|---------|----------|
| Sites | Ilimitados |
| Requests/mês | 100.000 |
| Bandwidth | Ilimitado |
| Builds/mês | 500 |
| Custom domains | Ilimitados |
| SSL automático | ✅ |
| CDN global | ✅ |

Para um site de dentista/médico com tráfego local, o plano gratuito é mais do que suficiente.

---

## Script Completo de Deploy Automatizado

Para deployar diretamente do workspace:

```bash
#!/bin/bash
# deploy.sh — Executar com: bash deploy.sh

PROJECT_NAME=$1
SITE_DIR="./site-output"

if [ -z "$PROJECT_NAME" ]; then
  echo "Uso: bash deploy.sh nome-do-projeto"
  exit 1
fi

echo "🚀 Iniciando deploy de $SITE_DIR para Cloudflare Pages..."

# Verificar wrangler
if ! command -v wrangler &> /dev/null; then
  echo "Instalando wrangler..."
  npm install -g wrangler
fi

# Criar projeto se não existir (ignora erro se já existir)
wrangler pages project create $PROJECT_NAME 2>/dev/null || true

# Deploy
wrangler pages deploy $SITE_DIR --project-name $PROJECT_NAME

echo "✅ Deploy concluído!"
echo "🌐 URL: https://$PROJECT_NAME.pages.dev"
```

Uso:
```bash
bash deploy.sh clinica-silva-demo
```

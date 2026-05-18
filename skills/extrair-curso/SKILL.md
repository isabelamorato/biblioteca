---
name: extrair-curso
description: >
  Extrai curso online — vídeo, áudio MP3 e transcrição com timestamps — de plataformas
  de cursos como Hotmart, Kiwify, Teachable, Memberkit, Eduzz, comunidade Circle,
  Hubla, Greenn, Cademí, ou self-host. Funciona porque captura o stream HLS que o
  player do browser carrega — o usuário fica logado normalmente, a skill escuta o
  Chrome via DevTools Protocol. Use SEMPRE que o usuário pedir "extrair curso",
  "baixar curso", "salvar aulas", "transcrever curso inteiro", "fazer backup do curso",
  ou colar URL de uma aula em qualquer plataforma de cursos online. Aborta limpo se
  detectar DRM (Widevine/FairPlay/PlayReady) — comum em Hotmart Premium e Vimeo OTT.
  Roda em Claude Code (precisa de Bash); não funciona em Claude Desktop.
---

# /extrair-curso

Extrai cursos online — vídeo (opcional), áudio MP3, transcrição com timestamps, índice navigável — usando o **próprio browser autenticado** do usuário como porta de entrada. Não scrapa, não burla auth, não baixa direto da URL: deixa o player tocar normalmente e captura o stream m3u8 via Chrome DevTools Protocol.

A skill é plataforma-agnóstica porque HLS é padrão aberto. O que muda entre plataformas é o "chrome em volta" — botões de navegação, layout do player, nomes das aulas. Esse "chrome" é resolvido em runtime usando árvore de acessibilidade + raciocínio do Claude, sem seletor por plataforma.

## Quando usar / quando não usar

**Use quando:**
- Usuário cola URL de aula de plataforma de cursos online
- Pede "baixar curso inteiro", "transcrever todas as aulas", "fazer backup do curso que comprei", "estudar offline"

**Não use quando:**
- É vídeo de YouTube público — `youtube-downloader` é melhor
- Aluno só quer transcrever 1 arquivo de áudio que ele já tem — `/etl-audio` direto
- Plataforma usa DRM (Widevine/FairPlay/PlayReady) — skill detecta no manifest e aborta

## Pré-requisitos

1. **Claude Code** (não funciona em Claude Desktop — precisa Bash pra rodar Node + ffmpeg). **Windows: Git Bash (via Git for Windows) ou WSL2.** PowerShell/cmd nativo não roda os scripts.
2. **Google Chrome instalado.** A skill **spawna um Chrome dedicado próprio** com profile isolado em `~/.cache/extrair-curso/chrome-profile/`. **Não usa o Chrome principal do user** — não interfere com sessões dele, e ele pode usar o Chrome normal enquanto a skill roda.
3. **Node.js 22+** instalado separadamente (`brew install node` no Mac, `winget install OpenJS.NodeJS` no Windows). Não vem com Chrome.
4. **ffmpeg** instalado (`brew install ffmpeg` no Mac, `winget install Gyan.FFmpeg` no Windows).
5. **`/etl-audio`** instalada — esta skill delega a transcrição pra ela.
6. **Login na plataforma é HITL na primeira execução**: skill detecta se está deslogado e pede pro user logar uma vez. Login persiste enquanto JWT da plataforma não expirar (ex: Hotmart = 48h) e o profile dedicado não for limpo.

A skill é **autônoma**: ela embute internamente uma cópia da CLI `cdp.mjs` em `scripts/`. **Não precisa instalar `/chrome-cdp` separadamente** nem ativar remote debugging manualmente.

### Por que Chrome dedicado (e não o Chrome do user)

- **Isolamento:** user pode usar o Chrome principal sem que ações dele (mudar aba, fechar aba, navegar) atrapalhem o CDP da skill
- **Sem prompt "Allow debugging?"** porque o user-data-dir é próprio
- **Sem polluíção** de extensions do user (ad-blockers, etc) que podem quebrar players
- **`--restore-last-session` flag:** preserva session cookies (TGC do CAS, JSESSIONID, etc) entre kills do Chrome — essencial pra SSO Hotmart e similares. Validado empiricamente em 2026-05-06.

## Sintaxe de invocação

```
/extrair-curso <url-da-primeira-aula>            # pergunta áudio vs vídeo antes de começar
/extrair-curso <url-da-primeira-aula> --audio    # explícito: só áudio + transcrição
/extrair-curso <url-da-primeira-aula> --video    # explícito: vídeo + áudio + transcrição
```

Sem URL, dispare a Pergunta 5 (ver "Protocolo de interação" abaixo).

## Protocolo de interação

**Toda pergunta ao aluno usa a tool `AskUserQuestion`.** Sem exceção. Não digite a pergunta como texto livre esperando resposta — é menos confiável e quebra UX em interfaces que renderizam choices nativamente.

### Pergunta 1 — modo (se não veio `--audio` nem `--video`)

```
question: "Como quer baixar o curso?"
header: "Modo"
options:
  - label: "Só áudio (Recommended)"
    description: "MP3 ~15-45MB por aula. Ideal pra estudar e transcrever."
  - label: "Vídeo + áudio extraído"
    description: "MP4 1080p ~80-300MB. Skill extrai MP3 dele localmente (instantâneo)."
```

### Pergunta 2 — próxima aula não detectada

```
question: "Aula NN salva. Como continuar?"
header: "Próximo passo"
options:
  - label: "Vou colar a URL da próxima"
    description: "Você navega pra próxima aula no Chrome e cola a URL aqui."
  - label: "Encerrar curso"
    description: "Trato a captura como completa e gero o índice final."
```

### Pergunta 3 — confirmação de botão "próxima" identificado com baixa confiança

```
question: "Encontrei {N} candidatos pra 'próxima aula'. Qual clico?"
header: "Botão próxima"
options:
  - label: "{descrição candidato 1}"
  - label: "{descrição candidato 2}"
  - label: "Nenhum, pula essa decisão"
```

### Pergunta 4 — cookies expirados durante captura

```
question: "Cookies expiraram durante o download. O que fazer?"
header: "Auth"
options:
  - label: "Renovei a sessão, tenta de novo (Recommended)"
  - label: "Pula essa aula"
  - label: "Encerrar"
```

### Pergunta 5 — quando aluno não forneceu URL inicial

```
question: "Qual a URL da primeira aula?"
header: "URL"
options:
  - label: "Vou colar agora"
  - label: "Não sei onde achar"
```

### Pergunta 6 — tradução de legenda (apenas se idioma original ≠ português)

```
question: "O curso está em {idioma detectado}. Quer também legenda em português?"
header: "Tradução"
options:
  - label: "Sim, traduzir todas as legendas pra PT"
  - label: "Não, manter só no idioma original"
```

### Pergunta 7 — login HITL no Chrome dedicado (primeira execução por plataforma)

```
question: "Chrome dedicado abriu mas você não está logado em {plataforma}. Loga e me avisa quando terminar."
header: "Login"
options:
  - label: "Loguei, pode continuar (Recommended)"
  - label: "Não consigo logar"
  - label: "Cancelar extração"
```

## Fluxo

### Setup inicial (uma vez por sessão de extração)

1. **Spawn (ou reuso) do Chrome dedicado.**
   ```bash
   DTAP=$(bash scripts/spawn-or-attach-chrome.sh "<url-da-aula>")
   export CDP_PORT_FILE="$DTAP"
   ```

2. **Encontre a aba.** Use `node scripts/cdp.mjs list` pra listar abas.

3. **Habilite Network domain.**
   ```bash
   node scripts/cdp.mjs evalraw <target> Network.enable '{}'
   ```

4. **Detecção de login + HITL inicial.**
   ```bash
   node scripts/cdp.mjs eval <target> "({isLoggedOut: document.body.innerText.includes('Cadastre-se aqui') && document.body.innerText.includes('Entrar') && !document.body.innerText.includes('Sair'), url: location.href})"
   ```
   Se `isLoggedOut: true`, dispare a Pergunta 7.

### Classificação de tipo de aula (CRÍTICA)

Antes de baixar qualquer coisa, **classifique a aula**:

```bash
node scripts/cdp.mjs eval <target> "({iframe: [...document.querySelectorAll('iframe')].find(f => f.src.includes('cf-embed.play.hotmart') && f.clientWidth > 100)?.src, dlCount: [...document.querySelectorAll('button')].filter(b => b.textContent.trim() === 'Download').length})"
```

| Sinal | Tipo da aula | Fluxo |
|---|---|---|
| `iframe` presente | **vídeo** | Fast path (Panda/Hotmart Player) → `hotmart-extract.sh` ou `capture.sh` |
| `iframe` ausente, `dlCount > 0` | **texto + materiais** | `text-aula-extract.sh` |
| `iframe` ausente, `dlCount == 0` | **texto puro** | `text-aula-extract.sh` (só `.md`) |
| Sem título, sem iframe, sem botões | **fim do curso** | Pula |

### Estrutura do fluxo principal (modo vídeo)

- **Fase 1** — loop por aula: classifica → baixa MP4 (vídeo) ou MD+materiais (texto). Navega pra próxima.
- **Fase 2** — em lote: extrai MP3 dos MP4 e transcreve via `transcribe.sh --srt`.

**No modo áudio**, as fases colapsam — baixa MP3 direto + transcreve por aula.

### Regra de feedback ao aluno (CRÍTICA)

- **A cada aula finalizada na Fase 1**, emita mensagem: *"✓ Aula N/total — `título` (XmYs, NMB) — restam M aulas"*
- Se rodando script em background, **faça poll a cada ~60s** e reporte aulas novas. Não espere o `=== FIM ===`.

### Para cada aula (loop = Fase 1)

1. **Detecte o player e tente fast path.**
   ```bash
   node scripts/cdp.mjs eval <target> "[...document.querySelectorAll('iframe')].map(f => ({src: f.src, w: f.clientWidth})).filter(f => f.w > 100)"
   ```

2. **Espere o player carregar metadata** (se fast path falhou). Poll de 500ms por até 30s:
   ```bash
   node scripts/cdp.mjs eval <target> "({rs: document.querySelector('video')?.readyState, t: document.querySelector('video')?.currentTime})"
   ```

3. **Capture o m3u8 master** via `scripts/iframe-capture.mjs` para iframes cross-origin.

4. **Detecte DRM.** Baixe o master com `curl -s <m3u8>` e busque por Widevine/FairPlay/PlayReady URNs. Se DRM real, aborte.

5. **Capture cookies.**
   ```bash
   node scripts/cdp.mjs evalraw <target> Network.getCookies '{"urls":["<dominio-do-m3u8>"]}'
   ```

6. **Capture metadados e baixe a mídia.**
   ```bash
   # Modo áudio
   bash scripts/capture.sh <m3u8-url> ~/cursos/<slug>/aula-NN-<titulo>.mp3 "<cookies>" "<referer>"
   # Modo vídeo
   bash scripts/capture.sh --video <m3u8-url> ~/cursos/<slug>/aula-NN-<titulo>.mp4 "<cookies>" "<referer>"
   ```

7. **Transcreva** (modo áudio direto):
   ```bash
   bash ~/.claude/skills/etl-audio/scripts/transcribe.sh <mp3> <basename>.json
   ```

8. **Salve metadados** em `aula-NN-<titulo>.meta.json`.

9. **Navegue pra próxima aula** via snap + click. Se múltiplos candidatos → Pergunta 3. Se nenhum → Pergunta 2.

### Fase 2 — Extração de áudio + transcrição em lote (apenas modo vídeo)

```bash
for VIDEO in ~/cursos/<slug>/aula-*.mp4; do
  BASE="${VIDEO%.mp4}"
  [ ! -f "$BASE.mp3" ] && ffmpeg -hide_banner -loglevel error -i "$VIDEO" -vn -c:a libmp3lame -b:a 64k -y "$BASE.mp3"
done
```

Após extrações: `bash ~/.claude/skills/etl-audio/scripts/transcribe.sh --srt <mp3> <basename>.json` em cada MP3.

## Modo batch — múltiplos cursos com pool paralelo

Use `pool-runner.sh` pra paralelizar download (4 workers) e transcrição (MAX_PARALLEL=2).

```bash
bash scripts/pool-runner.sh 4 ~/.cache/extrair-curso/download-jobs.txt /tmp/pool-download
bash scripts/pool-runner.sh 2 ~/.cache/extrair-curso/transcribe-jobs.txt /tmp/pool-transcribe
```

**Default MAX_PARALLEL=2 pra transcrição** (não 4 — Voxtral throttla agressivo com 4+ workers simultanâneos). Cada job tem retry built-in (5 tentativas × sleep 60s).

## Fast paths (providers conhecidos)

| Provider | Sinal no iframe `src` | Como obter URL master m3u8 |
|---|---|---|
| **Panda Video** | `*.tv.pandavideo.com.br/embed/?v=<videoId>` | URL pública direta: `https://b-{playerId}.tv.pandavideo.com.br/{videoId}/master.m3u8`. Sem cookies. |
| **Hotmart Player nativo** | `cf-embed.play.hotmart.com/embed/<mediaCode>` | Curl iframe URL com cookies da page hotmart.com. Parse `__NEXT_DATA__` → `pageProps.applicationData.mediaAssets[0].url`. Token Akamai expira em ~8min — baixar imediatamente. |

## Aulas-texto e materiais

Usar `scripts/text-aula-extract.sh` que extrai texto via `h1.h5._font-weight-bold`, limpa ruído de UI, e usa `Page.setDownloadBehavior` pra materiais:

```bash
bash scripts/text-aula-extract.sh <target-id> <outdir> <basename>
```

## Plataforma desconhecida

Consulte antes de desistir:
- **Katomart** (`github.com/katomaro/katomart`): 40+ plataformas brasileiras mapeadas
- **Gist juvenal/Hotmart**: API oficial Hotmart com auth OAuth Sparkle

## Cookies: opcionais por padrão

- **Signed URL** (Panda Video, Mux): sem cookies. Capture sem cookies primeiro; se ffmpeg dá 200, OK.
- **Cookie-based**: capture via `Network.getCookies` e passe pro `capture.sh`.

Tente sem cookies primeiro. Se `capture.sh` retornar exit 2 (auth error), aí captura cookies.

## Composição com outras skills

- **CDP**: `scripts/cdp.mjs` é cópia local da CLI `/chrome-cdp`. Skill é autônoma.
- **`/etl-audio`**: chamada via `bash ~/.claude/skills/etl-audio/scripts/transcribe.sh [--srt] <mp3> <basename>.json`. Sempre gera `.json` + `.md`. Com `--srt`, gera também `.srt`.

## Convenções de output

```
~/cursos/
└── <slug-do-curso>/
    ├── aula-01-introducao.mp3
    ├── aula-01-introducao.mp4         (opcional, se --video)
    ├── aula-01-introducao.json        (raw Voxtral — source of truth)
    ├── aula-01-introducao.md          (transcrição LLM/humano-friendly)
    ├── aula-01-introducao.srt         (só modo vídeo — auto-load com MP4)
    └── index.md
```

## Limites conhecidos

- **DRM** (Widevine/FairPlay/PlayReady): aborta.
- **Player não-HTML5**: passo 1 do loop falha. Skill avisa e pede ação manual.
- **Cursos com >100 aulas**: pode levar horas. Loop é incremental.

## Pitfalls aprendidos em campo

### 1. Parsing de CSV/dados estruturados → SEMPRE Python, NUNCA bash `read IFS='|'`
`read -r` quebra com strings UTF-8 longas. Use `python3 -c "with open(csv) as f: parts = line.split('|')"`.

### 2. Mistral Voxtral: default MAX_PARALLEL=2 com retry built-in — não 4
5+ workers paralelos disparam `429 Rate limit exceeded`. 4 também falha em batches médios. Default=2 + retry 5x/sleep 60s.

### 3. Dedupe de aulas: por `mediaCode` do iframe, NÃO por slug do título
Usar `set()` de `mediaCode` já visto. Se repetir, pula com aviso.

### 4. Validar JSON após gerar — fallback se ffprobe falhou
Após escrever JSON, ler de volta com `json.load`. Se inválido, fallback duracao_segundos=0.

### 5. LIVEs longas (>1h) podem travar no token Akamai mid-download
Monitorar progresso do ffmpeg — se `time=` não avançar por 60s, matar e reiniciar.

### 6. Workers paralelos: cada um grava em log separado, NUNCA `tee` compartilhado
Cada worker grava em `/tmp/worker-NN.log` próprio.

### 7. Feedback obrigatório a cada 60-90s
Após lançar background task >60s, **sempre** agendar `ScheduleWakeup(delaySeconds=90)`.

### 8. Cleanup de processos órfãos: `pkill -9 ffmpeg`
```bash
pkill -f "wrapper-script.sh" 2>/dev/null
sleep 2
pkill -9 ffmpeg 2>/dev/null
```

### 9. brew updates podem quebrar ffmpeg silenciosamente
Diagnóstico: `ffmpeg -version` + `ffprobe -version`. Se reclamar de symbol/library, `brew reinstall ffmpeg`.

### 10. Modal "Perfil" do Hotmart Club = sessão SSO expirou
Causa: cookie `TGC` (Ticket Granting Cookie do CAS) expirou. Com `--restore-last-session`, TGC persiste entre kills. Se mesmo assim aparecer modal, JWT do localStorage expirou (Hotmart: 48h). Dispare Pergunta 7.

### 11. ffmpeg paralelo lendo do mesmo SSD USB → falhas silenciosas
- SSD interno NVMe: 4 workers seguros.
- SSD USB ou HD externo: 2 workers no máximo.

### 12. Use case: processar curso já-baixado (sem CDP)
Se argumento é path absoluto local: pule CDP, vá direto para Fase 2. Split output: MP4+MP3+SRT ficam no SSD; JSON+MD+materiais vão para `~/cursos/<slug>/`.

### 13. Não mostre log inteiro de falhas
Use filtro Python compacto: `cat progress.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(f\"{d['done']}/{d['total']} ok={d['ok']} fail={d['fail']}\"); [print('FAIL:',f['file'][:80],'::',f['error'][:80]) for f in d['failures'][:5]]"`

### 14. Módulos colapsáveis no Hotmart Club: aulas escondidas até clicar no botão de módulo
Fix: chamar `btn[reactPropsKey].onClick()` (NÃO `btn.click()`). Implementado em `scripts/discover-courses.sh` via `expand_collapsible_modules`.

### 15. CDP_PORT_FILE não herda em subshells do `bash -c`
Fix: workers devem ter fallback default:
```bash
export CDP_PORT_FILE="${CDP_PORT_FILE:-$HOME/.cache/extrair-curso/chrome-profile/DevToolsActivePort}"
```

### 16. MP4 parciais corrompidos passam silenciosos pra fase de transcrição
Fix duplo:
1. Trap em workers de download pra remover MP4 < 1MB em SIGTERM/SIGINT.
2. Validação anti-corrupção ao gerar `transcribe-jobs.txt` via `ffprobe -show_entries format=duration`.

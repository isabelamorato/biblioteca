#!/usr/bin/env bash
# 00-inventory.sh -- Fase 0 do /curso2skill
# Inventaria curso e classifica em Tipo A/B/C
#
# Uso: bash 00-inventory.sh <slug>
# Output: JSON em stdout

set -uo pipefail

SLUG="${1:?usage: 00-inventory.sh <slug>}"
COURSE_DIR="$HOME/cursos/$SLUG"

if [ ! -d "$COURSE_DIR" ]; then
  echo "{\"error\": \"course not found: $COURSE_DIR\"}" >&2
  exit 1
fi

# Detecta layout
DEEP_TRANSCRIPTS=$(find "$COURSE_DIR" -mindepth 2 -type f \( -name "*.md" -o -name "*.json" \) ! -name "index.md" ! -name "*.meta.json" 2>/dev/null | head -1 | wc -l | tr -d ' ')
if [ "$DEEP_TRANSCRIPTS" -gt 0 ]; then
  LAYOUT="multi-module"
else
  LAYOUT="flat"
fi

# Conta arquivos de transcricao (recursivo)
N_MD=$(find "$COURSE_DIR" -type f -name "*.md" ! -name "index.md" 2>/dev/null | wc -l | tr -d ' ')
N_JSON=$(find "$COURSE_DIR" -type f -name "*.json" ! -name "*.meta.json" 2>/dev/null | wc -l | tr -d ' ')
N_TXT=$(find "$COURSE_DIR" -type f -name "*.txt" 2>/dev/null | wc -l | tr -d ' ')
N_SRT=$(find "$COURSE_DIR" -type f -name "*.srt" 2>/dev/null | wc -l | tr -d ' ')
N_MP4=$(find "$COURSE_DIR" -type f -name "*.mp4" 2>/dev/null | wc -l | tr -d ' ')
N_MP3=$(find "$COURSE_DIR" -type f -name "*.mp3" 2>/dev/null | wc -l | tr -d ' ')

# N_AULAS = basenames unicos
N_AULAS=$(find "$COURSE_DIR" -type f \( -name "*.md" -o -name "*.json" -o -name "*.txt" \) \
  ! -name "index.md" ! -name "*.meta.json" 2>/dev/null \
  | sed 's/\.[^.]*$//' | sort -u | wc -l | tr -d ' ')

# Materiais anexados
N_MATERIAIS=$(find "$COURSE_DIR" -type f \( -name "*.pdf" -o -name "*.zip" -o -name "*.docx" -o -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) 2>/dev/null | wc -l | tr -d ' ')

TAMANHO_MAT=$(find "$COURSE_DIR" -type f \( -name "*.pdf" -o -name "*.zip" -o -name "*.docx" -o -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) 2>/dev/null \
  | python3 -c "import sys, os; print(sum(os.path.getsize(f.strip()) for f in sys.stdin if f.strip()))" 2>/dev/null || echo 0)

# Tokens estimados (palavras x 1.3)
if [ "$N_MD" -gt 0 ]; then
  WORDS=$(find "$COURSE_DIR" -type f -name "*.md" ! -name "index.md" -exec cat {} + 2>/dev/null | wc -w | tr -d ' ')
else
  WORDS=$(find "$COURSE_DIR" -type f -name "*.txt" -exec cat {} + 2>/dev/null | wc -w | tr -d ' ')
fi
TOKENS=$(awk -v w="$WORDS" 'BEGIN { print int(w*1.3) }')

# Cobertura
N_TRANSCRITAS=$((N_MD + N_TXT))
EXPECTED=$N_AULAS
if [ "$N_MP4" -gt "$EXPECTED" ]; then
  EXPECTED=$N_MP4
fi
COVERAGE=$(python3 -c "print(round($N_TRANSCRITAS / max($EXPECTED, 1) * 100))" 2>/dev/null || echo 0)

# Detector de pipeline executavel
PIPELINE_HINTS=$(find "$COURSE_DIR" -type f -name "*.md" ! -name "index.md" \
  -exec grep -lE "playwright|puppeteer|ffmpeg|npm install|pip install|^#!|bash -c|python3? |.sh\b|.py\b|requirements.txt|package.json" {} + 2>/dev/null | wc -l | tr -d ' ')
HAS_PIPELINE=false
[ "$PIPELINE_HINTS" -gt 5 ] && HAS_PIPELINE=true

# Classificacao
if [ $N_MATERIAIS -gt 0 ] && [ $TAMANHO_MAT -gt 50000 ]; then
  TIPO="A"
  STRATEGY="RICH ARTIFACTS -- TRANSCODIFICACAO"
elif [ $COVERAGE -lt 80 ]; then
  TIPO="C"
  STRATEGY="INCOMPLETE -- execute /extrair-curso $SLUG --redo antes"
else
  TIPO="B"
  STRATEGY="TRANSCRIPT-ONLY -- CTA REAL"
fi

cat <<EOF
{
  "slug": "$SLUG",
  "course_dir": "$COURSE_DIR",
  "layout": "$LAYOUT",
  "n_aulas": $N_AULAS,
  "n_transcripts_md": $N_MD,
  "n_transcripts_json": $N_JSON,
  "n_transcripts_txt": $N_TXT,
  "n_srt": $N_SRT,
  "n_video_mp4": $N_MP4,
  "n_audio_mp3": $N_MP3,
  "n_materiais_anexados": $N_MATERIAIS,
  "tamanho_materiais_bytes": $TAMANHO_MAT,
  "tokens_estimados_transcricao": $TOKENS,
  "coverage_transcricoes_pct": $COVERAGE,
  "tipo": "$TIPO",
  "estrategia": "$STRATEGY",
  "has_executable_pipeline": $HAS_PIPELINE,
  "pipeline_signal_count": $PIPELINE_HINTS,
  "fase_1_4_required": $HAS_PIPELINE
}
EOF

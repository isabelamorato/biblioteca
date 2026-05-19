#!/usr/bin/env bash
# Limpa processos zumbi do Chrome dedicado de debug.
set -euo pipefail

PROFILE="$HOME/.chrome-cdp-profile"

if pgrep -f "user-data-dir=$PROFILE" > /dev/null; then
  echo "Matando processos do Chrome dedicado..."
  pkill -f "user-data-dir=$PROFILE" || true
  sleep 2
fi

if [ -f "$PROFILE/DevToolsActivePort" ]; then
  rm -f "$PROFILE/DevToolsActivePort"
  echo "Port file removido."
fi

echo "Pronto. Rode \`chrome-debug <url>\` pra abrir limpo."

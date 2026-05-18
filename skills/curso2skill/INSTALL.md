# Instalacao -- curso2skill

## Como instalar

1. Descompacte este arquivo (`curso2skill.skill` e um ZIP):
   ```bash
   unzip curso2skill.skill -d ~/.claude/skills/
   ```
   Resultado esperado: pasta `~/.claude/skills/curso2skill/` com `SKILL.md` dentro.

2. Reinicie o Claude Code (ou rode `/help` pra forcar reload das skills).

3. Teste invocando: `/curso2skill` (sem argumentos -- vai listar cursos disponiveis em `~/cursos/`).

## Pre-requisitos

| Skill | Para que | Obrigatoria? |
|---|---|---|
| `/extrair-curso` | Extrai curso de Hotmart/Kiwify/etc | Sim |
| `/etl-audio` | Re-transcreve aulas faltantes | So se algumas aulas vierem sem transcricao |
| `/etl-ocr` | Converte PDFs/workbooks em Markdown | So para cursos com material PDF denso |
| `skill-creator` | Valida a skill gerada com eval suite | Recomendada (Fase 3) |

## Convencao de pastas

A skill assume que cursos estao em `~/cursos/<slug>/`. Se voce usa outra pasta, edite `scripts/00-inventory.sh` e o `SKILL.md`.

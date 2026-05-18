# ACTA Matrix -- Dominando Claude Code (referencia de debug)

Fonte: Knowledge Audit completo em `.curso2skill/02-knowledge-audit.md`

## Resumo por passo

| Passo | Regras Green | Tacitas Yellow | Inferidas Red |
|---|---|---|---|
| 1 - Instalar | 5 | 0 | 0 |
| 2 - CLAUDE.md | 2 | 1 | 0 |
| 3 - memory.md | 1 | 2 | 0 |
| 4 - Skills | 4 | 1 | 0 |
| 5 - Agentes | 3 | 1 | 0 |
| 6 - FPCN | 4 | 2 | 0 |
| Gerais | 0 | 1 | 2 |
| **Total** | **19** | **8** | **2** |

## Inferencias Red nao confirmadas

- **#27**: Multiplos terminais em paralelo com contextos isolados
- **#28**: Base de conhecimento obrigatoria antes de builds complexos

## Erros mais criticos a evitar

1. Criar skill sem pasta `scripts/` -> nao executa nada
2. Usar Windows PowerShell 5.1 (antigo) em vez do PowerShell 7
3. Executar direto sem FPCN -> retrabalho + gasto de tokens
4. Nao usar memory.md -> regras se perdem entre sessoes
5. Aceitar primeiro plano sem confrontar -> resultado superficial

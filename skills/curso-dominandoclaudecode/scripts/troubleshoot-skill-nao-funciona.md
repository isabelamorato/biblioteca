# Troubleshoot: Skill nao funciona

## Decision tree

```
Skill nao executa nada?
|-- Tem pasta scripts/ dentro da skill?
|   |-- NAO -> Criar scripts/ e pedir ao Claude para gerar o script da ferramenta
|   `-- SIM -> Continuar...
|
|-- skill.md tem campo "quando ativar"?
|   |-- NAO -> Adicionar: quando usar esta skill, gatilhos que a disparam
|   `-- SIM -> Continuar...
|
|-- O agente referencia a skill explicitamente?
|   |-- NAO -> No .md do agente: adicionar "consulte a skill X para Y"
|   `-- SIM -> Continuar...
|
|-- A ferramenta tem API disponivel?
|   |-- NAO -> Integracao automatica nao e possivel; usar outra abordagem
|   `-- SIM -> Verificar se credenciais foram fornecidas ao script
|
`-- Erro especifico?
    `-- Copiar o erro completo e jogar no Claude: "me ajude a resolver este erro"
```

## Erros comuns

| Sintoma | Causa provavel | Solucao |
|---|---|---|
| Skill so conversa, nao age | Sem scripts/ | Criar pasta scripts/ + gerar script |
| Agente ignora a skill | skill.md sem "quando ativar" | Adicionar gatilhos no skill.md |
| Script da erro de autenticacao | Credenciais nao configuradas | Fornecer API key/token a skill |
| Claude cria errado na 1a tentativa | Nao usou FPCN | Refazer com Planejar->Confrontar antes |

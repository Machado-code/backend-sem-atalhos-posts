# Inbox: pedidos para o escritório

Um arquivo por pedido, com o nome `AAAA-MM-DD-assunto.md`. A resposta vai em
`outbox/` com o mesmo nome. Quando o pedido terminar, mude o status para `feito`.
Quem pediu lê a resposta e muda o status para `encerrado`.

Pedidos, respostas e mudanças de status vão direto na `main`, sem PR (só arquivos desta
pasta e de `outbox/`). O escritório também pode pedir algo ao claude.ai: use
`de: escritorio` e `para: claude-ai`.

## Modelo

```markdown
---
de: claude-ai        # claude-ai | escritorio
para: escritorio     # escritorio | claude-ai
status: aberto       # aberto | em-andamento | feito | bloqueado | encerrado
---

# Pedido
O que precisa ser feito, em poucas linhas.

# Pronto quando
- Critério verificável 1
- Critério verificável 2

# Contexto
Links, arquivos do repositório ou decisões que importam.
```

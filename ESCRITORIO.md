# Escritório: papel e regras

Guia para o escritório (Claude Code no VS Code do Matheus) trabalhar neste repositório
junto com o Claude do claude.ai. Leia também o `PROJETO.md`, que é a memória do projeto.

## Quem faz o quê

| Quem | Faz |
| --- | --- |
| Claude (claude.ai) | Página de vendas, banco de pautas, textos, imagens e vídeos dos posts; tarefa semanal (domingo 20h34) que cria os rascunhos no Buffer (Instagram e LinkedIn) e agenda depois do "aprovo" do Matheus. |
| Matheus | Responde "aprovo" (ou pede mudanças) uma vez por semana e responde os comentários. |
| Escritório | Tudo o que precisa de .NET ou de rodar código de verdade, sempre por pedido em `inbox/`. |

O claude.ai não tem .NET. O escritório é quem confirma que um trecho C# faz o que o post diz.

## Rotina

1. Ao começar a trabalhar no repositório: `git pull` na `main` e veja `inbox/` em busca
   de arquivos com `status: aberto`.
2. Para cada pedido: mude o status para `em-andamento`, faça o trabalho numa branch
   própria (`escritorio/<assunto>`), escreva a resposta em `outbox/` com o MESMO nome do
   pedido e mude o status para `feito` (ou `bloqueado`, explicando o motivo).
3. Abra um PR com a resposta. Quem aprova o merge é o Matheus.
4. Se um pedido tiver prazo, ele vem escrito no próprio pedido.

## Atividades

- **Conferir desafios C#**: rodar os trechos do `pautas/banco-de-pautas.md` e confirmar que
  a saída bate com a resposta marcada. Pendente: `inbox/2026-11-19-conferir-desafios-csharp.md`.
- **Conferir trechos novos**: quando o claude.ai criar um desafio ou dica com código C#
  fora do banco atual, ele abre um pedido em `inbox/`.
- **Ferramentas do repositório**: melhorar `scripts/` (render das imagens, geração de
  vídeo) ou criar uma ferramenta que rode os desafios automaticamente, só quando houver
  pedido em `inbox/`.
- **Projetos de exemplo**: se algum post precisar de um projeto .NET pequeno para mostrar
  algo (antes e depois de uma refatoração, por exemplo), o pedido vem pelo `inbox/`.

## Pode

- Ler todo o repositório.
- Criar branches, commits e PRs.
- Escrever em `outbox/` e mudar o `status` dos pedidos em `inbox/`.
- Rodar .NET, SQL e scripts na máquina do Matheus para conferir código.
- Criar arquivos novos em `scripts/` ou `tools/` quando um pedido pedir.
- Abrir um pedido para o claude.ai, se achar algo errado: crie `inbox/AAAA-MM-DD-assunto.md`
  com `de: escritorio` e `para: claude-ai`.

## Não pode

- Fazer merge de PR ou commit direto na `main`: tudo passa pelo Matheus.
- Mudar por conta própria `pautas/`, `posts/`, `docs/` (página de vendas), `PROJETO.md` ou
  este arquivo. Se algo estiver errado, descreva na resposta em `outbox/` que o claude.ai
  corrige (a tarefa de domingo depende desses arquivos).
- Publicar, agendar ou mexer em Buffer, Instagram, LinkedIn ou Kiwify.
- Mudar preço, cupom, produto ou as tarefas agendadas.
- Colocar o nome do Matheus em imagens ou posts da marca.
- Commitar tokens, chaves, senhas ou números de vendas (o repositório é público).
- Commitar os guias completos (PDF, `.md` ou `.zip` do pacote) ou gabaritos inteiros.

## Formato da resposta em `outbox/`

```markdown
---
de: escritorio
para: claude-ai
pedido: inbox/AAAA-MM-DD-assunto.md
status: feito   # feito | bloqueado
---

# Resultado
O que foi feito, em poucas linhas.

# Detalhes
Saídas reais, versões usadas (.NET, SQL) e arquivos ou PRs criados.

# Divergências
O que não bate com o banco de pautas, com a saída exata. "Nenhuma" se estiver tudo certo.
```

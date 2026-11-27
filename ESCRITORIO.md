# Escritório: papel e regras

Guia para o escritório (Claude Code no VS Code do Matheus) trabalhar neste repositório
junto com o Claude do claude.ai. Leia também o `PROJETO.md`, que é a memória do projeto.

## Quem faz o quê

| Quem | Faz |
| --- | --- |
| Claude (claude.ai) | Página de vendas, banco de pautas, textos, imagens e vídeos dos posts; tarefa semanal (domingo 20h34) que cria os rascunhos no Buffer (Instagram e LinkedIn) e agenda depois do "aprovo" do Matheus. |
| Matheus | Responde "aprovo" (ou pede mudanças) uma vez por semana, responde os comentários e dá o "aprovo" nos PRs quando recebe o aviso de que estão prontos. |
| Escritório | Tudo o que precisa de .NET ou de rodar código de verdade, sempre por pedido em `inbox/`. |

O claude.ai não tem .NET. O escritório é quem confirma que um trecho C# faz o que o post diz.

## Rotina

A conversa entre o claude.ai e o escritório acontece em `inbox/` e `outbox/`, direto na
`main`, sem PR e sem esperar o Matheus. Qualquer outra mudança passa por PR e só entra na
`main` com o "aprovo" dele.

1. Ao começar: `git pull` na `main`. Veja `inbox/` em busca de pedidos com
   `para: escritorio` e `status: aberto`, e os PRs com a etiqueta `ajustar`.
2. Pedido: mude o status para `em-andamento` (commit direto na `main`). Faça o trabalho,
   escreva a resposta em `outbox/` com o MESMO nome do pedido e mude o status para
   `feito` (ou `bloqueado`, explicando o motivo). Resposta e status vão direto na `main`.
3. Se o trabalho mudar arquivos fora de `inbox/` e `outbox/` (código, scripts, projetos
   de exemplo), faça numa branch `escritorio/<assunto>`, abra um PR com as etiquetas
   `escritorio` e `revisar` e cite o PR na resposta em `outbox/`.
4. Ciclo do PR:
   - o claude.ai revisa e comenta no PR. Se precisar de ajuste, troca a etiqueta para
     `ajustar`;
   - o escritório corrige, comenta o que mudou e volta a etiqueta para `revisar`;
   - quando estiver certo, o claude.ai põe `pronto-para-aprovo` e o Matheus recebe um aviso
     no celular. O merge é feito pelo claude.ai, só depois do "aprovo" dele.
5. As duas pontas usam a mesma conta do GitHub: todo comentário em PR começa com
   `[claude.ai]` ou `[escritório]`.
6. Se um pedido tiver prazo, ele vem escrito no próprio pedido.

Do lado do claude.ai, a tarefa agendada "Revisar PRs do escritório" roda nos dias úteis
às 9h40 e às 17h40: lê `inbox/` e `outbox/`, revisa os PRs e avisa o Matheus quando algum
fica `pronto-para-aprovo`. Quando o claude.ai termina de ler uma resposta, muda o status do
pedido para `encerrado`.

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
- Commitar direto na `main` SÓ arquivos `.md` em `inbox/` e `outbox/` (pedidos, respostas
  e status). Nada de código, imagens, binários ou arquivos de outras pastas.
- Escrever em `outbox/` e mudar o `status` dos pedidos em `inbox/`.
- Rodar .NET, SQL e scripts na máquina do Matheus para conferir código.
- Criar arquivos novos em `scripts/` ou `tools/` quando um pedido pedir.
- Abrir um pedido para o claude.ai, se achar algo errado: crie `inbox/AAAA-MM-DD-assunto.md`
  com `de: escritorio` e `para: claude-ai`.

## Não pode

- Fazer merge de PR (quem faz é o claude.ai, depois do "aprovo" do Matheus).
- Commit direto na `main` fora de `inbox/` e `outbox/`.
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

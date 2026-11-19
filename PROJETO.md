# Projeto: lançamento do pacote .NET (R$ 39)

Memória compartilhada entre o Claude do claude.ai e o escritório (Claude Code no VS Code).
Quem mudar uma decisão atualiza este arquivo no mesmo commit.

## Objetivo
Primeira venda do pacote de 5 guias .NET/backend ("aprender sem depender de IA")
em até 30 dias, com o mínimo de trabalho manual.

## Responsabilidades
- Claude (claude.ai): página de vendas, posts, legendas e imagens; tarefa semanal
  (domingo à noite) que cria RASCUNHOS no Buffer. Nunca publica.
- Matheus: revisa e agenda os rascunhos às segundas; responde comentários.
- Escritório: tarefas de código pedidas em `inbox/`.

## Stack
- Venda e entrega: Kiwify.
- Publicação: Buffer gratuito (LinkedIn + Instagram profissional + 1 canal livre).
  MCP: https://mcp.buffer.com/mcp
- Imagens: PNG 1080x1350 neste repositório (público). O Buffer recebe o link raw:
  `https://raw.githubusercontent.com/Machado-code/backend-sem-atalhos-posts/main/<caminho>`
- Ritmo: 3 posts por semana por canal. Formato fixo: desafio de código C# com
  alternativas A–D; a resposta sai no post seguinte.

## Como nos comunicamos
- `inbox/`: pedidos para o escritório. Um arquivo por pedido:
  `inbox/AAAA-MM-DD-assunto.md` (modelo em `inbox/README.md`).
- `outbox/`: respostas do escritório, com o MESMO nome do pedido.
- `posts/AAAA-MM/`: textos (`.md`), fonte das imagens (`.html`) e imagens (`.png`).
- Mudanças entram por pull request; o Matheus aprova o merge na `main`.

## Regras
- Nada é publicado sem aprovação do Matheus.
- Posts em PT-BR, 1ª pessoa, no máximo 3 hashtags, sem promessa de emprego ou salário.
- Repositório PÚBLICO: nunca commitar tokens, chaves, senhas ou números de vendas.

## Status
- 2026-11-19: repositório criado; estrutura inicial e primeiro desafio (desafio-01) enviados.
- Pendente (Matheus): Kiwify, Instagram profissional, Buffer + conector, enviar os 5 guias.

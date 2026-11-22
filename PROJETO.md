# Projeto: lançamento do pacote .NET (R$ 47)

Memória compartilhada entre o Claude do claude.ai e o escritório (Claude Code no VS Code).
Quem mudar uma decisão atualiza este arquivo no mesmo commit.

## Objetivo
Primeira venda do pacote de 5 guias .NET/backend ("aprender sem depender de IA")
em até 30 dias, com o mínimo de trabalho manual.

## Responsabilidades
- Claude (claude.ai): página de vendas, posts, legendas e imagens; tarefa semanal
  (domingo 20h34) que cria RASCUNHOS no Buffer e mostra a semana ao Matheus. Só agenda
  depois que ele escreve "aprovo"; nunca publica direto.
- Matheus: revisa a semana e responde "aprovo" (ou pede mudanças); responde comentários.
  Sem rosto e sem voz nos posts, para não gerar demanda.
- Escritório: tarefas de código pedidas em `inbox/` (rodar e conferir C#, ferramentas).
  Papel, rotina e limites em `ESCRITORIO.md`.

## Marca
- Marca: Sem Atalhos ("dev sem atalhos"). Produto: Dev Raiz. Domínio: sematalhos.dev.br.
- Página de vendas: `docs/index.html`, publicada pelo GitHub Pages (main, /docs) em
  https://sematalhos.dev.br. Capa do produto: `docs/img/capa-kiwify.png`.
- Decisões da página: preço R$ 47; cupom DEVRAIZ (R$ 37) só nos primeiros 7 dias; sem suporte;
  sem seção "sobre o autor".

## Stack
- Venda e entrega: Kiwify.
- Publicação: Buffer gratuito com o Instagram @sematalhos.dev e o LinkedIn pessoal do
  Matheus (perfil Matheus F. Machado), com o mesmo fluxo de rascunho e "aprovo";
  sobra 1 canal livre.
  MCP: https://mcp.buffer.com/mcp
- Imagens: PNG 1080x1350 (e Reels MP4 1080x1920) neste repositório (público). O Buffer
  recebe o link raw fixado no commit:
  `https://raw.githubusercontent.com/Machado-code/backend-sem-atalhos-posts/<sha>/<caminho>`
- Ritmo: 3 posts por semana por canal: Instagram às 19h, LinkedIn às 8h30 (mesmas
  imagens; texto do LinkedIn com um pouco mais de contexto; carrossel vai como PDF). Segunda: post interativo com o desafio
  (rodízio de formatos: A–D, PR, Parece certo, Qual você usaria?). Quarta: a resposta
  (imagem ou Reels sem voz). Sexta: dica (carrossel) ou post de venda. Formatos e
  rodízio no banco de pautas. Horário revisto em 18/12 com dados reais.
- Pautas: `pautas/banco-de-pautas.md` (fila semanal, desafios com resposta, dicas e
  posts de venda). A tarefa semanal segue a fila e atualiza o status.

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
- Os guias completos (PDF, .md e .zip do pacote) NUNCA entram aqui. Só trechos curtos
  de divulgação, como os do banco de pautas.

## Próximo produto (ideia, não construir antes da primeira venda)
- Parte 2 do Dev Raiz: programar COM IA usando a base dos 5 guias. Não contradiz a marca:
  o Dev Raiz ensina a não depender da IA; a Parte 2 ensina a conferir o que ela gera.
  Cada módulo retoma um guia (depurar com IA e pegar quando ela erra, conferir com
  EXPLAIN o SQL que ela sugere, montar a API em par com ela, testar o código gerado,
  saber quando não usar). Escada: Dev Raiz (R$ 47) → Parte 2 (preço maior) → oferta
  para quem comprou o primeiro (upsell/order bump na Kiwify).
- Validação antes de construir: (1) primeira venda do Dev Raiz; (2) comentários e alcance
  dos posts "Parece certo" com código no estilo do que a IA costuma sugerir; (3) uma
  pergunta a quem comprou: "faria sentido uma parte com IA?".
- Regra que continua valendo: nada de avatar ou voz gerados por IA se passando pelo Matheus.

## Status
- 2026-11-19: repositório criado; estrutura inicial e primeiro desafio (desafio-01) enviados.
- 2026-11-19: banco de pautas criado (26 desafios, 16 dicas, 6 posts de venda);
  texto da página de vendas pronto num doc do claude.ai para revisão.
- 2026-11-19: página de vendas no ar pelo GitHub Pages; DNS de sematalhos.dev.br
  validado (registro.br).
- 2026-11-19: HTTPS ativo. Kiwify: produto criado (R$ 47), área de membros com
  2 módulos ("Os 5 guias" com o PDF; "Projetos e exercícios" com o .zip), ambos
  publicados. Botões da página apontam para o checkout https://pay.kiwify.com.br/ZD70Zmh.
- Pendente (Matheus): verificação de identidade na Kiwify, compra de teste,
  cupom DEVRAIZ no dia do lançamento, e-mail contato@sematalhos.dev.br no Zoho,
  Instagram profissional, Buffer + conector.
- Pendente (escritório): `inbox/2026-11-19-conferir-desafios-csharp.md`.
- 2026-11-20: Instagram @sematalhos.dev ligado ao Buffer (conector ativo no claude.ai);
  tarefa semanal criada (domingo 20h34); posts às 19h; rodízio de formatos e quadros
  extras (Humor de dev, Bug real, Dev Raiz responde) a partir da semana 6.
  Revisão do horário com dados reais em 18/12.
- 2026-11-22: semana 1 em rascunho no Buffer (Instagram e LinkedIn): desafio D00 na
  segunda, resposta em imagem na quarta e carrossel T01 (stack trace) na sexta.

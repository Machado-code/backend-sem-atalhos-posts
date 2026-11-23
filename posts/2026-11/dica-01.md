---
formato: dica (carrossel, Anatomia)
semana: 1
dica: T01
titulo: Ler um stack trace em 30 segundos
data: 2026-11-27
imagens: [dica-01-1.png, dica-01-2.png, dica-01-3.png, dica-01-4.png, dica-01-5.png]
documento: dica-01.pdf   # LinkedIn: o carrossel vai como documento
canais: [instagram, linkedin]
horarios: {instagram: "19:00", linkedin: "08:30"}
status: rascunho
---

# Instagram (sexta, 19h)

Stack trace parece um muro de texto, mas dá para ler em 30 segundos. São 4 partes:

1. O tipo da exceção
2. A mensagem
3. A primeira linha do SEU projeto (arquivo e linha)
4. O que vem depois do último --->

Arrasta para o lado que eu mostro cada uma. Salva para usar no próximo erro.

#dotnet #csharp #backend

# LinkedIn (sexta, 8h30)

Quando um erro aparece, o impulso é copiar o stack trace inteiro e colar numa busca ou numa IA. Antes disso, vale gastar 30 segundos lendo: ele quase sempre já diz o que aconteceu e onde.

Eu leio em 4 partes: o tipo da exceção (a categoria do problema), a mensagem (o detalhe), a primeira linha que pertence ao meu projeto (a chamada que eu controlo, com arquivo e número da linha) e, quando existe, o que vem depois do último --->, que é a causa real.

Essa última parte é a que mais faz diferença no trabalho. Um DbUpdateException do EF Core só diz que algo falhou ao salvar; a exceção interna diz qual restrição do banco foi violada. Por isso, no log, eu registro a exceção inteira, não só a Message, que não traz o --->.

Deixei as 4 partes no documento abaixo, com um exemplo de cada. Vale salvar para o próximo erro em produção.

#dotnet #csharp #backend

# Textos alternativos

1. Slide 1 de 5: "Leia um stack trace em 30 segundos. Parece um muro de texto. São só 4 partes." Abaixo, um stack trace de exemplo: DbUpdateException ao salvar, com uma PostgresException interna de chave duplicada em IX_Clientes_Email, e as linhas "at" que passam por Npgsql, EF Core e Loja.Api.ClienteService.CriarAsync, em ClienteService.cs, linha 42.
2. Slide 2 de 5: "1 e 2. O tipo e a mensagem." A primeira linha do stack trace com DbUpdateException destacado em amarelo (o tipo, a categoria do erro) e a mensagem sublinhada em vermelho (o detalhe). Abaixo, tipos comuns: NullReferenceException, algo era null; KeyNotFoundException, a chave não existe; FormatException, texto que não virou número; DbUpdateException, o banco recusou a gravação.
3. Slide 3 de 5: "3. A primeira linha do SEU projeto." As linhas "at" do stack trace, com as do .NET e das bibliotecas apagadas e a linha Loja.Api.ClienteService.CriarAsync, em ClienteService.cs, linha 42, destacada e contornada em vermelho, com a nota "comece aqui". Texto: as de cima mostram onde estourou; desça até o primeiro nome do seu projeto, onde está a chamada que você controla.
4. Slide 4 de 5: "4. O que vem depois do último --->." A DbUpdateException aparece apagada e a parte interna destacada: PostgresException 23505, duplicate key value violates unique constraint IX_Clientes_Email. Texto: a causa real é um e-mail repetido, barrado pelo índice único do banco; no log, grave a exceção inteira, não só ex.Message.
5. Slide 5 de 5: "Em 30 segundos": 1, tipo, a categoria do erro; 2, mensagem, o detalhe do que falhou; 3, seu projeto, a primeira linha dele, com arquivo e linha; 4, último --->, a causa real, quando existe. "Só depois disso vale pesquisar, já sabendo o que perguntar. Salve para o próximo erro."

# Observação

O stack trace é um exemplo montado para o post (nomes encurtados para caber na tela), não um incidente real.

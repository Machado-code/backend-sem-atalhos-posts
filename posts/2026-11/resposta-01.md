---
formato: resposta (imagem)
semana: 1
desafio: D00
data: 2026-11-25
imagem: resposta-01.png
canais: [instagram, linkedin]
horarios: {instagram: "19:00", linkedin: "08:30"}
status: rascunho
---

# Instagram (quarta, 19h)

Resposta: B) 2.

O Where não filtra na hora. Ele guarda a regra e só a executa quando alguém pede o resultado, que aqui é o Count(). Nesse momento, a lista já tem o 4.

No EF Core é igual: enumerar a mesma consulta duas vezes faz duas idas ao banco. Se for usar o resultado mais de uma vez, chame ToList() antes.

Você acertou na segunda? Conta aqui.

#dotnet #csharp #backend

# LinkedIn (quarta, 8h30)

Resposta do desafio de segunda: B) 2.

O Where não filtra no momento em que é chamado. Ele guarda a regra e só a executa quando alguém pede o resultado, aqui no Count(). Quando isso acontece, o 4 já está na lista, então os pares são 2 e 4.

Isso se chama execução adiada (deferred execution) e, no backend, aparece muito com EF Core: a mesma consulta enumerada duas vezes vai duas vezes ao banco, e a segunda leitura pode trazer dados diferentes da primeira. Não quebra nenhum teste; aparece como lentidão ou como um número que não bate.

Minha regra: se vou usar o resultado mais de uma vez, chamo ToList() logo depois de montar a consulta. E, em code review, quando vejo um IEnumerable passando de uma camada para outra, pergunto em que momento ele de fato roda.

#dotnet #csharp #backend

# Texto alternativo da imagem

Resposta do desafio #1: B) 2. O mesmo trecho de C# da segunda, com anotações em vermelho: abaixo do Where, "ainda não filtrou nada"; abaixo do Console.WriteLine(pares.Count()), destacado em amarelo, "filtra só agora: { 2, 4 }". Embaixo: no EF Core, enumerar a mesma consulta duas vezes são duas idas ao banco; para usar o resultado mais de uma vez, chame .ToList() logo depois do Where.

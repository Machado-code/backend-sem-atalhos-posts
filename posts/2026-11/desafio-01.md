---
formato: desafio
imagem: desafio-01.png
canais: [linkedin, instagram]
status: rascunho
---

# Post 1: desafio

Sem rodar e sem perguntar pra IA: o que esse código imprime?

A) 1
B) 2
C) 3
D) Exceção

Responde só com a letra nos comentários. Na quarta eu explico, e o motivo está por trás de muito bug com EF Core.

#dotnet #csharp #backend

Texto alternativo da imagem: trecho de C# que cria uma lista com 1, 2 e 3, filtra os pares com Where, adiciona o 4 à lista e imprime pares.Count(); abaixo, as alternativas A) 1, B) 2, C) 3 e D) Exceção.

# Post 2: resposta (quarta-feira)

Resposta: B) 2.

O Where não filtra na hora. Ele guarda a regra e só a executa quando alguém pede o resultado, que aqui é o Count(). Nesse momento, a lista já tem o 4.

No EF Core é igual: enumerar a mesma consulta duas vezes faz duas idas ao banco. Se for usar o resultado mais de uma vez, chame ToList() antes.

#dotnet #csharp #backend

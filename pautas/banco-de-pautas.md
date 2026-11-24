# Banco de pautas: Dev Raiz

Pautas para divulgar o pacote "Dev Raiz: 5 guias para programar sem depender de IA".
Tudo aqui é material de divulgação: os guias completos, os gabaritos inteiros e os
scripts NUNCA entram neste repositório, que é público.

## Ritmo semanal

| Dia | O que sai | Imagem |
| --- | --- | --- |
| Segunda | Post interativo com o desafio da semana, no formato da coluna "Seg" da Fila | 1080x1350, layout de `posts/2026-11/desafio-01.html` |
| Quarta | Resposta do desafio de segunda, com a explicação, no formato da coluna "Qua" | Imagem 1080x1350 ou Reels sem voz 1080x1920 |
| Sexta | Dica (carrossel) ou post de venda, no formato da coluna "Sex" | Carrossel de 3 a 6 slides, 1080x1350 |

Horário (America/Sao_Paulo): Instagram às 19h, LinkedIn às 8h30, com as mesmas imagens.
Sem rosto e sem voz do Matheus: tudo é gerado aqui.

## Formatos (rodízio para não repetir)

O conteúdo de cada desafio (código, resposta, explicação) continua o mesmo; o que muda
é como ele é apresentado.

Segunda:
- `A–D`: "Sem rodar: o que esse código imprime?" com alternativas A–D; "comente só a letra".
- `PR`: "Você aprovaria esse PR?" O código aparece como um diff ou trecho de pull request
  (título curto do PR em cima). Pergunta: "aprova ou pede mudança? Comenta o porquê."
- `Parece certo`: "Compila, roda e parece certo. O que está errado aqui?" Sem alternativas;
  as pessoas apontam o problema nos comentários.
- `Qual você usaria?`: duas versões lado a lado (A e B) e a pergunta "qual você usaria e
  por quê?". Na quarta, a resposta diz qual eu uso, quando a outra faz sentido e o motivo.

Quarta:
- `Imagem`: a alternativa ou a linha certa destacada com marca-texto e a correção.
- `Reels`: vídeo vertical de 15 a 25 s, sem voz: o código aparece, a linha com problema
  é circulada em vermelho, a correção entra no lugar e a explicação vai em legendas
  curtas na tela. Se o vídeo falhar, vira `Imagem` e a tarefa avisa.

Sexta (dicas):
- `Passo a passo`: um slide por passo.
- `Antes e depois`: o jeito comum e o jeito certo, lado a lado.
- `Mito ou verdade`: uma afirmação por slide, com o veredito no seguinte.
- `Comparação`: duas ou três opções com quando usar cada uma.
- `Anatomia`: uma coisa só (um stack trace, uma requisição HTTP) com setas explicando cada parte.

Sexta (quadros, a partir da semana 6, mais ou menos um a cada 4 semanas). Podem sair do
conteúdo dos guias (git, deploy, logs, rotina de dev backend), desde que sejam úteis para
quem trabalha com .NET e backend; são complemento, não resumo dos módulos.
- `Humor de dev`: uma situação do dia a dia de dev, com texto e código no visual da marca.
  Piada original: nunca imagem de meme conhecido, personagem ou print de terceiros;
  nunca zombar de pessoas, empresas ou grupos; a IA pode ser alvo leve da piada, mas a
  marca não é contra IA. Uma imagem ou carrossel curto. Duas variações:
  - `Humor leve`: só para rir, uma situação que todo dev reconhece (commits de sexta,
    estimativa de "é rapidinho", nomes de variáveis, o deploy que "só muda um texto").
    Legenda curta e uma pergunta para comentar ("qual foi o seu?").
    Modelo: `posts/modelos/humor-leve.*`.
  - `Humor com lição`: a piada esconde um erro técnico de verdade e a legenda explica em
    duas ou três frases. Modelo: `posts/modelos/humor-com-licao.*`.
- `Bug real`: carrossel de 5 a 7 slides contando um incidente clássico de produção:
  sintoma → investigação → causa → correção → lição. Contado como cenário ("um caso
  comum"), nunca como se tivesse acontecido com o Matheus ou com uma empresa real.
- `Dev Raiz responde`: responde uma dúvida REAL deixada nos comentários. O Buffer não lê
  comentários, então o resumo da semana anterior pergunta ao Matheus se apareceu alguma
  dúvida boa (é opcional para ele). Sem pergunta real, a tarefa usa o substituto da Fila.
  Nunca inventar a pergunta.

## Chamada para venda por fase

- Semanas 1 e 2: nenhum link no post. O link fica só no perfil.
- Semanas 3 e 4 (lançamento): o post de resposta termina com "Esse é um dos detalhes que o Guia N treina" e o link.
- Da semana 5 em diante: uma menção leve ao guia no post de resposta; venda direta só nas pautas V.

## Chamada para a amostra (Instagram, toda semana)

Quem comenta "amostra" em qualquer post do Instagram recebe na DM o link da amostra
grátis (automação do NicoChat). Para puxar esses comentários:
- Uma vez por semana, só no Instagram, na legenda do post de sexta, antes das hashtags:
  "Quer as primeiras páginas do Dev Raiz? Comente AMOSTRA que eu te mando no direct."
- Se a sexta for um post de venda (V), a chamada vai no post de quarta, porque a sexta
  já tem a chamada de compra.
- Nunca no post de segunda (os comentários ali são as respostas do desafio) e nunca no
  LinkedIn (lá não há automação; quando a fase permitir link, use o do site).

## Regras

- Trechos de código curtos: no máximo 12 linhas e 48 caracteres por linha, para caber na imagem.
- Nunca publicar listas completas de exercícios, gabaritos inteiros ou os scripts do pacote.
- Números de desempenho sempre como "no teste do guia"; nunca como garantia.
- Desafios C# D00 a D10, D17, D20 e D21 rodados pelo escritório em 23/11 (.NET 8, 9 e 10):
  todos batem com a resposta marcada. Detalhes em `outbox/2026-11-19-conferir-desafios-csharp.md`.
- Posts em PT-BR, 1ª pessoa, no máximo 3 hashtags (#dotnet #csharp #backend ou #sql).
- Visual: o da página (papel quadriculado, tinta azul-marinho, caneta vermelha, marca-texto
  amarelo, fontes DejaVu Sans Mono e DejaVu Serif). Topo com "sem/atalhos" e o nome do
  quadro; rodapé com "@sematalhos.dev". Nunca o nome do Matheus nas imagens.
  Modelos: `posts/2026-11/desafio-01.html` e `posts/modelos/`.

## Fila

A tarefa semanal pega a primeira semana com status `pendente`, cria os rascunhos
no Buffer e muda o status para `rascunho`. Depois que o Matheus agenda, vira `agendado`.

Se um desafio não couber bem no formato da semana, a tarefa pode trocar pelo formato
de segunda mais próximo que ainda não saiu no último mês, e diz isso no resumo.

| Semana | Desafio | Seg | Qua | Sex | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | D00 | A–D | Imagem | T01 · Anatomia | agendado |
| 2 | D01 | Parece certo | Imagem | V01 | pendente |
| 3 | D13 | PR | Imagem | V03 | pendente |
| 4 | D17 | A–D | Reels | V05 | pendente |
| 5 | D02 | Qual você usaria? | Imagem | T09 · Passo a passo | pendente |
| 6 | D20 | Parece certo | Reels | Humor leve | pendente |
| 7 | D03 | PR | Imagem | T10 · Antes e depois | pendente |
| 8 | D11 | Qual você usaria? | Reels | V04 | pendente |
| 9 | D05 | A–D | Imagem | T12 · Anatomia | pendente |
| 10 | D14 | Parece certo | Reels | Bug real (usa o tema do T11: FK sem índice e N+1) | pendente |
| 11 | D07 | PR | Imagem | V06 | pendente |
| 12 | D18 | A–D | Reels | T04 · Antes e depois | pendente |
| 13 | D09 | Qual você usaria? | Imagem | T02 · Passo a passo | pendente |
| 14 | D15 | PR | Reels | Dev Raiz responde (sem pergunta real: Humor leve) | pendente |
| 15 | D21 | Parece certo | Imagem | T08 · Antes e depois | pendente |
| 16 | D04 | A–D | Reels | T13 · Mito ou verdade | pendente |
| 17 | D16 | Qual você usaria? | Imagem | T05 · Passo a passo | pendente |
| 18 | D06 | Parece certo | Reels | Humor com lição | pendente |
| 19 | D19 | A–D | Imagem | T16 · Anatomia | pendente |
| 20 | D22 | PR | Reels | T03 · Passo a passo | pendente |
| 21 | D08 | Parece certo | Imagem | T06 · Antes e depois | pendente |
| 22 | D10 | PR | Reels | Bug real (tema livre: um incidente clássico de backend) | pendente |
| 23 | D12 | A–D | Imagem | T07 · Comparação | pendente |
| 24 | D23 | Parece certo | Reels | Dev Raiz responde (sem pergunta real: Humor leve) | pendente |
| 25 | D24 | Qual você usaria? | Imagem | T14 · Passo a passo | pendente |
| 26 | D25 | PR | Reels | T15 · Comparação | pendente |

---

## Desafios (segunda + quarta)

### D00 · Extra · LINQ adiado
Já pronto em `posts/2026-11/desafio-01.*`. Resposta: B) 2.

### D01 · Guia 1, bug 4 · A porcentagem que dá zero
- Gancho: Compila, roda, não dá erro nenhum e está errado.
```csharp
int aprovados = 18;
int inscritos = 25;
double percentual = aprovados / inscritos * 100;

Console.WriteLine($"Aprovação: {percentual}%");
```
- Alternativas: A) Aprovação: 72% · B) Aprovação: 0% · C) Aprovação: 72,0% · D) Erro de compilação
- Resposta: **B**
- Explicação: `int / int` descarta a parte decimal, então 18 / 25 vira 0 antes de multiplicar. O `double` só entra depois, quando o estrago já foi feito. Correção: `aprovados * 100.0 / inscritos`.

### D02 · Guia 1, bug 7 · Dinheiro em double
- Gancho: Dez moedas de 10 centavos dão um real. Para o `double`, não.
```csharp
double saldo = 0;
for (int i = 0; i < 10; i++)
    saldo += 0.10;

Console.WriteLine(saldo == 1.00);
```
- Alternativas: A) True · B) False · C) Erro de compilação · D) Exceção
- Resposta: **B**
- Explicação: o `double` guarda frações em binário e não representa 0,10 exato. A soma dá 0,9999999999999999. Para dinheiro, use `decimal` em tudo: `0.10m` e `1.00m`.

### D03 · Guia 1, bug 5 · Removendo no meio do caminho
- Gancho: Um `foreach`, um `Remove` e um programa que cai.
```csharp
var tarefas = new List<string>
    { "estudar", "CANCELADA: bar", "treinar" };

foreach (var t in tarefas)
    if (t.StartsWith("CANCELADA"))
        tarefas.Remove(t);

Console.WriteLine(string.Join(", ", tarefas));
```
- Alternativas: A) estudar, treinar · B) estudar, CANCELADA: bar, treinar · C) Exceção · D) Erro de compilação
- Resposta: **C** (`InvalidOperationException: Collection was modified`)
- Explicação: não se altera uma lista enquanto o `foreach` percorre ela. Correção: `tarefas.RemoveAll(t => t.StartsWith("CANCELADA"));`.

### D04 · Guia 1, bug 6 · Maiúscula importa
- Gancho: Três usuários, dois ativos. Quantos o código encontra?
```csharp
string[] s = { "Ativo", "inativo", "ATIVO" };
Console.WriteLine(s.Count(x => x == "ativo"));
```
- Alternativas: A) 0 · B) 1 · C) 2 · D) 3
- Resposta: **A**
- Explicação: comparação de texto diferencia maiúsculas, e nenhum item é exatamente "ativo". Correção: `string.Equals(x, "ativo", StringComparison.OrdinalIgnoreCase)`, que imprime 2 ("inativo" não conta). Melhor ainda: um `enum`.

### D05 · Guia 1, bug 9 · Data com sotaque
- Gancho: Funciona na sua máquina. No servidor, o vencimento muda de mês.
```csharp
using System.Globalization;

CultureInfo.CurrentCulture = new("en-US");
var data = DateTime.Parse("03/04/2026");
Console.WriteLine(data.Month);
```
- Alternativas: A) 3 · B) 4 · C) Exceção · D) Depende do fuso horário
- Resposta: **A**
- Explicação: em inglês, o formato é mês/dia/ano. Servidores em nuvem e Docker costumam vir em inglês. Correção: `DateTime.ParseExact(..., "dd/MM/yyyy", CultureInfo.InvariantCulture)`; em APIs, use ISO: `2026-04-03`.
- Resposta pronta para comentário: em container com globalização invariante (Alpine, por exemplo), o `new("en-US")` lança `CultureNotFoundException` antes de imprimir; a resposta A vale para o `dotnet new console` normal. Mais um motivo para não depender da cultura do servidor.

### D06 · Guia 1, bug 10 · A propriedade que chama a si mesma
- Gancho: Quatro linhas de propriedade e o programa morre.
```csharp
var conta = new Conta { Titular = " Ana " };
Console.WriteLine(conta.Titular);

class Conta
{
    public string Titular
    {
        get => Titular;
        set => Titular = value.Trim();
    }
}
```
- Alternativas: A) Ana · B) " Ana " · C) O programa cai · D) Erro de compilação
- Resposta: **C** (stack overflow)
- Explicação: o `set` atribui a `Titular`, que chama o próprio `set`, para sempre. Stack overflow não dá para capturar com `catch`. Correção: guardar o valor num campo `_titular`.

### D07 · Guia 1, bug 8 · O await esquecido
- Gancho: O método salvou. O contador discorda.
```csharp
var repo = new Repo();
repo.SalvarAsync("Pedido 1");
Console.WriteLine(repo.Total);

class Repo
{
    readonly List<string> _dados = new();
    public int Total => _dados.Count;
    public async Task SalvarAsync(string s)
    { await Task.Delay(100); _dados.Add(s); }
}
```
- Alternativas: A) 1 · B) 0 · C) Exceção · D) Erro de compilação
- Resposta: **B**
- Explicação: sem `await`, o programa segue antes de o salvamento terminar. Numa API com EF Core, um `SaveChangesAsync()` sem `await` pode não gravar nada, sem erro nenhum.

### D08 · Guia 1, bug 2 · Um a mais
- Gancho: O bug mais antigo da programação ainda pega muita gente.
```csharp
var notas = new List<int> { 7, 9, 6, 10 };
int soma = 0;
for (int i = 0; i <= notas.Count; i++)
    soma += notas[i];

Console.WriteLine(soma / notas.Count);
```
- Alternativas: A) 8 · B) 6 · C) Exceção · D) 10
- Resposta: **C** (`ArgumentOutOfRangeException`)
- Explicação: o laço vai até `i == 4`, mas a lista só tem as posições 0 a 3. Troque `<=` por `<`, ou use `notas.Average()`.

### D09 · Guia 1, bug 3 · O item que não existe
- Gancho: `First` ou `FirstOrDefault`? Um dos dois derruba a API.
```csharp
var ids = new List<int> { 1, 2 };
var achado = ids.First(id => id == 3);
Console.WriteLine(achado);
```
- Alternativas: A) 0 · B) null · C) Exceção · D) Erro de compilação
- Resposta: **C** (`InvalidOperationException`)
- Explicação: `First` exige pelo menos um item. Detalhe extra: `FirstOrDefault` aqui devolveria 0, e numa lista de `int` o 0 pode ser um valor válido. Trate o "não achei" de forma explícita.

### D10 · Guia 1, bug 1 · O endereço que sumiu
- Gancho: O compilador avisou. Ninguém leu o warning.
```csharp
var clientes = new List<Cliente> {
    new("Ana", new Endereco("Recife")),
    new("Bruno", null),
    new("Carla", new Endereco("Santos")) };

foreach (var c in clientes)
    Console.WriteLine(c.Endereco.Cidade);

record Endereco(string Cidade);
record Cliente(string Nome, Endereco? Endereco);
```
- Pergunta: o que aparece antes do erro?
- Alternativas: A) Nada · B) Recife · C) Recife e Santos · D) Não dá erro
- Resposta: **B**
- Explicação: Bruno não tem endereço e o código acessa `.Cidade` mesmo assim. O compilador já avisava com `CS8602`. Correção: `c.Endereco?.Cidade ?? "não informado"`.

### D11 · Guia 2 · Singleton ou Scoped?
- Gancho: Criei uma despesa. Listei. Sumiu.
```csharp
builder.Services.AddScoped<
    IDespesaRepositorio,
    DespesaRepositorioMemoria>();

// POST /despesas  -> 201 Created
// GET  /despesas  -> ?
```
- Pergunta: o repositório guarda as despesas numa lista em memória. O que o GET devolve?
- Alternativas: A) A despesa criada · B) Uma lista vazia · C) Erro 500 · D) 404
- Resposta: **B**
- Explicação: `Scoped` cria uma instância por requisição. A lista do POST morre junto com ele. Lista em memória pede `Singleton`; `DbContext` pede `Scoped`.

### D12 · Guia 2 · O que tem dentro do JWT
- Gancho: Seu token de login é secreto? Não do jeito que você pensa.
```text
eyJhbGciOi...  .  eyJzdWIiOi...  .  SflKxwRJ...
  cabeçalho         conteúdo          assinatura
```
- Pergunta: o conteúdo de um JWT é:
- Alternativas: A) Criptografado · B) Só assinado: qualquer um lê · C) Um hash irreversível · D) Comprimido
- Resposta: **B**
- Explicação: a assinatura prova quem emitiu, mas o conteúdo é só Base64. Qualquer um decodifica. Nunca coloque dados sensíveis no token.

### D13 · Guia 3 · COUNT(*) no LEFT JOIN
- Gancho: A pegadinha de SQL mais comum em entrevista.
```sql
SELECT c.nome, COUNT(*) AS pedidos
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
GROUP BY c.id, c.nome;
```
- Pergunta: o Hugo nunca fez um pedido. Quanto aparece para ele?
- Alternativas: A) 0 · B) 1 · C) NULL · D) Erro
- Resposta: **B** (conferido no PostgreSQL 16)
- Explicação: o `LEFT JOIN` cria uma linha para o Hugo com os campos do pedido em `NULL`. `COUNT(*)` conta a linha; `COUNT(p.id)` ignora o `NULL` e mostra o certo: 0.

### D14 · Guia 3 · O apelido que não existe
- Gancho: Você escreve o SQL de cima para baixo. O banco, não.
```sql
SELECT nome, preco * 2 AS dobro
FROM produtos
WHERE dobro > 500;
```
- Pergunta: no PostgreSQL, o que acontece?
- Alternativas: A) Filtra certinho · B) Erro: a coluna "dobro" não existe · C) Ignora o WHERE · D) Volta vazio
- Resposta: **B** (conferido no PostgreSQL 16)
- Explicação: o banco roda o `WHERE` antes do `SELECT`, então o apelido ainda não existe. Ordem: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT.

### D15 · Guia 3 · A função que desliga o índice
- Gancho: Mesmo resultado, índice ignorado. No teste do guia: 114 ms contra 19 ms.
```sql
-- A
WHERE EXTRACT(YEAR FROM acessado_em) = 2025
  AND EXTRACT(MONTH FROM acessado_em) = 3
-- B
WHERE acessado_em >= '2025-03-01'
  AND acessado_em <  '2025-04-01'
```
- Pergunta: há um índice em `acessado_em`. Qual filtro usa o índice?
- Alternativas: A) O A · B) O B · C) Os dois · D) Nenhum
- Resposta: **B** (conferido no PostgreSQL 16 com 1 milhão de linhas)
- Explicação: o índice guarda os valores da coluna, não o resultado de `EXTRACT`. Regra: aplique funções no valor, nunca na coluna do `WHERE`.

### D16 · Guia 3 · A ordem das colunas no índice
- Gancho: Criou o índice e a consulta continua lenta? Olhe a ordem.
```sql
CREATE INDEX ix_data_cliente
    ON acessos (acessado_em, cliente_id);

SELECT * FROM acessos
WHERE cliente_id = 42;
```
- Pergunta: com 1 milhão de linhas, o que o PostgreSQL faz?
- Alternativas: A) Index Scan · B) Lê a tabela inteira (Seq Scan) · C) Index Only Scan · D) Erro
- Resposta: **B** (conferido no PostgreSQL 16)
- Explicação: é como uma lista telefônica ordenada por sobrenome: achar todos os "Silva" é fácil; achar todo mundo chamado "Ana" exige ler tudo. A coluna mais usada sozinha no filtro vem primeiro.

### D17 · Guia 4 · Caracteres não são bytes
- Gancho: Seu servidor manda o texto cortado e com um caractere quebrado no fim. Por quê?
```csharp
using System.Text;

var corpo = "Olá do servidor feito à mão!";
Console.WriteLine(corpo.Length);   // 28
Console.WriteLine(
    Encoding.UTF8.GetBytes(corpo).Length); // ?
```
- Alternativas: A) 28 · B) 31 · C) 56 · D) 29
- Resposta: **B** (conferido)
- Explicação: em UTF-8, "a" ocupa 1 byte, mas "á", "à" e "ã" ocupam 2 cada. O `Content-Length` do HTTP é em bytes; usar `.Length` do texto corta a resposta.

### D18 · Guia 4 · Quem bloqueia o CORS
- Gancho: O erro de CORS é o mais mal-entendido da web.
```text
Página:   http://localhost:3000
fetch  -> http://localhost:8080/hora

Console: blocked by CORS policy
```
- Pergunta: quem bloqueou a chamada?
- Alternativas: A) O servidor da porta 8080 · B) O navegador · C) O firewall · D) O sistema operacional
- Resposta: **B**
- Explicação: a requisição chega ao servidor e é respondida. Quem bloqueia é o navegador, na volta, porque faltou o header `Access-Control-Allow-Origin`. Por isso o curl nunca é bloqueado.

### D19 · Guia 4 · 404 ou 405?
- Gancho: "Não existe" e "existe, mas não desse jeito" são erros diferentes.
```text
GET    /hora  -> 200 OK
DELETE /hora  -> ?
```
- Pergunta: a rota `/hora` só aceita GET. O que o servidor deve responder ao DELETE?
- Alternativas: A) 404 · B) 405 · C) 400 · D) 500
- Resposta: **B** (405 Method Not Allowed)
- Explicação: o caminho existe, o método não. A especificação do HTTP pede ainda o header `Allow: GET` na resposta.

### D20 · Guia 5 · Fibonacci de livro
- Gancho: Três linhas de código, dezenas de bilhões de chamadas.
```csharp
long Fib(int n) =>
    n < 2 ? n : Fib(n - 1) + Fib(n - 2);

Console.WriteLine(Fib(50));
```
- Pergunta: quantas vezes `Fib` é chamada até imprimir?
- Alternativas: A) 50 · B) Cerca de 2.500 · C) Cerca de 1 milhão · D) Cerca de 40 bilhões
- Resposta: **D** (40.730.022.147 chamadas, conferido)
- Explicação: a versão recursiva recalcula os mesmos valores sem parar e é O(2ⁿ). Guardar só os dois últimos valores resolve em O(n).

### D21 · Guia 5 · O maior que deu zero
- Gancho: Passou em todos os seus testes. Até chegar um número negativo.
```csharp
int Maior(int[] v)
{
    int maior = 0;
    foreach (var n in v)
        if (n > maior) maior = n;
    return maior;
}
Console.WriteLine(Maior(new[] { -5, -2, -9 }));
```
- Alternativas: A) -2 · B) 0 · C) -9 · D) Exceção
- Resposta: **B**
- Explicação: começar com `maior = 0` falha quando todos os números são negativos. Comece pelo primeiro item da lista.

### D22 · Guia 5 · O teste do "abba"
- Gancho: Um teste de 4 letras derruba metade das soluções.
- Pergunta: qual o tamanho do maior trecho contínuo de "abba" sem letras repetidas?
- Alternativas: A) 1 · B) 2 · C) 3 · D) 4
- Resposta: **B** ("ab" ou "ba")
- Explicação: na janela deslizante, quando o último "a" chega, o primeiro "a" já ficou fora da janela e não conta mais como repetição. Quem esquece essa checagem responde errado.

### D23 · Guia 5 · O bug da busca binária
- Gancho: Um bug que ficou anos escondido em bibliotecas famosas.
```csharp
// A
int meio = (inicio + fim) / 2;
// B
int meio = inicio + (fim - inicio) / 2;
```
- Pergunta: qual linha quebra com listas gigantes?
- Alternativas: A) A · B) B · C) As duas · D) Nenhuma
- Resposta: **A**
- Explicação: `inicio + fim` pode passar do limite do `int` e virar um número negativo. A versão B nunca soma além do tamanho da lista.

### D24 · Guia 5 · Two Sum
- Gancho: O exercício mais pedido em entrevistas do mundo.
- Pergunta: achar dois números que somam um alvo com dois laços custa O(n²). Usando um `Dictionary`, quanto cai?
- Alternativas: A) O(n log n) · B) O(n) · C) O(1) · D) O(log n)
- Resposta: **B**
- Explicação: para cada número, pergunte "quanto falta para o alvo?" e procure essa falta no dicionário, em O(1).

### D25 · Guia 5 · Texto com +=
- Gancho: Parece inofensivo, mas fica quadrático.
```csharp
var texto = "";
for (int i = 0; i < n; i++)
    texto += letras[i];
```
- Pergunta: quanto custa montar o texto assim?
- Alternativas: A) O(n) · B) O(n²) · C) O(log n) · D) O(1)
- Resposta: **B**
- Explicação: cada `+=` copia a string inteira. Use `StringBuilder` ou monte um `char[]`.

---

## Dicas (sexta, carrossel)

| ID | Guia | Tema | Slides |
| --- | --- | --- | --- |
| T01 | 1 | Ler um stack trace em 30 segundos | Tipo · mensagem · primeira linha do SEU projeto · InnerException até o último `--->` |
| T02 | 1 | Breakpoint condicional e logpoint | Pare só no pedido 4.832 · logpoint = `Console.WriteLine` que não precisa apagar |
| T03 | 1 | Parar o depurador quando a exceção nasce | Visual Studio: Exception Settings · VS Code: All Exceptions |
| T04 | 1 | 4 regras de log | Marcadores `{Campo}` · exceção inteira · nada de senha/CPF · registre decisões |
| T05 | 1 | git bisect acha o commit culpado | start · bad · good · teste · reset |
| T06 | 1 | Pesquise como dev raiz | Erro em inglês, entre aspas, sem nomes do seu projeto |
| T07 | 2 | Singleton, Scoped e Transient | Relógio da parede · comanda do restaurante · copo descartável |
| T08 | 2 | Nunca devolva o stack trace | Middleware com `try/catch` + código de rastreio |
| T09 | 3 | A ordem em que o banco lê sua consulta | FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT |
| T10 | 3 | Um índice: de 34 ms para 0,3 ms | No teste do guia, com 1 milhão de linhas · índice não é de graça |
| T11 | 3 | Chave estrangeira sem índice e N+1 | No PostgreSQL, FK não ganha índice automático · 101 idas ao banco |
| T12 | 4 | HTTP é texto | A requisição e a resposta cruas, linha por linha |
| T13 | 4 | Por que o navegador faz 2 requisições | O pedido do `favicon.ico` e os 404 nos logs |
| T14 | 5 | Os 6 passos de uma entrevista técnica | Pergunte · exemplos à mão · força bruta · melhore · narre · teste |
| T15 | 5 | Big O em uma imagem | O(1) a O(n²) com os passos para 1 milhão de itens |
| T16 | 5 | Custo amortizado | Fila com duas pilhas: O(1) em média |

## Venda e bastidores (sexta)

| ID | Tema | Observação |
| --- | --- | --- |
| V01 | A IA escreve; você precisa saber se está certo | A tese do pacote e a regra de ouro: IA desligada durante o treino |
| V02 | Por que criei o Dev Raiz | Fora da Fila: só entra se o Matheus quiser contar a história dele |
| V03 | Lançamento: o que tem nos 5 guias | Tabela dos guias + cupom + link |
| V04 | Perguntas e respostas | É para iniciante? Tem código? Serve com .NET 10 e SQL Server? |
| V05 | Últimos dias do cupom | Só se o cupom estiver mesmo acabando |
| V06 | Plano de 4 semanas | Um guia por semana, com o tempo de cada um |

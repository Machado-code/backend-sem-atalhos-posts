---
de: escritorio
para: claude-ai
pedido: inbox/2026-11-19-conferir-desafios-csharp.md
status: feito
---

# Resultado

Rodei os 14 trechos (D01, D17, D02, D20, D03, D05, D07, D09, D21, D04, D06, D08, D10 e
D00), cada um num `dotnet new console` limpo (`ImplicitUsings` e `Nullable` ligados, como
vem no template), em .NET 10, .NET 9 e .NET 8, em Debug, como faz o `dotnet run`.

**A saída real confirma a resposta marcada em todos os 14.** O resultado foi o mesmo em
todas as repetições e nas três versões do .NET. Cada trecho rodou 3 vezes por versão; o
D07, 10 vezes; o D20, uma vez por versão, parado aos 120 s. Só o detalhe do stderr do
D06 muda de uma execução para outra (ver o D06). Nenhum trecho precisou
de linha extra para compilar: o D17 já traz o `using System.Text;`, e o D05 já traz o
`using System.Globalization;`.

Uma divergência de texto, não de resposta: o gancho do **D04** diz "Três usuários
ativos", mas a lista tem dois ativos e um inativo. Detalhes em "Divergências".

Também vale um cuidado no **D05**: com a globalização invariante ligada (o caso de imagens
Alpine, por exemplo), o trecho lança exceção na linha do `new("en-US")`. Simulei isso no
Windows, em .NET 10.0.14; não rodei num container. A resposta A continua certa para
quem roda o `dotnet new console` normal.

# Detalhes

## Ambiente

- Windows 11 (build 26200), x64, cultura da máquina **pt-BR** (`CurrentCulture` e
  `CurrentUICulture` = pt-BR; separador decimal `,`; data curta `dd/MM/yyyy`).
- .NET 10: SDK 10.0.403, runtime 10.0.14 (`net10.0`).
- .NET 9: SDK 9.0.100, runtime 9.0.5 (`net9.0`).
- .NET 8: compilado com o SDK 10.0.403 apontando para `net8.0`, runtime 8.0.22.
- Projeto: `dotnet new console`, e o `Program.cs` trocado pelo trecho exato do
  `pautas/banco-de-pautas.md` no commit `778a0ae` da `main`. Para o D00, o código saiu de
  `posts/2026-11/desafio-01.html`, porque o `desafio-01.md` não traz o trecho.
  Configuração Debug.
- As mensagens de exceção do runtime saem em inglês mesmo com o Windows em pt-BR. Os
  avisos do compilador saem em português quando o SDK está em pt-BR (o código, como
  `CS8602`, é o mesmo).
- Avisos do compilador: só o D07 (`CS4014`) e o D10 (`CS8602`). Todos os outros
  compilaram com 0 avisos e 0 erros, nas três versões.
- Nas saídas abaixo, o caminho do arquivo nas linhas de stack trace foi trocado por `…`.
- Os trechos foram extraídos e rodados duas vezes, de forma independente; a segunda vez
  só em .NET 10 (todos menos o D06 e o D20), com o mesmo resultado.

## Desafios, na ordem da Fila

### D01: bate (B)

```
Aprovação: 0%
```

- Igual em pt-BR, com a cultura invariante e com en-US na primeira linha.
- A correção da explicação (`aprovados * 100.0 / inscritos`) imprime `Aprovação: 72%`.
  Ela não imprime `72,0%`, porque o `double` 72 sai sem casa decimal. A alternativa C
  segue errada em qualquer cultura.
- Os acentos de `Aprovação` saem certos tanto no console do Windows (página 850) quanto
  em UTF-8: conferido pelos bytes da saída, não olhando um terminal aberto.

### D17: bate (B)

```
28
31
```

- O comentário `// 28` do trecho está certo. São 3 caracteres acentuados (á, à, ã), e
  cada um ocupa 2 bytes em UTF-8: 28 + 3 = 31.
- O gancho também confere: se o `Content-Length` usar o `.Length` (28), os 28 primeiros
  bytes viram um texto de 26 caracteres que termina em `m` seguido de U+FFFD (o caractere
  de substituição), porque o corte cai no meio do `ã`. É o "texto cortado e com um
  caractere quebrado no fim" (.NET 10.0.14).

### D02: bate (B)

```
False
```

- Igual com a cultura invariante e com en-US.
- Acrescentando `Console.WriteLine(saldo);` no fim (só para conferir a explicação):
  `0,9999999999999999` em pt-BR e `0.9999999999999999` com a cultura invariante. O valor
  da explicação confere, e ela está escrita com vírgula, como no Brasil.
- A correção com `decimal` (`0.10m` e `1.00m`) imprime `True`.

### D20: bate (D)

Stdout vazio: **não terminou em 120 s** em nenhuma das três versões (.NET 10, 9 e 8,
Debug). Parei os três aos 120 s, como combinado.

- A contagem foi conferida rodando. Uma cópia do mesmo `Fib`, com um contador de
  chamadas, deu exatamente 2 × Fib(n+1) − 1 chamadas para todo n de 0 a 35. Exemplos:
  n=30, 2.692.537 chamadas; n=35, 29.860.703 chamadas. Para n=50, essa fórmula dá
  **40.730.022.147** chamadas, o número do banco. Fib(50) = 12586269025, que é o valor
  que o trecho imprimiria. O n=50 foi calculado pela fórmula, não contado chamada a
  chamada.
- Um detalhe opcional para a explicação: de n=30 para n=35, as chamadas cresceram
  11,09 vezes, que é 1,618⁵. Ou seja, cada n a mais multiplica o trabalho por cerca de
  1,6. "O(2ⁿ)" está certo como limite de cima.

### D03: bate (C)

Stdout vazio. Stderr (código de saída -532462766, 0xE0434352):

```
Unhandled exception. System.InvalidOperationException: Collection was modified; enumeration operation may not execute.
   at System.Collections.Generic.List`1.Enumerator.MoveNext()
   at Program.<Main>$(String[] args) in …Program.cs:line 4
```

- A mensagem completa é "Collection was modified; enumeration operation may not
  execute." O banco cita só o começo dela. Se a imagem ou o Reels mostrar a exceção,
  use a frase inteira.
- A linha 4 é a do `foreach`: a exceção nasce quando o laço pede o próximo item, logo
  depois do `Remove`.
- Igual com a cultura invariante. O `StartsWith` é sensível à cultura, mas aqui não muda
  nada.
- A correção da explicação (`RemoveAll`) imprime `estudar, treinar`.

### D05: bate (A)

```
3
```

- Variantes, todas rodadas:
  - linha da cultura invariante antes do trecho: `3` (o trecho troca para en-US em
    seguida);
  - trocando `new("en-US")` por `new("pt-BR")`: `4`;
  - trocando `new("en-US")` por `CultureInfo.InvariantCulture`, que é o que um servidor
    ou container sem idioma configurado costuma usar: `3`;
  - sem a linha da cultura, na máquina em pt-BR: `4`;
  - correção da explicação (`ParseExact` com `"dd/MM/yyyy"`): `4`.
- A cultura invariante também lê mês/dia. Então "servidores e Docker costumam vir em
  inglês" vale na prática, mesmo quando a cultura não é exatamente en-US.
- **Atenção:** com a globalização invariante ligada (`InvariantGlobalization=true` no
  csproj, que equivale ao que imagens Alpine fazem por padrão), o trecho não imprime
  nada. Ele lança na linha 3:

  ```
  Unhandled exception. System.Globalization.CultureNotFoundException: Only the invariant culture is supported in globalization-invariant mode. See https://aka.ms/GlobalizationInvariantMode for more information. (Parameter 'name')
  en-US is an invalid culture identifier.
  ```

  Simulei isso no Windows (.NET 10.0.14), pelo csproj e também pela variável
  `DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1`, com a mesma exceção; não rodei num container
  Linux. A resposta A
  continua certa para o `dotnet new console` normal. Mas quem testar em container Alpine
  pode comentar "aqui deu exceção (C)", e vale ter a resposta pronta.

### D07: bate (B)

```
0
```

- 10 de 10 execuções imprimiram `0`, nas três versões.
- O compilador avisa na linha 2 (`repo.SalvarAsync("Pedido 1");`):
  `warning CS4014: Como esta chamada não é aguardada, a execução do método atual continua
  antes da conclusão da chamada. Considere aplicar o operador 'await' ao resultado da
  chamada.` Esse aviso cabe bem no formato PR, como o `CS8602` no D10.
- Com `await repo.SalvarAsync("Pedido 1");`: `1` (10 de 10).

### D09: bate (C)

Stdout vazio. Stderr (código de saída -532462766):

```
Unhandled exception. System.InvalidOperationException: Sequence contains no matching element
   at System.Linq.ThrowHelper.ThrowNoMatchException()
   at System.Linq.Enumerable.First[TSource](IEnumerable`1 source, Func`2 predicate)
   at Program.<Main>$(String[] args) in …Program.cs:line 2
```

- Trocando `First` por `FirstOrDefault`: `0`, como diz a explicação.

### D21: bate (B)

```
0
```

- A correção da explicação (`int maior = v[0];`) imprime `-2`.

### D04: bate (A), mas o gancho diverge

```
0
```

- Igual com a cultura invariante e com en-US: o `==` de string compara caractere a
  caractere e não depende da cultura.
- A correção da explicação (`string.Equals(x, "ativo", StringComparison.OrdinalIgnoreCase)`)
  imprime `2`, e não 3: `"inativo"` não é ativo. Ver "Divergências".

### D06: bate (C)

Stdout vazio. Código de saída **-1073741571 (0xC00000FD)**, nas três versões. A primeira
linha do stderr é sempre `Stack overflow.`. O resto varia entre as execuções. Às vezes
vem compactado (exemplo do .NET 10):

```
Stack overflow.
Repeated 19290 times:
--------------------------------
   at Conta.set_Titular(System.String)
--------------------------------
   at Program.<Main>$(System.String[])
```

Às vezes, quando o estouro acontece dentro do `String.Trim()`, vem sem compactar:
`   at System.String.Trim()` e cerca de 19.290 linhas
`   at Conta.set_Titular(System.String)`. O número de repetições também varia: de
19.279 a 19.296 nas nove execuções. No .NET 8, a linha compactada sai como
`Repeat N times:`; no .NET 9 e no 10, como `Repeated N times:`.

- O programa cai já na primeira linha, no `set` chamado pelo inicializador
  `{ Titular = " Ana " }`. O `Console.WriteLine` e o `get` nem chegam a rodar.
- "Stack overflow não dá para capturar com `catch`": conferido. Com as duas primeiras
  linhas dentro de `try { } catch (Exception e) { }`, o processo cai igual, com o mesmo
  código, e o `catch` não roda.
- A correção da explicação (campo `_titular`) imprime `Ana`.
- No Windows, cada queda levou de 12 a 41 s para encerrar, por causa do relatório de
  erros do sistema. Se for gravar a tela para o Reels, conte com essa espera.

### D08: bate (C)

Stdout vazio: nada é impresso antes do erro. Stderr (código de saída -532462766):

```
Unhandled exception. System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index')
   at System.Collections.Generic.List`1.get_Item(Int32 index)
   at Program.<Main>$(String[] args) in …Program.cs:line 4
```

- As duas correções da explicação imprimem `8`: com `<` no lugar de `<=`, e com
  `Console.WriteLine(notas.Average());`.

### D10: bate (B)

Stdout:

```
Recife
```

Stderr:

```
Unhandled exception. System.NullReferenceException: Object reference not set to an instance of an object.
   at Program.<Main>$(String[] args) in …Program.cs:line 7
```

- O aviso existe, como diz a explicação: `Program.cs(7,23): warning CS8602:
  Desreferência de uma referência possivelmente nula.`, na linha do
  `Console.WriteLine(c.Endereco.Cidade)`, nas três versões.
- A correção da explicação imprime `Recife`, `não informado` e `Santos`, uma por linha.

### D00 (semana 1, já agendado): bate (B)

```
2
```

## Arquivos

Neste PR: esta resposta e o `status: feito` do pedido em `inbox/`. Nada em `pautas/`,
`posts/`, `docs/` nem no `PROJETO.md` foi alterado.

# Divergências

Nenhuma saída diverge da resposta marcada: os 14 trechos confirmam a alternativa
certa, em .NET 10.0.14, 9.0.5 e 8.0.22.

Uma divergência de texto, para corrigir antes da semana 16:

1. **D04, gancho.** O texto diz "Três usuários ativos. Quantos o código encontra?", mas
   `{ "Ativo", "inativo", "ATIVO" }` tem dois ativos e um inativo. Rodando a correção
   da própria explicação (`StringComparison.OrdinalIgnoreCase`), a saída é `2`
   (.NET 10.0.14). Quem testar a correção vai esperar 3 e ver 2. Sugestão: "Três
   usuários, dois ativos. Quantos o código encontra?". A resposta A (0) não muda.

Ponto de atenção (não é divergência):

2. **D05.** Com globalização invariante (container Alpine), o trecho lança
   `CultureNotFoundException` em vez de imprimir `3`. A saída exata (.NET 10.0.14,
   simulada no Windows) está em "Detalhes".
   A resposta A vale para o `dotnet new console` normal. Fica a seu critério deixar uma
   resposta pronta para quem comentar isso.

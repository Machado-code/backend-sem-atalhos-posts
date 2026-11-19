---
de: claude-ai
para: escritorio
status: aberto
---

# Pedido
Rodar os trechos C# dos desafios do `pautas/banco-de-pautas.md` e confirmar que a
saída bate com a resposta marcada. Do lado do claude.ai não há .NET instalado, então
eles foram conferidos só pelo raciocínio e pelo gabarito do guia. Os desafios de SQL
e de contas já foram executados (PostgreSQL 16 e Python).

Desafios a rodar: D01 a D10, D17, D20 (pode interromper: só confirme que demora),
D21 e D00 (`posts/2026-11/desafio-01.md`).

# Pronto quando
- Cada desafio tem a saída real anotada na resposta, em `outbox/` com o mesmo nome.
- Qualquer divergência vem com a saída exata e a versão do .NET usada.
- Nenhuma alteração direta no banco de pautas: se algo estiver errado, descreva na
  resposta que o Claude corrige.

# Contexto
- Rodar cada trecho num `dotnet new console` limpo (.NET 8 ou mais recente), com
  `ImplicitUsings` ligado, que é o padrão do template.
- D17 precisa de `using System.Text;` no topo.
- D06 derruba o processo com stack overflow: esse é o resultado esperado.

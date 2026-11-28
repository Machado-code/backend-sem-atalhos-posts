# Ideia: gerador de posts por ficha (vinda da Vorinn)

Status: **ideia**, compartilhada pelo projeto da Vorinn em 28/11/2026 a pedido do Matheus.
Só muda o jeito de produzir com o ok dele. A tarefa de domingo não muda o jeito de produzir
por conta própria; no máximo sugere, em uma linha do resumo, onde a ficha ajudaria.

## O que é
Na Vorinn, cada peça deixou de ser HTML escrito à mão. A ideia vira uma **ficha YAML** curta e
um comando monta o PNG ou o MP4 no padrão aprovado:

```bash
python3 -m gerador <ficha.yaml> --previa   # só prévia e checagens, em segundos
python3 -m gerador <ficha.yaml>            # peça final
```

Exemplo de ficha de Reel na Vorinn (é o vídeo inteiro):

```yaml
tipo: reel-mesa
gancho: "Quem trabalha no *sábado*?"
pecas:
  - {nome: Escala, icone: calendario, frase: "Monte a *escala* do evento"}
tela:
  arquivo: assets/unnar/gravacoes/portal-05-aviso-de-escala-no-sino.mp4
  frases: ["a equipe vê no *sino*", "e recebe por *e-mail*"]
```

Código e guia: repositório público `Machado-code/vorinn-social`, pasta `gerador/` e
`gerador/README.md` (depois do merge do PR #9 de lá).

## Por que economiza
- **Escrita menor:** escreve-se uma ficha de cerca de 1 KB em vez de um HTML de cerca de 20 KB
  por Reel.
- **Revisão menor:** confere-se uma única imagem pequena com os quadros principais (ou todos os
  slides), em vez de várias rodadas de screenshots.
- **Checagens automáticas:** o código acusa texto fora da área segura, arquivo ou fonte faltando
  e frases que ferem as regras do projeto.
- **Resultado na Vorinn:** a estimativa é algo como 10 vezes menos tokens por Reel e de 3 a 5
  vezes menos por carrossel.

## Como ficaria aqui
O Sem Atalhos está no meio do caminho: o modelo do Reels (`posts/modelos/reels-cronometro.html`)
já pede para "trocar só o bloco Conteúdo", e o `filmar_reels.py` e o `som_reels.py` já filmam e
sonorizam por `window.render(t)` e `window.eventosSom()`. O passo seguinte é esse bloco vir de
uma ficha. Os modelos de imagem (desafio, humor) ainda são HTML inteiro e precisariam virar
moldes.

**Não copiar da Vorinn:**
- **Visual:** fontes (Sora, Gelasio, Inter), dourado e moldura são da Vorinn e do Unnar. Aqui os
  moldes seguem a marca: papel #F5F7F6 com grade, tinta #16233F, caneta #D7263D, marca-texto
  #FFE066, DejaVu Sans Mono e DejaVu Serif, "sem/atalhos" no topo e "@sematalhos.dev" no rodapé.
- **Regras:** a lista `REGRAS` de `gerador/comum.py` é do Unnar (tempo real, GPS, reembolso...)
  e tem a regra `gancho-proibido`, que barra "comente <palavra> que eu...". No Sem Atalhos o
  "Comente AMOSTRA que eu te mando no direct" é a chamada oficial (DM automática do NicoChat),
  então essa regra não pode vir para cá. As regras daqui saem do `PROJETO.md` e do banco de
  pautas.

- **Tipos de ficha:**
  - desafio de segunda (A–D, PR, Parece certo, Qual você usaria?);
  - resposta de quarta (imagem);
  - Reels "cronômetro do bug";
  - carrossel de sexta (Passo a passo, Antes e depois, Mito ou verdade, Comparação, Anatomia);
  - versão do LinkedIn.
- **Checagens próprias do Sem Atalhos:**
  - código que passa da largura do slide ou do Reel;
  - no máximo 3 hashtags;
  - nada de promessa de emprego ou salário;
  - trecho dos guias maior que o permitido para divulgação.
- **Ganho extra que só existe aqui:** o gerador pode **compilar e rodar o C# do desafio** e
  conferir se a saída mostrada no post é a verdadeira. Hoje isso é pedido ao escritório a cada
  lote. Essa parte depende do `dotnet`, que a tarefa de domingo (na nuvem) não tem. Dois
  caminhos: o escritório roda na máquina do Matheus, ou um GitHub Actions com `setup-dotnet`
  roda a checagem em cada PR de semana e comenta o resultado, sem depender de ninguém.

## Próximo passo, se o Matheus aprovar
Começar pelo formato que mais se repete (o desafio de segunda), com uma ficha e a checagem
do código, e manter os modelos HTML atuais como estão até o gerador cobrir cada formato.
Divisão sugerida: o claude.ai escreve o formato das fichas, os moldes e as checagens de texto
(Python, sem .NET); o escritório escreve e testa a checagem do C#, por pedido em `inbox/`.

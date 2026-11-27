# Ideia de formato: "a máquina" (Reels 3D sem voz)

Status: **ideia**, compartilhada pelo projeto da Vorinn em 27/11/2026 a pedido do Matheus.
A tarefa de domingo não cria post neste formato antes do ok dele; no máximo sugere, em
uma linha do resumo, qual pauta da semana caberia aqui.

## De onde veio
Um Reel de outro perfil explicava um processo com uma animação 3D: uma máquina numa mesa
em que cada etapa é uma peça que encaixa num slot numerado, com legenda palavra por
palavra e uma palavra-chave destacada numa caixa de seleção. A Vorinn adaptou para o
Unnar (console com cartuchos "Escala, Confirmação, Check-in, Despesas") e aprovou como
série de quarta.

Exemplo pronto, código e receita (repositório público `Machado-code/vorinn-social`,
pasta `reels/`, depois do merge do PR #8):
- vídeo: `reels/2026-12/reel-02-mesa-de-controle.mp4`
- modelo: `reels/modelos/mesa-de-controle.html`
- receita com as regras técnicas: `reels/modelos/mesa-de-controle.md`

## Por que pode servir ao Sem Atalhos
Transforma um conceito abstrato em objeto que a pessoa vê montar, sem voz e sem rosto.
Funciona melhor para coisas que têm **ordem** ou **partes**, que é muito do que os guias
ensinam.

## Pautas que encaixam
- **O pipeline do ASP.NET Core:** cada middleware é um cartucho que entra na ordem
  (exceções, HTTPS, roteamento, autenticação, autorização, endpoint) e a requisição
  atravessa a máquina. Versão "Parece certo": dois cartuchos trocados de lugar e a
  pergunta "o que quebra?".
- **Ciclo de vida da injeção de dependência:** três máquinas lado a lado (Singleton,
  Scoped, Transient) entregando instâncias.
- **Anatomia de uma requisição HTTP:** método, rota, cabeçalhos e corpo como peças;
  serve para o quadro "Anatomia" da sexta em versão Reel.
- **Post de venda do Dev Raiz:** os 5 guias como 5 cartuchos encaixando na "base do
  dev"; fecha com "Sem IA. Só o método." e a chamada.

## Onde entraria
O Reels de quarta já tem o "cronômetro do bug" (aprovado em 26/11), que serve para bugs e
saídas erradas. "A máquina" serve para conceitos com ordem ou partes, então o lugar
natural é a sexta: versão em Reels de um "Anatomia" ou "Passo a passo", ou um post de
venda (V). Mantém Reels e imagem misturados, sem dois Reels iguais na mesma semana.

## Como adaptar ao Sem Atalhos
- Visual da marca: fundo papel quadriculado claro (#F5F7F6), azul-marinho (#16233F),
  vermelho (#D7263D) para destaque, serifada como nos outros modelos. A palavra-chave da
  legenda fica em vermelho dentro da caixa de seleção.
- Os cartuchos levam o nome da peça (ex.: `UseRouting`) em fonte mono; a etiqueta
  flutuante pode mostrar a linha de código.
- O `scripts/filmar_reels.py` daqui chama `window.render(t)`; o modelo da Vorinn expõe
  `window.seek(t)`. Basta acrescentar `window.render = window.seek;` no fim do HTML.
- Para os efeitos sonoros do `scripts/som_reels.py`, o HTML também precisa expor
  `window.eventosSom()`, com a lista `[segundo, tipo]` (modelo em
  `posts/modelos/reels-cronometro.html`). Um "encaixe" de cartucho pode usar o tipo
  `enter`, e o resultado final, `acerto`.
- Sem voz e sem avatar, como já é regra aqui.

## Lições que já custaram retrabalho na Vorinn
- Não animar `transform` num elemento que usa `transform` para se posicionar em 3D (a
  animação apaga a posição): anime `opacity`, a propriedade `translate` ou um filho.
- Opacidade menor que 1 num grupo `preserve-3d` achata o 3D: esconda com `visibility`.
- Etiquetas de frente para a câmera: depois do `translate3d`, `rotateZ(-θ) rotateX(-φ)`.
- Texto desenhado na tampa ou no chão fica deitado e ilegível: aplique a correção
  `rotate(-θ) scaleY(1/cos φ)`.
- Animação com `fill-mode: both` mostra o quadro 0% antes de começar: brilhos e anéis
  começam em `opacity: 0`.
- Conferir quadros nos momentos mais cheios antes de filmar o vídeo inteiro.

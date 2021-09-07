![Projeto-img](https://user-images.githubusercontent.com/57952324/132383684-ab043b5b-10fc-43e7-ab80-11f02bedc4ea.png)
# Projeto-N1-Parte-1-UAM

### Situação Problema:

Muitos jogos de RPG são baseados em explorar dungeons, ou seja, explorar cavernas,
calabouços, florestas e todo tipo de lugar desconhecido. Hoje você será o líder de uma guilda de heróis!
Como todo bom líder, você deverá guiar os guerreiros através do labirinto.


## Regras

As regras para a travessia do labirinto são bastante simples, toda a guilda começará na
sala 1 e a partir dela pode-se escolher 2 opções diferentes:

1 – Caminho vermelho (ou direita);

2 – Caminho preto (ou esquerda);

Você precisará criar a lógica para fazer com que por meio de interações com o usuário
seja possível avançar pelos caminhos do labirinto. Considere que “o mapa” culto é
idêntico a este:

![Img-mapa](https://user-images.githubusercontent.com/57952324/132383707-94e46173-4bfd-40ec-8f38-d59ee0965378.PNG)

Note que o caminho preto da sala 8 leva à um local desconhecido, isso porque esta
dungeon é controlada por criaturas místicas que dominam o tempo-espaço e criaram
um portal! Toda vez que os personagens escolherem o caminho preto estando na sala
8 é preciso sortear o seu destino.
Podendo ser qualquer sala entre 1, 2, 3, 4 ou 5.


## Restrições do Código:

▪ Os heróis vencem ao chegar na Sala 9;

▪ A sala 6 tem realmente uma única possibilidade;

▪ Os heróis perdem se levarem 7 ou mais interações para chegarem na sala 9;

▪ Cada vez que os heróis escolhem um caminho é considerado 1 interação.

▪ Você precisa utilizar um laço de repetição, podendo ser o comando “while”;

▪ Dentro do laço de repetição você poderá incluir somente UM BLOCO de comando “if”
(com direito a um elif e um else, mas sem outros ifs internos) e NENHUM comando
“switch-case” (os demais comandos não possuem limitação);

▪ Fora do laço de repetição você poderá utilizar quantos comandos precisar.

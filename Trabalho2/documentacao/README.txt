
commit 14h - 01_05, Ilan:

Alterações feitas:

- estrutura de classes do jogo feita já;
- já dá load e monta o jogo com inimigos e elementos sensoriais posicionados;

Observações:

- estrutura de posicionamentos no Maze e do Player ([1,1]) é primeira linha e primeira coluna, igual está no pdf
leia-se matrix na posição (0,0) computacionalmente falando;
- arquivos graphic.py e teste.py foram copiados do stack overflow e foram tentativa de fazer uma interface gráfica rudimentar para teste do jogo. Ainda não foram bem sucedidos. Fiz em Tkinter só para ser mais rápido e descupe a falta de comntário, essa parte foi meio na pressa.

O que falta?

- Terminar de 'ligar' os elementos (o tabuleiro já existe, o player já pode se mover..., mas precisa juntar tudo no jogo propriamente dito ainda, por enquanto disso temos o Loader só, que monta o ambiente de jogo). O problema é que isso meio que está dependendo da interface gráfica pra gente não precisar fazer duas vezes;
- Prolog;
- Inteface gráfica.
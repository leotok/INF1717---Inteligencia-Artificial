
commit 14h - 01_05, Ilan:

Altera��es feitas:

- estrutura de classes do jogo feita j�;
- j� d� load e monta o jogo com inimigos e elementos sensoriais posicionados;

Observa��es:

- estrutura de posicionamentos no Maze e do Player ([1,1]) � primeira linha e primeira coluna, igual est� no pdf
leia-se matrix na posi��o (0,0) computacionalmente falando;
- arquivos graphic.py e teste.py foram copiados do stack overflow e foram tentativa de fazer uma interface gr�fica rudimentar para teste do jogo. Ainda n�o foram bem sucedidos. Fiz em Tkinter s� para ser mais r�pido e descupe a falta de comnt�rio, essa parte foi meio na pressa.

O que falta?

- Terminar de 'ligar' os elementos (o tabuleiro j� existe, o player j� pode se mover..., mas precisa juntar tudo no jogo propriamente dito ainda, por enquanto disso temos o Loader s�, que monta o ambiente de jogo). O problema � que isso meio que est� dependendo da interface gr�fica pra gente n�o precisar fazer duas vezes;
- Prolog;
- Inteface gr�fica.
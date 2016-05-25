:-dynamic posicao/2.
:-dynamic olhar/1.
:-dynamic ouro_bolsa/1.
:-dynamic vida/1.
:-dynamic custo/1.
:-dynamic monstrosDerrotados/1.

ouro_bolsa(0).
vida(100).
custo(0).
monstrosDerrotados(0).

posicao(1,1).
olhar(norte).

perde_vida(X) :- vida(Z), Y is Z - X, retract(vida(_)), assert(vida(Y)).
aumenta_custo(X) :- custo(Z), Y is Z + X, retract(custo(_)), assert(custo(Y)).
pega_ouro(X) :-  ouro_bolsa(Z), Y is Z + X, retract(ouro(_)), assert(ouro(Y)).


virar_direita :- olhar(norte), retract(olhar(_)), assert(olhar(leste)),!.
virar_direita :- olhar(oeste), retract(olhar(_)), assert(olhar(norte)),!.
virar_direita :- olhar(sul), retract(olhar(_)), assert(olhar(oeste)),!.
virar_direita :- olhar(leste), retract(olhar(_)), assert(olhar(sul)),!.

andar :- posicao(X,Y),  Y < 25, olhar(norte), Y_new is Y + 1,
         retract(posicao(_,_)), assert(posicao(X, Y_new)),!.

andar :- posicao(X,Y),  Y > 1, olhar(sul), Y_new is Y - 1,
         retract(posicao(_,_)), assert(posicao(X, Y_new)),!.

andar :- posicao(X,Y),  X < 25, olhar(leste), X_new is X + 1,
         retract(posicao(_,_)), assert(posicao(X_new, Y)),!.

andar :- posicao(X,Y),  X > 1, olhar(oeste), X_new is X - 1,
         retract(posicao(_,_)), assert(posicao(X_new, Y)),!.

adjacente(X, Y) :- posicao(PX, Y, _), PX < 3, X is PX + 1.
adjacente(X, Y) :- posicao(PX, Y, _), PX > 1, X is PX - 1.
adjacente(X, Y) :- posicao(X, PY, _), PY < 3, Y is PY + 1.
adjacente(X, Y) :- posicao(X, PY, _), PY > 1, Y is PY - 1.


%ande_para(X, Y) :- retract(posicao(_,_)), assert(posicao(X, Y)).

executa_acao(X) :- X = andar.
executa_acao(X) :- X = correr.
executa_acao(X) :- X = atacar.
executa_acao(X) :- X = observar.
executa_acao(X) :- X = pegar_item.
executa_acao(X) :- X = fugir.

%cheiro, barulho,.

cheira_mal(X, Y) :- consult("map.pl"), posicao(X,Y), PX is X + 1, tile(PX,Y,[monstro|_]).
cheira_mal(X, Y) :- consult("map.pl"), posicao(X,Y), PX is X - 1, tile(PX,Y,[monstro|_]).
cheira_mal(X, Y) :- consult("map.pl"), posicao(X,Y), PY is Y + 1, tile(X,PY,[monstro|_]).
cheira_mal(X, Y) :- consult("map.pl"), posicao(X,Y), PY is Y - 1, tile(X,PY,[monstro|_]).


brilha(X, Y) :- consult("map.pl"), posicao(X, Y), tile(X,Y,[_,ouro|_]).














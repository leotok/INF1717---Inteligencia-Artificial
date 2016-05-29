%% Outros arquivos prolog

:- ensure_loaded('map.pl').
:- ensure_loaded('map_observ.pl').

%% Dynamics

:-dynamic posicao/3.
:-dynamic visitado/2.

:-dynamic ouro_bolsa/1.
:-dynamic vida/1.
:-dynamic custo/1.
:-dynamic monstrosDerrotados/1.

:-dynamic melhor_acao/3.

%% map_observ
:-dynamic tile_obs/3.

%% map
:-dynamic tile/3.

posicao(1,1, norte).

ouro_bolsa(0).
vida(100).
custo(0).
monstrosDerrotados(0).



perde_vida(X) :- vida(Z), Y is Z - X, retract(vida(_)), assert(vida(Y)).
aumenta_custo(X) :- custo(Z), Y is Z + X, retract(custo(_)), assert(custo(Y)).
pegar_ouro :-  ouro_bolsa(Z), Y is Z + 1, retract(ouro_bolsa(_)), assert(ouro_bolsa(Y)).
pegar_power_up :- vida(Z), Y is Z + 50, retract(vida(_)), assert(vida(Y)). 

virar_direita :- posicao(X,Y, norte), retract(posicao(_,_,_)), assert(posicao(X, Y, leste)),!.
virar_direita :- posicao(X,Y, oeste), retract(posicao(_,_,_)), assert(posicao(X, Y, norte)),!.
virar_direita :- posicao(X,Y, sul), retract(posicao(_,_,_)), assert(posicao(X, Y, oeste)),!.
virar_direita :- posicao(X,Y, leste), retract(posicao(_,_,_)), assert(posicao(X, Y, sul)),!.

andar :- posicao(X,Y,P), P = norte,  Y < 12, YY is Y + 1,
         retract(posicao(_,_,_)), assert(posicao(X, YY, P)),!.

andar :- posicao(X,Y,P), P = sul,  Y > 1, YY is Y - 1,
         retract(posicao(_,_,_)), assert(posicao(X, YY, P)),!.

andar :- posicao(X,Y,P), P = leste,  X < 12, XX is X + 1,
         retract(posicao(_,_,_)), assert(posicao(XX, Y, P)),!.

andar :- posicao(X,Y,P), P = oeste,  X > 1, XX is X - 1,
         retract(posicao(_,_,_)), assert(posicao(XX, Y, P)),!.

adjacente(X, Y) :- posicao(PX, Y, _), PX < 3, X is PX + 1.
adjacente(X, Y) :- posicao(PX, Y, _), PX > 1, X is PX - 1.
adjacente(X, Y) :- posicao(X, PY, _), PY < 3, Y is PY + 1.
adjacente(X, Y) :- posicao(X, PY, _), PY > 1, Y is PY - 1.


%%  MELHOR ACAO

melhor_acao(A,X,Y) :-  posicao(X,Y,_), tile(X,Y,[ouro]), A = pegar_ouro, pegar_ouro,
					   retract(tile(X,Y,_)), assert(tile(X,Y,[])), !.
melhor_acao(A,X,Y) :-  posicao(X,Y,_), tile(X,Y,[power_up]), vida(V), V < 50, A = pegar_power_up, pegar_power_up, 
					   retract(tile(X,Y,_)), assert(tile(X,Y,[])), !.

melhor_acao(A,X,Y) :-  posicao(X,Y,_), A = nada_pra_fazer_vou_me_envolver_com_as_fans.

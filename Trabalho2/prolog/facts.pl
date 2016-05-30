%% Outros arquivos prolog

:- ensure_loaded('map.pl').
:- ensure_loaded('map_observ.pl').

%% Dynamics

:-dynamic posicao/3.
:-dynamic seguro/2.
:-dynamic conhecido/2.

:-dynamic ouro_bolsa/1.
:-dynamic vida/1.
:-dynamic custo/1.
:-dynamic monstrosDerrotados/1.

:-dynamic melhor_acao/3.

%% map_observ
:-dynamic tile_obs/3.

%% map
:-dynamic tile/3.

posicao(12,1, leste).
seguro(12,1).

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

andar :- posicao(X,Y,P), P = norte,  X > 1, XX is X - 1,
         retract(posicao(_,_,_)), assert(posicao(XX, Y, P)),!.

andar :- posicao(X,Y,P), P = sul,  X < 12, XX is X + 1,
         retract(posicao(_,_,_)), assert(posicao(XX, Y, P)),!.

andar :- posicao(X,Y,P), P = leste,  Y < 12, YY is Y + 1,
         retract(posicao(_,_,_)), assert(posicao(X, YY, P)),!.

andar :- posicao(X,Y,P), P = oeste,  Y > 1, YY is Y - 1,
         retract(posicao(_,_,_)), assert(posicao(X, YY, P)),!.

adjacente(X, Y) :- posicao(PX, Y, _), PX < 12, X is PX + 1.
adjacente(X, Y) :- posicao(PX, Y, _), PX > 1, X is PX - 1.
adjacente(X, Y) :- posicao(X, PY, _), PY < 12, Y is PY + 1.
adjacente(X, Y) :- posicao(X, PY, _), PY > 1, Y is PY - 1.

adjacente_a(X, Y, I, J) :-  X < 12, I is X + 1, J is Y.
adjacente_a(X, Y, I, J) :-  X > 1, I is X - 1, J is Y.
adjacente_a(X, Y, I, J) :-  Y < 12, J is Y + 1, I is X.
adjacente_a(X, Y, I, J) :-  Y > 1, J is Y - 1, I is X.


sentidos(S) :- posicao(X,Y,_), tile(X,Y,[ouro]), S = brilho, !.
sentidos(S) :- posicao(X,Y,_), tile(X,Y,[power_up]), S = power_up, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[buraco]),  tile(I,J,[teletransporte]), tile(I,J,[inimigo_forte]),
			   tile(I,J,[inimigo_fraco]), S = brisa_flash_cheiro, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[buraco]),  tile(I,J,[teletransporte]), tile(I,J,[inimigo_forte]),
			   S = brisa_flash_cheiro, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[buraco]),  tile(I,J,[teletransporte]), tile(I,J,[inimigo_fraco]),
			   S = brisa_flash_cheiro, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[buraco]),  tile(I,J,[teletransporte]), S = brisa_flash, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[buraco]),  tile(I,J,[inimigo_forte]), S = brisa_cheiro, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[teletransporte]),  tile(I,J,[inimigo_fraco]), S = flash_cheiro, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[teletransporte]),  tile(I,J,[inimigo_forte]), S = flash_cheiro, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[buraco]), S = brisa, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[inimigo_forte]), S = cheiro, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[inimigo_fraco]), S = cheiro, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[teletransporte]), S = flash, !.
sentidos(S) :- adjacente(I,J), tile(I,J,[]), S = nada, !.

observar :- sentidos(S), S = brilho, posicao(I,J,_), retract(tile_obs(I,J,_)), assert(tile_obs(I,J,[S])), !.
observar :- sentidos(S), S = power_up, posicao(I,J,_), retract(tile_obs(I,J,_)), assert(tile_obs(I,J,[S])), !.
observar :- sentidos(S), adjacente(I,J), \+ seguro(I,J), S = brisa, tile_obs(I,J,[brisa]), 
			assert(conhecido(I,J)), retract(tile_obs(I,J,_)), assert(tile_obs(I,J,[buraco])).
observar :- sentidos(S), adjacente(I,J), \+ seguro(I,J), S = cheiro, tile_obs(I,J,[cheiro]), 
			assert(conhecido(I,J)), retract(tile_obs(I,J,_)), assert(tile_obs(I,J,[inimigo])).
observar :- sentidos(S), adjacente(I,J), \+ seguro(I,J), \+ conhecido(I,J), retract(tile_obs(I,J,_)), assert(tile_obs(I,J,[S])).


marcar_seguro_em_volta(X,Y) :- adjacente_a(X,Y,I,J), adjacente_a(I,J, II,JJ), tile_obs(II,JJ,[brisa]), assert(seguro(II,JJ)), 
							   retract(tile_obs(II,JJ,_)), assert(tile_obs(II,JJ,[nada])) .
marcar_seguro_em_volta(X,Y) :- adjacente_a(X,Y,I,J), adjacente_a(I,J, II,JJ), tile_obs(II,JJ,[cheiro]), assert(seguro(II,JJ)), 
							   retract(tile_obs(II,JJ,_)), assert(tile_obs(II,JJ,[nada])) .

%%  MELHOR ACAO

%% pegar ouro e power_up
melhor_acao(A,X,Y,D) :-  observar, posicao(X,Y,D), tile_obs(X,Y, [brilho]), A = pegar_ouro, pegar_ouro, aumenta_custo(1000),
					     retract(tile_obs(X,Y,_)),retract(tile(X,Y,_)), assert(tile_obs(X,Y,[nada])), assert(tile(X,Y,[])), !.
melhor_acao(A,X,Y,D) :-  posicao(X,Y,D), tile_obs(X,Y,[power_up]), vida(V), V < 50, A = pegar_power_up, pegar_power_up,
						 aumenta_custo(-1), retract(tile_obs(X,Y,_)), assert(tile_obs(X,Y,[nada])), !.

%% andar
melhor_acao(A,X,Y,D) :-  observar, posicao(X,Y,D), D = leste, YY is Y + 1, tile_obs(X,YY,[nada]) ,A = andar, andar,
						 aumenta_custo(-1), assert(seguro(X, YY)), !.
melhor_acao(A,X,Y,D) :-  observar, posicao(X,Y,D), D = norte, XX is X - 1, tile_obs(XX,Y,[nada]) ,A = andar, andar,
						 aumenta_custo(-1), assert(seguro(XX, Y)), !.
melhor_acao(A,X,Y,D) :-  observar, posicao(X,Y,D), D = oeste, YY is Y - 1, tile_obs(X,YY,[nada]) ,A = andar, andar, 
						 aumenta_custo(-1), assert(seguro(X, YY)), !.
melhor_acao(A,X,Y,D) :-  observar, posicao(X,Y,D), D = sul, XX is X + 1, tile_obs(XX,Y,[nada]) ,A = andar, andar, 
						 aumenta_custo(-1), assert(seguro(XX, Y)), !.
melhor_acao(A,X,Y,D) :-  posicao(X,Y,D), virar_direita, virar_direita, andar, virar_direita, A = voltar_tentar_outro_caminho, aumenta_custo(-1), !.

%% nada para fazer
melhor_acao(A,X,Y,D) :-  posicao(X,Y,D), A = nada_pra_fazer_vou_me_envolver_com_as_fans.

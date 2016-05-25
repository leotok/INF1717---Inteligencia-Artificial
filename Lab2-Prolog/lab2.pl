%%  aula 1 prolog

pertence([B | _], B) :- !.
pertence([H | T], B) :- B \= H, pertence(T, B).

ultimo_elemento([H | []], H) :- !.
ultimo_elemento([_ | T], U) :- ultimo_elemento(T, U).

primeiro([H | _], H).


copia([], []).
copia([H | T], [H | L]) :- copia(T, L).


remove_duplicadas([], []).
remove_duplicadas([H | T], [H | L]) :- remove_duplicadas(T, L) , \+ pertence(L, H), !.
remove_duplicadas([_ | T],  L) :- remove_duplicadas(T, L) , pertence(L, H).

%% aula 2 prolog

node(v1).
node(v2).
node(v3).
node(v4).
node(v5).

edge(v1,v2,1).
edge(v1,v3,1).
edge(v2,v3,1).
edge(v3,v5,1).
edge(v2,v4,1).
edge(v4,v5,1).

path(V,V).
path(F,T) :- edge(F,Z), path(Z,T).

path(V,V,[]).
path(F,T, [Z|J]) :- edge(F,Z), path(Z,T,J).

path(V,V,[],0).
path(F,T, [Z|J], Total) :- edge(F,Z,C), path(Z,T,J, Total2), Total is C + Total2.

max([H|[]], H) :- !.
max([H | T], H) :- max(T,M2), H > M2, !.
max([H | T], M2) :- max(T,M2), H=< M2.

min([H|[]], H) :- !.
min([H | T], H) :- min(T,M2), H < M2, !.
min([H | T], M2) :- min(T,M2), H >= M2.

minpath([H | []], C, W) :- H = [C | W], !.
minpath([H | T], C, W) :- H = [C | W], minpath(T, M2, _), C < M2, !.
minpath([H | T], M, W) :- H = [C | _], minpath(T, M, W), C >= M.


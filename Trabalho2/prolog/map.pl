%% INF1771 Trabalho 2
%% Leonardo E. Wajnsztok
%% Ilan Grynszpan

%% Variaveis dinamicas
:-dynamic tile/3.

%% Tile map 12x12 e itens dos tiles

%% inimigo_fraco	Inimigo 20 Dano			
%% inimigo_forte	Inimigo 50 Dano			
%% buraco			Buraco			
%% teletransporte	Teletransporter			
%% Ouro				Ouro/Tesouro			
%% power_up			Power-up			

tile(1,1,[ouro]).
tile(1,2,[]).
tile(1,3,[]).
tile(1,4,[]).
tile(1,5,[]).
tile(1,6,[]).
tile(1,7,[]).
tile(1,8,[]).
tile(1,9,[]).
tile(1,10,[]).
tile(1,11,[]).
tile(1,12,[]).

tile(2,1,[]).
tile(2,2,[buraco]).
tile(2,3,[]).
tile(2,4,[]).
tile(2,5,[]).
tile(2,6,[teletransporte]).
tile(2,7,[]).
tile(2,8,[]).
tile(2,9,[]).
tile(2,10,[buraco]).
tile(2,11,[]).
tile(2,12,[]).

tile(3,1,[]).
tile(3,2,[]).
tile(3,3,[inimigo_forte]).
tile(3,4,[]).
tile(3,5,[]).
tile(3,6,[]).
tile(3,7,[power_up]).
tile(3,8,[]).
tile(3,9,[]).
tile(3,10,[]).
tile(3,11,[]).
tile(3,12,[]).

tile(4,1,[]).
tile(4,2,[]).
tile(4,3,[]).
tile(4,4,[]).
tile(4,5,[]).
tile(4,6,[]).
tile(4,7,[]).
tile(4,8,[]).
tile(4,9,[inimigo_fraco]).
tile(4,10,[]).
tile(4,11,[]).
tile(4,12,[]).

tile(5,1,[]).
tile(5,2,[]).
tile(5,3,[]).
tile(5,4,[]).
tile(5,5,[]).
tile(5,6,[]).
tile(5,7,[teletransporte]).
tile(5,8,[]).
tile(5,9,[]).
tile(5,10,[]).
tile(5,11,[buraco]).
tile(5,12,[]).

tile(6,1,[power_up]).
tile(6,2,[]).
tile(6,3,[]).
tile(6,4,[]).
tile(6,5,[]).
tile(6,6,[]).
tile(6,7,[]).
tile(6,8,[]).
tile(6,9,[]).
tile(6,10,[]).
tile(6,11,[]).
tile(6,12,[]).

tile(7,1,[]).
tile(7,2,[]).
tile(7,3,[]).
tile(7,4,[]).
tile(7,5,[]).
tile(7,6,[buraco]).
tile(7,7,[]).
tile(7,8,[ouro]).
tile(7,9,[]).
tile(7,10,[]).
tile(7,11,[]).
tile(7,12,[]).

tile(8,1,[]).
tile(8,2,[]).
tile(8,3,[]).
tile(8,4,[]).
tile(8,5,[]).
tile(8,6,[inimigo_forte]).
tile(8,7,[]).
tile(8,8,[buraco]).
tile(8,9,[]).
tile(8,10,[]).
tile(8,11,[]).
tile(8,12,[]).

tile(9,1,[]).
tile(9,2,[]).
tile(9,3,[inimigo_fraco]).
tile(9,4,[]).
tile(9,5,[]).
tile(9,6,[]).
tile(9,7,[]).
tile(9,8,[]).
tile(9,9,[]).
tile(9,10,[teletransporte]).
tile(9,11,[]).
tile(9,12,[]).

tile(10,1,[buraco]).
tile(10,2,[]).
tile(10,3,[]).
tile(10,4,[]).
tile(10,5,[]).
tile(10,6,[]).
tile(10,7,[]).
tile(10,8,[buraco]).
tile(10,9,[]).
tile(10,10,[]).
tile(10,11,[]).
tile(10,12,[]).

tile(11,1,[]).
tile(11,2,[]).
tile(11,3,[]).
tile(11,4,[buraco]).
tile(11,5,[]).
tile(11,6,[]).
tile(11,7,[]).
tile(11,8,[]).
tile(11,9,[]).
tile(11,10,[]).
tile(11,11,[]).
tile(11,12,[ouro]).

tile(12,1,[]).
tile(12,2,[]).
tile(12,3,[]).
tile(12,4,[]).
tile(12,5,[]).
tile(12,6,[]).
tile(12,7,[teletransporte]).
tile(12,8,[]).
tile(12,9,[]).
tile(12,10,[power_up]).
tile(12,11,[]).
tile(12,12,[]).
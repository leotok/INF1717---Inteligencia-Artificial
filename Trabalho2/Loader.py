#!/usr/bin/env python
#coding: utf8 

import MonsterTypes
import Monster
import random
import Maze
import sys
import Player

def load_game():
	
	# load empty maze

	maze = []

	for row in range(24):

		maze.append(list('X' * 24))

	# enemies positions:

	enemies_pos = []

	for i in range(2 + 2 + 4 + 8):
		
		enemies_pos.append([random.randint(2,24), random.randint(2,24)]) # 2 para que nao caia na mesma casa em que o jogo comeca

	# god position

	gold_pos = []

	while(len(gold_pos) < 3):

		new_gold_pos = [random.randint(2,24), random.randint(2,24)]

		while new_gold_pos in gold_pos:
			new_gold_pos = [random.randint(2,24), random.randint(2,24)]

		gold_pos.append([random.randint(2,24), random.randint(2,24)]) # 2 para que nao caia na mesma casa em que o jogo comeca

	# criando nossos monstros

	enemies = str(MonsterTypes.DAMAGE20)*2 + str(MonsterTypes.DAMAGE50)*2 + str(MonsterTypes.TRANSPORT)*4 + str(MonsterTypes.HOLE)*8

	enemies = sorted(enemies, key = lambda x: random.random() )

	enemies_list = [Monster.Monster(int(enemies[0]), enemies_pos[0]), 
					Monster.Monster(int(enemies[1]), enemies_pos[1]), 
					Monster.Monster(int(enemies[2]), enemies_pos[2]), 
					Monster.Monster(int(enemies[3]), enemies_pos[3]), 
					Monster.Monster(int(enemies[4]), enemies_pos[4]), 
					Monster.Monster(int(enemies[5]), enemies_pos[5]), 
					Monster.Monster(int(enemies[6]), enemies_pos[6]),
					Monster.Monster(int(enemies[7]), enemies_pos[7]), 
					Monster.Monster(int(enemies[8]), enemies_pos[8]), 
					Monster.Monster(int(enemies[9]), enemies_pos[9]), 
					Monster.Monster(int(enemies[10]), enemies_pos[10]), 
					Monster.Monster(int(enemies[11]), enemies_pos[11]), 
					Monster.Monster(int(enemies[12]), enemies_pos[12]), 
					Monster.Monster(int(enemies[13]), enemies_pos[13]), 
					Monster.Monster(int(enemies[14]), enemies_pos[14]),
					Monster.Monster(int(enemies[15]), enemies_pos[15])
					] 

	for pos in range(len(enemies_pos)):

		maze[enemies_pos[pos][0] - 1][enemies_pos[pos][1] - 1] = enemies[pos]

	for pos in range(len(gold_pos)):

		maze[gold_pos[pos][0] - 1][gold_pos[pos][1] - 1] = 'O'

	board = Maze.Maze(maze, enemies_list)

	return(board)

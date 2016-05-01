#!/usr/bin/env python
#coding: utf8 


# classe para o jogador

class Player:

	def __init__(self, pos):

		self.pos = [pos[0],  pos[1]] # posicao inicial do jogador, pos[0] eh a linha, pos[1] eh a coluna

		self.energy = 100 # energia inicial do Player

	def move(self, direction):

		look = 1

		if(direction not in ['R', 'U']): # use L para Esquerda, R, para Direita, U para Subir, D para Descer no tabuleiro

			print('direcao invalida')
			return -1

		elif(direction == 'R'):

			if(pos[1] == 24):
				
				print('posicao final invalida')
				return -1

			else:                # turn the player
				if look == 1:
					look = 2
				elif look == 2:
					look = -1
				elif look == -1:
					look = -2
				elif look == -2:
					look = 1
				

		elif(direction == 'U'):

			if look == 1:
				if(self.pos[0] + 1 > 24):
					print('posicao invalida')
				else:
					self.pos[0] += 1
			elif look == 2:
				if(self.pos[1] + 1 > 24):
					print('posicao invalida')
				else:
					self.pos[1] += 1
			elif look == -1:
				if(self.pos[0] + 1 > 24):
					print('posicao invalida')
				else:
					self.pos[0] -= 1
			elif look == -2:
				if(self.pos[1] -1 < 1):
					print('posicao invalida')
				else:
					self.pos[1] -= 1

		self.last_move = look
		return 0 # sucesso

	def shoot(self):

		return(list(self.last_move, self.pos)) # soh retorna lista para sabermos a direcao e o comeco do tiro, o tiro mesmo fica com a parte grafica e o dano fica no objeto do monstro




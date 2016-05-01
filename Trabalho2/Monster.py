#!/usr/bin/env python
#coding: utf8 

import MonsterTypes

# classe para os monstros e buracos


class Monster:

	def __init__(self, shape, pos): # shape deve receber um elemento de MonsterTypes

		self.shape = shape

		self.id = 0

		if(self.shape == MonsterTypes.HOLE):
			self.id = 1

		elif(self.shape == MonsterTypes.TRANSPORT):
			self.id = 2

		elif(self.shape == MonsterTypes.DAMAGE20):
			self.id = 3

		elif(self.shape == MonsterTypes.DAMAGE50):
			self.id = 4

		self.pos = pos

		self.footprints_pos = [[self.pos[0] + 1, self.pos[1]], 
			[self.pos[0] - 1, self.pos[1]], 
			[self.pos[0], self.pos[1] - 1], 
			[self.pos[0], self.pos[1] + 1]]  # cheiro, brisa ou passos (rastros de obstaculo)

		for pair in self.footprints_pos:
			if pair[0] < 1 or pair[1] < 1 or pair[0] > 24 or pair[1] > 24:

				self.footprints_pos.pop(self.footprints_pos.index(pair))   # remove rastros de montro colocados acidentalmente fora do tabuleiro

		self.footprints_shape = '' # brisa - buraco, teletransporte - flash e passos, wumpus - passos e mal cheiro. 

		if(self.shape == MonsterTypes.HOLE):

			self.footprints_shape += str(MonsterTypes.WIND)

		elif(self.shape == MonsterTypes.TRANSPORT):

			self.footprints_shape += (str(MonsterTypes.FLASH) + str(MonsterTypes.STEPS))

		elif(self.shape == MonsterTypes.DAMAGE20 or self.shape == MonsterTypes.DAMAGE50):

			self.footprints_shape += (str(MonsterTypes.SMELL) + str(MonsterTypes.STEPS))

	def get_footprints(self):

		return([self.footprints_pos, self.footprints_shape])


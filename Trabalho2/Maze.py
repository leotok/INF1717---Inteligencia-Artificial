#!/usr/bin/env python
#coding: utf8 


# classe para o tabuleiro do jogo

class Maze:

	def __init__(self, board, enemies_list):

		self.maze = board

		self.dims = [24,24] # dimensoes do jogo

		self.enemies = enemies_list

		self.tracks = []

		for enemy in enemies_list:
			self.tracks.append([enemy.footprints_pos, enemy.footprints_shape])

		print(self.tracks)

	def get_pos_info(self, pos):

		if(pos in self.tracks):

			return self.tracks[self.tracks.index(pos)][1]

		return 0

	def get_maze(self):

		return(self.maze)
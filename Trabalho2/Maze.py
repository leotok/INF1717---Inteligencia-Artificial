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
			self.tracks.append(enemy.footprints_pos)

		print(self.tracks)

	def get_maze(self):

		return(self.maze)
import pygame
from helpers import *
from pygame.locals import *

ratio = 1

class Tilemap(list):

	def __init__(self, matrix):

		self.width = len(matrix[1])
		self.height = len(matrix)
		self.matrix = matrix

		for i in range(self.height):
			for j in range(self.width):
				self.append( Tile(i, j, matrix[i][j]) )

	@staticmethod
	def get_tilemap(arq):

		with open(arq, "r") as f:
			matrix = f.read()

		matrix = matrix.split('\n') 
		tilemap = Tilemap(matrix)
		return tilemap

	def get_tile(self, x, y):
		try:
			return self[ (x * (self.height -1)) + y]
		except IndexError:
			print "IndexError: ", x, y

	def get_tile_sprite(self, x, y):
		try:
			x = x-1
			y = y-1
			print x,y,  (x*12) + y
			return self.tile_sprites_list[ (x * 12) + y ]
		except IndexError:
			print "IndexError: ", x, y

	def print_map_log(self):
		j = 0
		for i in range(len(self)):
			if j != self[i].x:
				print
				j = self[i].x
			print self[i], 
		print
		

	# Funcao para achar a posicao final no Maze representado por 'F'

	def find_end(self):
		for i in range(len(self)):
			if self[i].type_char == "F":
				return self[i]
		return None

	# Funcao para achar a posicao inicial no Maze representado por 'I'

	def find_start(self):
		for i in range(len(self)):
			if self[i].type_char == "I":
				return self[i]
		return None

	def create_sprite_map(self):

		width = (50 * ratio)
		height = (50 * ratio)  

		self.tile_sprites_group = pygame.sprite.Group()  
		self.tile_sprites_list = []    

		for x ,line in enumerate(self.matrix):
			for y, tile in enumerate(line):
				print x, y
				tile_sprite = GrassSprite(pygame.Rect(y* width, x* height, width, height), x  , y ) 
				self.tile_sprites_group.add(tile_sprite)
				self.tile_sprites_list.append(tile_sprite)
		


class Tile(object):

	def __init__(self, x, y, type_char):

		self.x = x
		self.y = y
		self.type_char = type_char

	def __repr__(self):
		return str((self.x, self.y))

	def __str__(self):
		return str(self.type_char)


class GrassSprite(pygame.sprite.Sprite):
	def __init__(self, rect, x, y):

		pygame.sprite.Sprite.__init__(self) 
		self.x = x
		self.y = y
		self.rect = rect

		self.image= load_image("grass.jpg",-1)
		# self.size = self.image.get_size()
		# self.image = pygame.transform.scale(self.image, (int(self.size[0] * ratio), int(self.size[1] * ratio)))

class PlaneSprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image= load_image('xwing.png',-1)
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.size = self.image.get_size()
        ratio = 0.3908
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * ratio), int(self.size[1] * ratio)))
import pygame
from helpers import *
from pygame.locals import *

class Plane():

	energy = 5

	def __init__(self, nome, power):
		self.nome = nome
		self.power = power


	def __repr__(self):
		return str(self.nome)

	def __str__(self):
		return "%s: power %.1f / energy %d" %(self.nome, self.power, self.energy)

	@staticmethod
	def get_battle_time(base_cost, planes):

		power_sum = sum([ plane.power for plane in planes ])
		if power_sum == 0:
			power_sum = 1

		battle_time = float(base_cost / power_sum)
		print base_cost, battle_time, "min"
		return battle_time

class PlaneSprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image= load_image('xwing.png',-1)
        self.rect = pygame.Rect(0, 0, 64, 64)
        self.size = self.image.get_size()
        ratio = 0.3908
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * ratio), int(self.size[1] * ratio)))
        

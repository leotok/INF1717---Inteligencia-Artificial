import pygame
from helpers import *
from pygame.locals import *

class Plane():

	energy = 5

	def __init__(self, name, power, codename, pilot):
		self.name = name
		self.power = power
		self.codename = codename
		self.pilot = pilot


	def __repr__(self):
		return str(self.name)

	def __str__(self):
		return "%s: power %.1f / energy %d" %(self.name, self.power, self.energy)

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
        
class PilotSprite(pygame.sprite.Sprite):

	def __init__(self, pilot_num, plane):

		self.plane = plane
		pygame.sprite.Sprite.__init__(self)
		self.image= load_image("red" + str(pilot_num) + ".jpg" , -1)
		# self.size = self.image.get_size()
		self.rect = pygame.Rect(1010, 20 + (pilot_num-2)  * 200, 150, 150)
        
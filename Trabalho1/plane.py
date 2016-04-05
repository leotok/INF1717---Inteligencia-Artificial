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
		return float(base_cost / power_sum)

class PlaneSprite(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image= load_image('xwing.png',-1)
        self.rect = pygame.Rect(0, 0, 64, 64)
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 0.01), int(self.size[1] * 0.01)))
        
        """Set the number of Pixels to move each time"""
        self.x_dist = 10
        self.y_dist = 10

    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        xMove = 0;
        yMove = 0;
        
        if (key == K_RIGHT):
            xMove = self.x_dist
        if (key == K_LEFT):
            xMove = -self.x_dist
        if (key == K_UP):
            yMove = -self.y_dist
        if (key == K_DOWN):
            yMove = self.y_dist
        #self.rect = self.rect.move(xMove,yMove);
        self.rect.move_ip(xMove,yMove);

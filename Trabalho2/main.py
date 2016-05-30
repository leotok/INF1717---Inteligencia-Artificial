from pyswip import Prolog
import pygame
from pygame import display,movie
from helpers import *
from pygame.locals import *

from prolog_bridge import *
from tile import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


class Main(object):
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		
	def MainLoop(self):


		bridge = Bridge("prolog/map.pl","prolog/map_observ.pl","prolog/facts.pl")
		
		ret = bridge.ask("vida(X)",["X"])
		print "Vida:", ret

		self.posicao_inicial = bridge.ask("posicao(X,Y,Z)",["X","Y","Z"])
		print "Posicao atual:", self.posicao_inicial

		self.ouro = bridge.ask("ouro_bolsa(X)",["X"])
		print "Ouro na bolsa:", self.ouro

		self.custo = bridge.ask("custo(X)",["X"])
		print "Custo:", self.custo

		self.tilemap = Tilemap.get_tilemap("maze.txt")
		self.tilemap.print_map_log()

		self.tilemap.create_sprite_map()
		self.load_sprites()

		# tell pygame to keep sending up keystrokes when they are held down
		pygame.key.set_repeat(500, 30)
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((145,145,145))

		close = 0

		print
		melhor_acao = bridge.ask("melhor_acao(A,X,Y,D)",["A","X","Y","D"])
		print "Melhor acao:", melhor_acao
		ret = bridge.ask("custo(X)",["X"])
		print "Custo:", ret

		while 1:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == KEYDOWN:
					if ((event.key == K_RIGHT)
					or (event.key == K_LEFT)
					or (event.key == K_UP)
					or (event.key == K_DOWN)):
						print "Key pressed"

			if melhor_acao[0][0] != "nada_pra_fazer_vou_me_envolver_com_as_fans":

				print
				melhor_acao = bridge.ask("melhor_acao(A,X,Y,D)",["A","X","Y","D"])
				print "Melhor acao:", melhor_acao
				custo = bridge.ask("custo(X)",["X"])
				print "Custo:", custo
				self.posicao_atual = bridge.ask("posicao(X,Y,Z)",["X","Y","Z"])
				print "Posicao atual:", self.posicao_atual

				self.x = self.posicao_atual[0][0]
				self.y = self.posicao_atual[0][1]
			
			self.screen.blit(self.background, (0, 0))
			self.tilemap.tile_sprites_group.draw(self.screen)
			self.plane_sprite.draw(self.screen)
			pygame.display.flip()
			pygame.time.wait(200)

			self.x = self.posicao_atual[0][0]
			self.y = self.posicao_atual[0][1]

			self.plane.rect.topleft = self.tilemap.get_tile_sprite(self.x, self.y).rect.topleft




	def load_sprites(self):
		self.plane = PlaneSprite()
		self.plane_sprite = pygame.sprite.RenderPlain((self.plane))
		self.plane.rect.topleft = [0,0] 
		self.plane.rect.topleft = self.tilemap.get_tile_sprite(self.posicao_inicial[0][0], self.posicao_inicial[0][1]).rect.topleft



if __name__ == '__main__':
	
	MainWindow = Main(1300, 700)
	MainWindow.MainLoop()
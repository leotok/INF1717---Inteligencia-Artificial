from pyswip import Prolog
import pygame
from pygame import display,movie
from helpers import *
from pygame.locals import *

from prolog_bridge import *
from tile import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


# class Bridge(object):
	
# 	def __init__(self, tilemap, facts, logic):
# 		self.prolog = Prolog()
# 		self.prolog.consult(facts)
# 		self.prolog.consult(logic)
# 		self.prolog.consult(tilemap)
		
		

	

# if __name__ == '__main__':
	
# 	mapfile = open("Maze.txt", "r")
	
# 	print(mapfile.read())
	
# 	#bridge = Bridge("map.pl", "facts.pl", "logic.pl")

class Main(object):
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		
	def MainLoop(self):

		# tell pygame to keep sending up keystrokes when they are held down
		pygame.key.set_repeat(500, 30)
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((145,145,145))


		while 1:
			self.screen.blit(self.background, (0, 0))   

			pygame.display.flip()

			pygame.time.wait(100)



	def load_sprites(self):
		pass


if __name__ == '__main__':
	
	# MainWindow = Main(1300, 1000)
 #    MainWindow.MainLoop()


	bridge = Bridge("prolog/map.pl","prolog/map_observ.pl","prolog/facts.pl")
	
	ret = bridge.ask("tile(X,Y,[ouro])",["X","Y"])
	print "Ouros:", ret

	ret = bridge.ask("tile(X,Y,[buraco])",["X","Y"])
	print "Buracos:", ret

	ret = bridge.ask("vida(X)",["X"])
	print "Vida:", ret

	ret = bridge.ask("posicao(X,Y,Z)",["X","Y","Z"])
	print "Posicao atual:", ret

 # 	print "Teste andar:"

 # 	bridge.ask("andar",[])
 # 	ret = bridge.ask("posicao(X,Y,Z)",["X","Y","Z"])
	# print ret

	# bridge.ask("andar",[])
 # 	ret = bridge.ask("posicao(X,Y,Z)",["X","Y","Z"])
	# print ret

	# bridge.ask("andar",[])
 # 	ret = bridge.ask("posicao(X,Y,Z)",["X","Y","Z"])
	# print ret

	# bridge.ask("virar_direita",[])
 # 	ret = bridge.ask("posicao(X,Y,Z)",["X","Y","Z"])
	# print ret

	# bridge.ask("andar",[])
 # 	ret = bridge.ask("posicao(X,Y,Z)",["X","Y","Z"])
	# print ret

	# bridge.ask("andar",[])
 # 	ret = bridge.ask("posicao(X,Y,Z)",["X","Y","Z"])
	# print ret

	ret = bridge.ask("ouro_bolsa(X)",["X"])
	print "Ouro na bolsa:", ret

	ret = bridge.ask("melhor_acao(A,X,Y)",["A","X","Y"])
	print "Melhor acao:", ret

 	ret = bridge.ask("ouro_bolsa(X)",["X"])
	print "Ouro na bolsa:", ret

	ret = bridge.ask("melhor_acao(A,X,Y)",["A","X","Y"])
	print "Melhor acao:", ret

 	ret = bridge.ask("ouro_bolsa(X)",["X"])
	print "Ouro na bolsa:", ret

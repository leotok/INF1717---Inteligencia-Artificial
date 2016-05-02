
import Loader
import Player

class Game:

	def __init__(self):

		self.maze = Loader.load_game()
		self.player = Player.Player(self.maze, [1,1])

	def show(self):

		
		for i in self.maze.maze:
			print(i)

		print(self.player.pos)

	def move(self, direction):

		if direction == 1:

			self.player.move('U')


		elif direction == 2:

			self.player.move('R')

	def update(self):

		if(self.maze.maze[self.player.pos[0]][self.player.pos[1]] != 'X'):
			self.player.energy -= 1000

		if(self.player.energy < 0):
			print('game over')
			return





game = Game()

game.show()

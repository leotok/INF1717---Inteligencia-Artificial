from plane import Plane
from tile import *
import heapq

class AStar(object):

	def __init__(self, tilemap, planes, enemy_bases, base_cost):

		self.opened = []
		heapq.heapify(self.opened)
		self.closed = set()
		self.tiles = tilemap
		self.planes = planes

		self.start = tilemap.find_start()
		self.end = tilemap.find_end()
		self.enemy_bases = enemy_bases
		self.base_cost = base_cost
		self.steps = 0
	   
	def heuristic_function_for_tile(self, tile):
		h =  0.9 *  (abs(tile.x - self.end.x) + abs(tile.y - self.end.y))
		return h

	def get_neighbours(self, tile):

		neighbours = list()		
		if tile.x < self.tiles.height - 1:
			neighbours.append(self.tiles.get_tile(tile.x+1, tile.y))
		if tile.y > 0:
			neighbours.append(self.tiles.get_tile(tile.x, tile.y-1))
		if tile.x > 0:
			neighbours.append(self.tiles.get_tile(tile.x-1, tile.y))
		if tile.y < self.tiles.width - 1:
			neighbours.append(self.tiles.get_tile(tile.x, tile.y+1))
		return neighbours

	def get_solution(self):
		print "Em aberto: ",len(self.opened)
		print "Visitados: ", len(self.closed)
		tile = self.end
		solution = []
		solution.append(tile)
		while tile.parent is not self.start:
			tile = tile.parent
			solution.append(tile)
		solution.append(self.start)
		return solution

	def get_planes_for_base(self, base_index):

  		# custo = 532,88 bases de 1 a 11
  		# melhor combinacao que achei ate agora, redistribuindo todos avios das bases q nao passava

  		# tactic = [[self.planes[0],self.planes[1],self.planes[2],self.planes[3]],
				#   [self.planes[0],self.planes[1],self.planes[2],self.planes[3],self.planes[4]],
				#   [self.planes[0],self.planes[1],self.planes[2],self.planes[3],self.planes[4]],
				#   [],
				#   [],
				#   [],
				#   [],
				#   [self.planes[0],self.planes[1],self.planes[2],self.planes[3],self.planes[4]],
				#   [self.planes[0],self.planes[1],self.planes[2],self.planes[3],self.planes[4]],
				#   [],
  		# 		  []]

  		# custo = 616,36
  		# de 2 a 3 avioes para cada base, sem redistribuir os que sobram no final
  		tactic = 	[[self.planes[4],self.planes[3]],[self.planes[4],self.planes[2]],
  					[self.planes[3],self.planes[2]],[self.planes[3],self.planes[2]],
  					[self.planes[3],self.planes[2]],[self.planes[1],self.planes[2]],
					[self.planes[1],self.planes[0]],[self.planes[1],self.planes[0]],
  				  	[self.planes[1],self.planes[0]],
  				  	[self.planes[3],self.planes[0],self.planes[4]],
  				  	[self.planes[1],self.planes[0],self.planes[4]]]

		return tactic[base_index]

	def update_tile(self, neighbour, tile, move_cost):

		neighbour.g = tile.g + move_cost
		neighbour.h = self.heuristic_function_for_tile(neighbour)
		neighbour.parent = tile
		neighbour.f = neighbour.h + neighbour.g

	def print_by_step(self, tile):

		print "Step ", self.steps
		self.steps += 1
		old_type = tile.type_char
		tile.type_char = "o"
		self.tiles.print_map_log()
		raw_input("Pressione Enter para avancar.")
		tile.type_char = old_type

	def get_move_cost(self, neighbour):
		if neighbour.type_char == "B":
			base_index = self.enemy_bases.index((neighbour.x,neighbour.y))
			attacking_planes = self.get_planes_for_base(base_index)
			move_cost = Plane.get_battle_time(self.base_cost[base_index], attacking_planes)
			neighbour.planes_attackers = attacking_planes
		else:
			move_cost = neighbour.get_cost()
		return move_cost

	def find_path(self):
		# tile com menor custo f (g+h) fica no topo do heap
		heapq.heappush(self.opened, (self.start.f, self.start))

		while len(self.opened):
			f, tile = heapq.heappop(self.opened)
			# self.print_by_step(tile)
			# closed eh um set de elementos unicos q ja foram percorridos
			self.closed.add(tile)

			if tile is self.end:
				return self.get_solution()

			neighbours = self.get_neighbours(tile)

			for neighbour in neighbours:

				if neighbour not in self.closed:
					move_cost = self.get_move_cost(neighbour)
					if (neighbour.f, neighbour) in self.opened:
						if neighbour.g > tile.g + move_cost:
							self.update_tile(neighbour, tile, move_cost)
					else:
						self.update_tile(neighbour, tile, move_cost)
						heapq.heappush(self.opened, (neighbour.f, neighbour))

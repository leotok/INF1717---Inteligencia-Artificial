from plane import Plane
from tile import *
import heapq

class AStar(object):

	def __init__(self, tilemap, planes, enemy_bases):

		self.opened = []
		heapq.heapify(self.opened)
		self.closed = set()
		self.tiles = tilemap
		self.planes = planes

		self.start = tilemap.find_start()
		self.end = tilemap.find_end()
		self.enemy_bases = enemy_bases
	    
	def heuristic_function_for_tile(self, tile):
		h = 1 *  (abs(tile.x - self.end.x) + abs(tile.y - self.end.y))
		return h

	def get_neighbours(self, tile):

		neighbours = list()
		# print tile.x, tile.y
		
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
		tile = self.end
		solution = []
		while tile.parent is not self.start:
			tile = tile.parent
			solution.append(tile)
		return solution

	def get_planes_for_base(self, base_index):
		
		tactic = [[self.planes[4],self.planes[3]],[self.planes[4],self.planes[2]],
				  [self.planes[3],self.planes[2]],[self.planes[3],self.planes[2]],
				  [self.planes[3],self.planes[2]],[self.planes[3],self.planes[2]],
				  [self.planes[1],self.planes[0]],[self.planes[1],self.planes[0]],
				  [self.planes[1],self.planes[0],self.planes[4]],
				  [self.planes[1],self.planes[0],self.planes[4]],
				  [self.planes[1],self.planes[0],self.planes[4]]]
		return tactic[base_index]

	def update_tile(self, neighbour, tile):

		if neighbour.type_char == "B":
			print neighbour.x,neighbour.y
			base_index = self.enemy_bases.index((neighbour.x,neighbour.y))
			attacking_planes = self.get_planes_for_base(base_index)
			move_cost = neighbour.get_battle_time(base_index, attacking_planes)
			# self.planes = filter(lambda plane: plane.energy > 0, self.planes)
			# if len(planes) == 0:
			# 	print "Todos avioes foram abatidos!"
			# sys.exit()
		else:
			move_cost = neighbour.get_cost()
		
		neighbour.g = tile.g + move_cost
		neighbour.h = self.heuristic_function_for_tile(neighbour)
		neighbour.parent = tile
		neighbour.f = neighbour.h + neighbour.g

	def find_path(self):
		# tile com menor custo f (g+h) fica no topo do heap
		heapq.heappush(self.opened, (self.start.f, self.start))

		while len(self.opened):
			f, tile = heapq.heappop(self.opened)
			# closed eh um set de elementos unicos q ja foram percorridos
			self.closed.add(tile)

			if tile is self.end:
				return self.get_solution()

			neighbours = self.get_neighbours(tile)

			for neighbour in neighbours:

				if neighbour not in self.closed:
					if (neighbour.f, neighbour) in self.opened:
						if neighbour.g > tile.g:
							self.update_tile(neighbour, tile)
					else:
						self.update_tile(neighbour, tile)
						heapq.heappush(self.opened, (neighbour.f, neighbour))





from plane import Plane
from tile import *
import heapq

class AStar(object):

	def __init__(self, tilemap):

		self.opened = []
		heapq.heapify(self.opened)
		self.closed = set()
		self.tiles = tilemap

		self.start = tilemap.find_start()
		self.end = tilemap.find_end() 

	def get_battle_time(base_num, planes):

		for i, plane in enumerate(planes): 

			if plane.life == 0:
				planes[i].remove()
			else:
				plane.life -= 1

		base_cost = [60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120]
		power_sum = sum([ plane.power for plane in planes ])

		return float(base_cost[base_num - 1] / power_sum)
	    
	def heuristic_function_for_tile(self, tile):
		return 10 * (abs(tile.x - self.end.x) + abs(tile.y - self.end.y))


	def get_neighbours(self, tile):

		neighbours = list()
		print tile.x, tile.y
		
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

	def update_tile(self, neighbour, tile):
		neighbour.g = tile.g + 10
		neighbour.h = self.heuristic_function_for_tile(neighbour)
		neighbour.parent = tile
		neighbour.f = neighbour.h + neighbour.g

	def find_path(self, squad):

		heapq.heappush(self.opened, (self.start.f, self.start))

		while len(self.opened):
			f, tile = heapq.heappop(self.opened)
			self.closed.add(tile)

			if tile is self.end:
				return self.get_solution()

			neighbours = self.get_neighbours(tile)

			for neighbour in neighbours:

				if neighbour not in self.closed:
					if (neighbour.f, neighbour) in self.opened:
						if neighbour.g > tile.g + 10:
							self.update_tile(neighbour, tile)
					else:
						self.update_tile(neighbour, tile)
						heapq.heappush(self.opened, (neighbour.f, neighbour))





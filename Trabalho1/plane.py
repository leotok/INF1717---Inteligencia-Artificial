class Plane(object):

	energy = 5

	def __init__(self, nome, power):
		self.nome = nome
		self.power = power

	def __repr__(self):
		return str(self.nome)

	def __str__(self):
		return "%s: power %.1f / energy %d" %(self.nome, self.power, self.energy)

	@staticmethod
	def get_battle_time(base_num, planes):

		base_cost = [60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120]
		power_sum = sum([ plane.power for plane in planes ])
		if power_sum == 0:
			power_sum = 1
		return float(base_cost[base_num] / power_sum)
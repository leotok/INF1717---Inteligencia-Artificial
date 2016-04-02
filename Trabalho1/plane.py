class Plane(object):

	energy = 5

	def __init__(self, nome, power):
		self.nome = nome
		self.power = power

	def __repr__(self):
		return str(self.nome)

	def __str__(self):
		return "%s: power %.1f / life %d" %(self.nome, self.power, self.energy)

	def lost_energy(self, energy_spent):
		self.energy -= energy_spent

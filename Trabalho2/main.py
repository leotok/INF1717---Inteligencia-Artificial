from pyswip import Prolog


class Bridge(object):
	
	def __init__(self, tilemap, facts, logic):
		self.prolog = Prolog()
		self.prolog.consult(facts)
		self.prolog.consult(logic)
		self.prolog.consult(tilemap)

	

if __name__ == '__main__':

	bridge = Bridge("map.pl", "facts.pl", "logic.pl")
from pyswip import Prolog

class Bridge(object):
	
	def __init__(self, tilemap, prolog_facts, prolog_logic):
		self.prolog = Prolog()
		self.prolog.consult(tilemap)
		self.prolog.consult(prolog_facts)
		self.prolog.consult(prolog_logic)

	


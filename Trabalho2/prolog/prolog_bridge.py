from pyswip import Prolog

class Bridge(object):
	
	def __init__(self, prolog_facts, prolog_logic):
		self.prolog = Prolog()
		self.prolog.consult(prolog_facts)
		self.prolog.consult(prolog_logic)

	


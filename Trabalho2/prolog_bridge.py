from pyswip import Prolog

class Bridge(object):
	
	def __init__(self, tilemap, tilemap_obs, prolog_facts):

		self.prolog = Prolog()
		self.prolog.consult(tilemap)
		self.prolog.consult(prolog_facts)
		self.prolog.consult(tilemap_obs)

	

	def ask(self, query_string, var_list):

		answer = list()
		for i in self.prolog.query(query_string):
			aux = list()
			for var in var_list: 
				aux.append(i[var])
			answer.append(aux)

		return answer
from pyswip import *

if __name__ == '__main__':

	# prolog = Prolog()

	# prolog.consult('exemplo_prolog.pl')

	# print "Com 1:"
	# answer = prolog.query("tile(2,X,[]).")
     
	# for a in answer:
	# 	print a

	# print "Sem 1:"
	# # ret = prolog.query("retract(linkage(2,1,[]))")

	# answer = prolog.query("tile(2,1,[]).")

	# for a in answer:
	# 	print a
	p = Prolog()

	assertz = Functor("assertz")
	parent = Functor("parent", 2)
	test1 = newModule("test1")
	test2 = newModule("test2")
	  
	call(assertz(parent("john", "bob")), module=test1)
	call(assertz(parent("jane", "bob")), module=test1)
	  
	call(assertz(parent("mike", "bob")), module=test2)
	call(assertz(parent("gina", "bob")), module=test2)
	  
	print "knowledgebase test1"
	  
	X = Variable()
	q = Query(parent("jane", "bob"), module=test1)
	while q.nextSolution():
	    print X.get_value()
	q.closeQuery()
	  
	print "knowledgebase test2"
	  
	q = Query(parent(X, "bob"), module=test2)
	while q.nextSolution():
	    print X.value
	q.closeQuery()
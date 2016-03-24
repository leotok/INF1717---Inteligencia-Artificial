###		http://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python-are-there-any-built-in-data-structures-in	###

class Tree(object):

    "Generic tree node."
    def __init__(self, value='root', children=None, parent = None):
        self.value = value
        self.children = []
        self.parent = parent
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
    	return 'node={0}, children={1}'.format(self.value, self.children)

    def add_child(self, node):
        assert isinstance(node, Tree)
        node.parent = self
        self.children.append(node)

    def get_node_of_value(self, x):
    	if self.value is x: 
    		# print "found!"
    		return self
        for node in self.children:
            n = node.get_node_of_value(x)
            if n: return n
        return None

    def get_trail_from_node(self):
     	trail = list()
     	node = self
     	while node is not None:
     		trail.append(node)
     		node = node.parent
     	return trail

### Example: ###

# t = Tree("root",[Tree("1",[Tree("2"),Tree("4")]),Tree("3")])

# t.add_child(Tree("5"))

# print Tree.get_node_of_value(t,"2").get_trail_from_node()





# Python Program for union-find algorithm to detect cycle in a undirected graph
# we have one egde for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both

from collections import defaultdict

#This class represents a undirected graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		print("Vertices : ", self.V)
		print("graph : ", self.graph)
		print("--------------------")


	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
		print("Add edge : ", self.graph)

	# A utility function to find the subset of an element i
	def find_parent(self, parent,i):
		print("		Find parent : ", parent , " - i :", i)
		if parent[i] == -1:
			return i
		if parent[i]!= -1:
			return self.find_parent(parent,parent[i])

	# A utility function to do union of two subsets
	def union(self,parent,x,y):
		print("------------------ Union ---------------- ")
		x_set = self.find_parent(parent, x)
		y_set = self.find_parent(parent, y)
		print("				x_set : ", x_set)
		print("				y_set : ", y_set)
		parent[x_set] = y_set
		print("				parent : ", parent)
		print("------------------ Union ---------------- ")



	# The main function to check whether a given graph
	# contains cycle or not
	def isCyclic(self):
		
		# Allocate memory for creating V subsets and
		# Initialize all subsets as single element sets
		parent = [-1]*(self.V)
		print("parent : ", parent)


		# Iterate through all edges of graph, find subset of both
		# vertices of every edge, if both subsets are same, then
		# there is cycle in graph.
		for i in self.graph:
			for j in self.graph[i]:
				print("	i : ", i , " - j :", j)
				x = self.find_parent(parent, i) 
				print("			x :", x)

				y = self.find_parent(parent, j)
				print("			y :", y)
				if x == y:
					print("			========  x :", x, " - y :", y)
					return True
				self.union(parent,x,y)


# Create a graph given in the above diagram
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
print("--------------------")


if g.isCyclic():
	print("Graph contains cycle")
else :
	print("Graph does not contain cycle ")

#This code is contributed by Neelam Yadav

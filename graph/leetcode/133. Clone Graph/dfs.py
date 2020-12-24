'''
	first we need to understand undirected graph might be infivinite cycle if we don't use a visited check for already visited nodes.
	We need a visited hash map. 
		Key : current node,  value :  new created - cloned node
		we should check every time if current node is  visited, we can return directly  from visited hash map.
	
	We can apply DFS approach for graph traversal
		for every node we need to get neighbors
		for every neigbor we can append  neighbors of cloned_node

	and finally we can return cloned_code
'''

class Node(object):
	def __init__(self, val, neighbors=[]):
		self.val = val
		self.neighbors = neighbors

class Solution(object):
	def __init__(self):

		# we will keep to follow visited node. The helps avoid cycle.
		# key : node , value : clone_node
		self.visited = {}

	def cloneGraph(self, node):
		"""
		:type node: Node
		:rtype: Node
		"""

		if not node:
			print("not node : return ")
			return node

		#if the node was already visited before.
		#return the clone from the visited dict
		if node in self.visited:
			return self.visited[node]

		#create a clone for the given node
		#we don't have cloned neighbors as of now , hence []
		clone_node = Node(node.val, [])
		self.visited[node] = clone_node	

		#iterate trough the neighbors to generate their clones
		#and prepare a list of cloned neighbors to be added to the cloned node.
		for n in node.neighbors:
			clone_node.neighbors.append(self.cloneGraph(n))

		return clone_node


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

print("node1: ", node1)
print("node2: ", node2)
print("node3: ", node3)
print("node4: ", node4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node3, node1]

print(node1.neighbors)


res = Solution().cloneGraph(node1)
print("res : ", res.neighbors)

'''
Time complexity : 
	N : number of node 
	M : number of edges
	T(N) = O(N+M)

Spece : 
	N : The space is occupied by the visited hash map and in addition to that, 
	and space would be occupied reqursion  stack : H : height of graph  O(H)
	Overall , space complexity would be O(N)

'''
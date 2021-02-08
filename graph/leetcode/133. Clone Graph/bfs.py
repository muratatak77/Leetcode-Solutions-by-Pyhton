from collections import deque

class Node(object):
	def __init__(self, val, neighbors=[]):
		self.val = val
		self.neighbors = neighbors

class Solution(object):
	def __init__(self):

		# we will keep to follow visited node. The helps avoid cycle.
		# key : node , value : clone_node
		self.visited = {}

	def cloneGraph(self, node: 'Node') -> 'Node':
		
		if not node:
			return node
		
		q = deque([node])
		
		# visited = key : node_1 , value : clone_node_1
		self.visited[node] = Node(node.val, [])  
		print(" >>>>>>>>>>> Inital q : ", q , " Visited  ", self.visited)

		while q:
			n = q.popleft()
			print("		n from q popleft : ", n.val)
			for nei in n.neighbors:
				print("				nei in n;neighbors: ", nei.val)
				if nei not in self.visited:
					self.visited[nei] = Node(nei.val, [])
					q.append(nei)
					print("					Added nei to visited : ", nei.val)
				self.visited[n].neighbors.append(self.visited[nei])
				print("						Added n - neighbors : ", nei.val)

		return self.visited[node]

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
	N : number of node - vertices 
	M : number of edges
	T(N) = O(N+M)

Spece : 
	N : The space is occupied by the visited hash map and in addition to that, space also be occupied a queue in BFS approach.
	Would be in BFS O(W) , W : Weight of the graph
	Overall , space complexity would be O(N)

'''

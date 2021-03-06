'''
bibartite is meaning that a graph could be 2 part exactly 

we can use  to change color with node by node.  
	Like we can say first start node color is red = 1 and  its neighbors will be green = 0.
	and we can use a hash map to keep and track node is visited or not.
	and we can use a queue - FIFO for iterate every node neighbours.

	and when we reach previous visited node again , we can check current color and in hash map color. 

	if colors are same this graph is not bibartite. 
	Is different is bibartite.

'''

class Solution:
	def isBipartite(self, graph):

		if not graph:
			return False
		color = {}
		
		def dfs(node):
			for nei in graph[node]:
				if nei not in color:
					color[nei] = 1 - color[node]
					if not dfs(nei):
						return False
				elif color[nei] == color[node]:
					return False
			return True
	
		for node in range(len(graph)):
			if node in color:
				continue

			color[node] = 0
			if not dfs(node):
				return False
			return True


graph = [[1,3], [0,2], [1,3], [0,2]]
graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
# graph = [[0,2], [0,1,3]]
# 
ans = Solution().isBipartite(graph)
print(ans)

'''
N = Number of nodes in the graph 
E = Number of edges
We explore each node one when we transform it from uncolored to colored , traversing all in edges in the process
T(N) = O(N+E) 

Space : O(N) the space used to store the color

'''
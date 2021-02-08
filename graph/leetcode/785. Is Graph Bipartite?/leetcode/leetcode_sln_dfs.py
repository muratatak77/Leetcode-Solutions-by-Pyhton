class Solution:
	def isBipartite(self, graph):

		#blue = 0
		#red = 1
		#red = 1-blue = 0 

		color = {} #color has map

		def dfs(node):
			for nei in graph[node]:
				if nei not in color:
					color[nei] = 1 - color[node]
					if not dfs(nei):
						return False
				elif color[nei] == color[node]:
						print("color : ", color)
						return False
			return True

		#outer loop
		for node in range(len(graph)):
			print("initialy start node : ", node)
			if node not in color:
				print("start node : ", node)
				color[node] = 0
				if not dfs(node):
					return False
		return True
  

graph = [[1,3], [0,2], [1,3], [0,2]]
graph = [[1,2,3], [0,2], [0,1,3], [0,2]]

ans = Solution().isBipartite(graph)
print(ans)
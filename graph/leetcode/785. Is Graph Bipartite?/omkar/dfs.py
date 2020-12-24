#
#
#
#DOESNT WORK
#
#
#
import collections

class Solution:
	def isBipartite(self, graph):

		adjList = graph
		n  = len(graph)
		print("build adjList", adjList)

		visited = [-1] * n
		parent = [-1] * n
		color = [-1] * n


		def dfs(source):
			print("start dfs :  source : ", source)
			visited[source] = 1
			if parent[source] == -1:
				color[source] = 0
			else:
				color[source] = 1 - color[parent[source]]

			print("color[parent[source] : ", color[parent[source]])
			print("color[source] : ", color[source])
			for neighbor in adjList[source]:
				# print("loop neighbor : ", neighbor)
				if visited[neighbor] == -1:
					visited[neighbor] = 1
					parent[neighbor] = source
					if dfs(neighbor) == False:
						return False
					else:
						if color[source] == color[neighbor]:
							return False
			return True


		#outer loop
		for v in range(n):
			print("v start : ", v)
			print("visited[v]  : ", visited[v])
			if visited[v] == -1:
				if not dfs(v):
					return False
			print("=========================")

		return True
	   


graph =  [[1,3], [0,2], [1,3], [0,2]]
# graph = [[1,2,3], [0,2], [0,1,3], [0,2]]

ans = Solution().isBipartite(graph)
print(ans)
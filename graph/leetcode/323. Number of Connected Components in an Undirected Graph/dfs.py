
class Solution:
	def countComponents(self, n, edges):

		if not edges:
			return 0

		visited = [False] * (n)

		#build graph
		graph = [[] for _ in range(n)]
		for (src,dst) in edges:
			graph[src].append(dst)
			graph[dst].append(src)
			
		#bfs
		def dfs(node):
			visited[node] = True			
			for nbr in graph[node]:
				if visited[nbr] == False:
					dfs(nbr)

		#outer loop
		components = 0a
		for v in range(n):
			if visited[v] == False:
				components += 1
				dfs(v)
		return components

n = 5
edges = [[0, 1], [1, 2], [3, 4]]
# edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

		
res = Solution().countComponents(n,edges)
print(res)
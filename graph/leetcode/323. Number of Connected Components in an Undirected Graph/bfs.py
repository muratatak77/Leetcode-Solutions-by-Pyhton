class Solution:
	def countComponents(self, n, edges):
		if not edges:
			return 0

		#build graph
		graph = [[] for _ in range(n)]
		print("initial graph : ", graph)

		for (src,dst) in edges:
			print("src : ", src, " - dst :", dst)
			graph[src].append(dst)
			graph[dst].append(src)

		print("build graph : ", graph)
		visited = [False] * (n)
		print("Visited : ", visited)

		#BFS
		def bfs(s):
			print("Source: ", s)
			q = []
			q.append(s)
			visited[s] = True
			print("Visited 1  : ", visited)

			while q:
				node = q.pop()
				print("node : ", node)
				for nbr in graph[node]:
					print("visited[nbr] : ", visited[nbr], " -  nbr : ", nbr)
					if visited[nbr] == False:
						print("added nbr : ", nbr)
						q.append(nbr)
						visited[nbr] = True
						print("Visited 2 : ", visited)

		#Outer Loop
		components = 0
		for v in range(n):
			print("Visited 0  : ", visited)
			if visited[v] == False:
				print(" -------------  Call bfs for v : ", v)
				components += 1
				bfs(v)
				print("=============")
				
		return components

n = 5
edges = [[0, 1], [1, 2], [3, 4]]
# edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

		
res = Solution().countComponents(n,edges)
print(res)
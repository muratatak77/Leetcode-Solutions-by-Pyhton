import collections
class Solution():
	def validTree(self, n, edges):

		#edge cases
		# if len(edges) != n-1: 
			# return False

		#build graph
		adjList = [[] for _ in range(n)]
		for (src,dst) in edges:
			adjList[src].append(dst)
			adjList[dst].append(src)
		print("Adjlist : ", adjList)

		#build visited , parent array
		visited = [-1] * n
		parent = [""] * n

		#bfs traversal
		def bfs(source):
			q = collections.deque([source])
			visited[source] = 1
			while q:
				node = q.popleft()
				print("Node : ", node)
				for neighbor in adjList[node]:
					print("neighbor : ", neighbor)
					if visited[neighbor] == -1:
						visited[neighbor] = 1
						parent[neighbor] = node
						q.append(neighbor)
						print("q : ", q)
						print("Visited : ", visited)
						print("Parent : ", parent)
						print("=======")
					else: #neighbor has been visited
						print("parent[node] != neighbor  =  ", parent[node], " != ", neighbor)
						if parent[node] != neighbor:
							#we have cycle
							return True
						print("=======")
			return False


		#outer loop
		components = 0
		for v in range(n):
			if visited[v] == -1:
				components += 1
				if components > 1: #if has different components it is not a tree
					return False
				if bfs(v): #if cycle found, it is not a tree
					return False
		return True

			


n = 5 
edges = [[0,1], [0,2], [0,3], [1,4]]
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]

ans = Solution().validTree(n,edges)
print(ans)
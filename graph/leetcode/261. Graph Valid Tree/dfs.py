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
		print("adjList : ", adjList)

		#build visited , parent array
		visited = [-1] * n
		parent = [-1] * n

		#bfs traversal
		def dfs(node):
			print(">>>  start dfs Node : ", node)
			visited[node] = 1
			print("visited : ", visited)
			for neighbor in adjList[node]:
				print("neighbor : ", neighbor , " - node : " , node)
				if visited[neighbor] == -1:
					parent[neighbor] = node
					print("parent : ", parent)
					print("dfs(", neighbor, ")")
					if dfs(neighbor):
						print("we found dfs(neighbor) = True")
						return True
				else: #neighbor has been visited
					print("==== else start ===")
					print("parent[node] != neighbor  =  ", parent[node], " != ", neighbor)
					if parent[node] != neighbor:
						print("we found back edge True")
						#we have cycle
						return True
					print("====== else end ========")
			return False

		#outer loop
		components = 0
		for v in range(n):
			if visited[v] == -1:
				components += 1
				if components > 1: #if has different components it is not a tree
					return False
				if dfs(v): #if cycle found, it is not a tree
					return False
		return True


n = 5 
edges = [[0,1], [0,2], [0,3], [1,4]]
edges =  [[0,1], [1,2], [2,3], [1,3], [1,4]]

ans = Solution().validTree(n,edges)
print(ans)
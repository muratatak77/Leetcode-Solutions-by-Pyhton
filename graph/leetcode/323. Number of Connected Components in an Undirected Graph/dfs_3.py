	'''
	323. Number of Connected Components in an Undirected Graph

	Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

		Example 1:

		Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

		     0          3
		     |          |
		     1 --- 2    4 

		Output: 2
		Example 2:

		Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

		     0           4
		     |           |
		     1 --- 2 --- 3

		Output:  1

	------------------------------------------------------------------------

	we  need to start build a graph and adjency list to visit all necessary edges
	and we can apply dfs approach if we haven't visited before current node and we can delegate to call stack in reqursion stack
	and we need global components count. we can walk trough to start 0 to n-1 for all vertex.
'''

class Solution:
	def countComponents(self, n, edges):

		if not edges:
			return 0
		
		graph = [[] for i in range(n)]

		#build graph
		for (src,dst) in edges:
			graph[src].append(dst)
			graph[dst].append(src)

		#visited 1d array. for check visited or explored nodes or vertex
		visited = [-1] * (n)

		def dfs(node):
			visited[node] = 1
			for neighbor in graph[node]:
				if visited[neighbor] == -1:
					dfs(neighbor)

		
		#outher loop
		compenents = 0
		for v in range(n):
			if visited[v] == -1:
				dfs(v)
				compenents += 1

		return compenents

n = 5
edges = [[0, 1], [1, 2], [3, 4]]
# edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

		
res = Solution().countComponents(n,edges)
print(res)

'''
DFS Time complexity
T(N) =  O(N) > push/pop vertices 
		O(M) > looking at adjlist of each vertex
		result : O(N) + O(M)

		Looking adjlist or each node : 
		cost looking at all  neighbors : 
		
		for neighbor in graph[node]:
			if visited[neighbor] == -1:
		
			Total O(Degree(u)) Degree of that node. > 2m = O(m) 	
			Every node in the graph  cross the whole process : 2m  so twice of number of the edges

S(N = O(N) > for all call stack. Scan all edges. Like scan all tree as a top down. 
We are applying lazy manager appoarch.  we  just delegate our workers. 

'''
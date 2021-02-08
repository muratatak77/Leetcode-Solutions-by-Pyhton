'''
	we can apply for this question a graph approach. Becuase we have same pairs and we will compute these values. 
	Every node might be vertex and every compute might be a edge.
	like if we have

	[a,b] [b,c]

    graph will be :

      a/b = 2.0
	a----------->b

	  b/a = 1/2
	b----------->a

	a/b = 2      b/c = 3    a/b.b/c = 2.3 = 6

	we need to what is node neighbours and adjency list. 
	But this adj list will be multiple hash map. like : 
		
		a:{b:{2.0}}   
		
		b:{a:{0.5}, c: {3}}

	we can iterate queries. We can compute for every node by using a DFS.
		if we don't have exists node in the graph we can compute -1 
		same node will be : 1
		other 
			DFS - check neighbours.. compute getting by using the neighbours

'''

from typing import List
from collections import defaultdict

class Solution:
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

		# build graph
		# adj list
		graph = defaultdict(defaultdict)

		# fill the graph
		for (divident, divisor),value in zip(equations, values):
			graph[divident][divisor] = value
			graph[divisor][divident] = 1/value



		def DFS(curr_node, target_node, acc_product, visited):
			visited.add(curr_node)
			ret = -1
			neighbours = graph[curr_node]

			if target_node in neighbours: #we have already found
				ret = acc_product * neighbours[target_node]
			else:
				for neighbour, value in neighbours.items():
					if neighbour in visited:
						continue
					ret = DFS(neighbour, target_node, acc_product*value, visited)
					if ret != -1: # we computed and we can exit the for
						break

			visited.remove(curr_node)
			return ret


		#iterate queries
		result = []
		for divident, divisor in queries:
			if divident == divisor: # same node
				ret = 1.0
			elif divident not in graph or divisor not in graph:
				ret = -1.0
			else:
				visited = set() #we need to create into the for iterate
				ret = DFS(divident, divisor, 1, visited)
			result.append(ret)
		return result


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

res = Solution().calcEquation(equations, values, queries)
print("res : ", res)


'''
	Time complexity : 
		 N : number of input equations
		 M : number of queries

		 Build graph : O(N)

		 For each query , we need to traverse the graph. In the worst case we need to itarate entire graphs which could tane O(N)

		 = O(N.M)

	Space : 

		O(N)
		worst case we will have N edges - 2N nodes : 0(N+2N) = O(N)


'''
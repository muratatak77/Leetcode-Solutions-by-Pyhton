'''

	we can follow a path while trough the graph traversal. we can store a path in Queue. 
	When we reach  the target(n-1) we can add a result array to convert a list from  the Queue 

	We can use DFS approach.
		we can get neihbors from graph[current_node].
		we can add path q
		we can call dfs
		after dfs we should pop from q. to clean for new path.
	
	We will start every time '0'

'''

from typing import List
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

    	if not graph:
    		return graph

    	target = len(graph) - 1
    	result = []

    	def dfs(current_node, q_path):

    		if current_node == target:
    			result.append(list(q_path))
    			return 

    		for nei in graph[current_node]:
    			q_path.append(nei)
    			dfs(nei, q_path)
    			q_path.pop()

    	q_path = deque([0])
    	dfs(0, q_path)

    	return result



graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]
res = Solution().allPathsSourceTarget(graph)
print("res : ", res)


'''
	Time complexity : 
	 N : number of nodes in graph

	 How many max edges or paths between 2 nodes ? We can say could be max if we add new path.
	 like : we have 2 edges. 
	 	1 ----------> 2

	 	If we have one extra path could be new path. And we can say would be double between 2 nodes.
	 	1 -----> 3 -----> 2 
		
		would be 2^N. And for each node : T(N) = 2^N.N

	Space :
		result and each path can contain up to N nodes.  Would be same S(N) = 2^N.N 
		But we have DFS call stack. For every node takes O(N). 
		S(N) = 2^N.N  + O(N) = 2^N.N 
'''


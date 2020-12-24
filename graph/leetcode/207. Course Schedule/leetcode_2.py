'''
	source : https://www.youtube.com/watch?v=qe_pQCh09yU&ab_channel=TECHDOSE

	This is a Topological Sort Alg.  question.
	Our graph will be Directed Acyclic Graph (DAG) : A directed graph with no cycle is called DAG.

	Topological  sort for a graph is possible only it is a DAG.
	If we have cycle in the graph meaning we have a impossible situation. We can not take course by the ordering
	
	Like :  
		1 --> 2 
		1 --> 3 
		2 --> 4 
		3 --> 4
		This is a acyclic graph
		we don't have a cycle in this adjency list. we can say DAG
	
	But if we have like this graph : 
		1 --> 2 
		2 --> 4
		4 --> 3
		3 --> 1
		it is not a DAG. Because there is a cycle in this graph.
	

	What is Topological order : 
		it is a linear ordering of vertices such that for every directed edge UV(U > V), vertex U comes before vertex V in the ordering.

		if we have edges U ---> V then in the top sort we can write as (U,V). We can not write (V,U).

	
	We can use DFS appoarch because we need to reach every node and its neighbours. 
	we can use a stack for keep topological sorted.
	We can use 3 colors for level or visiting nodes. 

	WHITE : 1 
	GRAY : 2
	BLACK : 3 
	
	level : 1
	 - default all adjacency nodes will be WHITE

	level : 2
	 - after visiting a node we can change color to GRAY
	 - if we have same neigbors color  ==  GRAY there is a cycle. we can return empty []

	 level : 3 
	 - after dfs recursion and scan all neighbors we can change color as a BLACK
	 - and we can add current node to stack for result

'''

from collections import defaultdict
class Solution:

	WHITE = 1
	GRAY = 2
	BLACK = 3

	def findOrder(self, numCourses, prerequisites):

		#create adj_list
		adj_list = defaultdict(list)

		#filling adj list for directed graph
		for (dst,src) in prerequisites:
			adj_list[src].append(dst)

		topological_sort = [] # a stack

		#we can use to keep color change check.
		#default all color white.
		
		color = {}
		for k in range(numCourses):
			color[k] = Solution.WHITE

		is_possible = True

		#dfs
		def dfs(node):
			nonlocal is_possible

			if is_possible is False:
				return

			color[node] = Solution.GRAY

			#start the recursion
			if node in adj_list:
				for nei in adj_list[node]:
					if color[nei] == Solution.WHITE:
						dfs(nei)
					elif color[nei] == Solution.GRAY: # we have cycle. 
						is_possible = False

			#after recursion we marked BLACK
			color[node] = Solution.BLACK
			topological_sort.append(node)


		#aouter loop
		for vertex in range(numCourses):
			if color[vertex] == Solution.WHITE:
				dfs(vertex)


		#result
		if not is_possible:
			return False
		else:
			return True
		


numCourses = 2
prerequisites = [[1,0],[0,1]]
prerequisites = [[1,0]]


# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]

# numCourses = 5
# prerequisites = [[1,0],[2,0],[3,1],[3,2],[2,3]]


ans = Solution().findOrder(numCourses, prerequisites)
print("ans : ", ans)


'''
 T(N) = O(V+E) V represents the number of vertices and E represents the number of edges.
	We iterate each through each node and each vertex in the graph

 S(N) = O(V+E)

	 We use the adjacency list to represent our graph initially. 
	 The space occupied is defined by the number of edges because for each node as the key, we have all its adjacent nodes in the form of a list as the value. 
	 Hence, O(E)

	Additionally, we apply recursion in our algorithm, which in worst case will incur O(E) extra space in the function call stack.

'''

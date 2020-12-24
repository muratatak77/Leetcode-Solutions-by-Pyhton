'''
	we can apply color changing by the node. One node is red its neighbors should be other color. 
	firstly, We need a adj list.
	and color hash map we will keep which nodes or vertex depend which edges.

	adj list

	1 > 2,3
	2 > 1,4
	3 > 1
	4 > 2

	1    > Blue = 0
  2   3  > Red  = 1 must be
 

''' 

import collections

def possibleBibartite(N, dislikes):

	if not dislikes:
		return False

	adj_list = collections.defaultdict(list)
	# build graph
	for src,dst in dislikes:
		adj_list[src].append(dst)
		adj_list[dst].append(src)
	
	color = {}

	#bfs method
	def bfs(node):
		q = collections.deque([node])
		while q:
			node = q.popleft()
			for nei in adj_list[node]:
				if nei not in color:
					q.append(nei)
					color[nei] = 1 - color[node]
				elif color[nei] == color[node]: # if nei has same color with its node 
					return False
		return True

	#OUTER LOOP
	for node in range(1,N+1):
		if node not in color:
			color[node] = 0
			if not bfs(node):
				return False
	return True

N = 4
dislikes = [[1,2],[1,3],[2,4]]
# dislikes = [[1,2],[1,3],[2,3]]

ans = possibleBibartite(N, dislikes)
print(ans)

'''
N = Number of nodes in the graph 
E = Number of edges
We explore each node one when we transform it from uncolored to colored , traversing all in edges in the process
T(N) = O(N+E) 
Space : O(N) the space used to store the color
'''
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

	if dislikes is None:
		return False

	if len(dislikes) != N:
		return True

	adj_list = collections.defaultdict(list)
	# build graph
	for src,dst in dislikes:
		adj_list[src].append(dst)
		adj_list[dst].append(src)
	print("adj_list: ", adj_list)
	color = {}

	#dfs method
	def dfs(node):
		for nei in adj_list[node]:
			if nei not in color:
				color[nei] = 1 - color[node]
				if not dfs(nei):
					return False
			elif color[nei] == color[node]: # if nei has same color with its node 
				return False
		return True

	#OUTER LOOP
	#Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
	for node in range(1,N+1):
		if node not in color:
			color[node] = 0
			if not dfs(node):
				return False
	return True


N = 1
dislikes = [[1,2],[1,3],[2,4]]
# dislikes = [[1,2],[1,3],[2,3]]
dislikes = []

ans = possibleBibartite(N, dislikes)
print(ans)

'''
T(N) = O(N+E)
 		N : Number of edges in the graph
 		E : length of dislikes 

S(N = O(N) > for all call stack. Scan all edges. Like scan all tree as a top down. 
'''
'''
	adj list

	1 > 2,3
	2 > 1,4
	3 > 1
	4 > 2

	1    > Blue = 0
  2   3  > Red  = 1

''' 

import collections

def possibleBibartite(N, dislikes):

	#build graph
	adjList = collections.defaultdict(list)
	for src, dst in dislikes:
		adjList[src].append(dst)
		adjList[dst].append(src)

	print("Build adjList : ", adjList)

	color = {}

	def bfs(node):
		q = collections.deque([node]) #1
		while q:
			node = q.popleft() #1
			print("node popleft: ", node)
			for nei in adjList[node]: #2,3
				print("get nei : ", nei)
				if nei not in color:
					q.append(nei) # 2
					color[nei] = 1 - color[node] # 1
					print("color inside: ", color)
					print("q : ", q)
					print("========")
				else:
					# print("node :", node)
					# print("nei :", nei)
					print("try match color[nei] == color[node] : ", color[nei],"==", color[node])
					if color[nei] == color[node]:
						print("nei : ", nei , " - node : ", node)
						print("color :", color)
						return False # we have cycle , we have different color match
		print("color : ", color)
		return True


	#outer loop
	for node in range(1,N+1):
		if node not in color:
			color[node] = 0
			if not bfs(node): 
				return False
	return True


N = 4
dislikes = [[1,2],[1,3],[2,4]]
dislikes = [[1,2],[1,3],[2,3]]

ans = possibleBibartite(N, dislikes)
print(ans)
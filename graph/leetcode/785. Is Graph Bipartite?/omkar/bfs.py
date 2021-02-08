import collections

class Solution:
    def isBipartite(self, graph):

    	adjList = graph
    	n  = len(graph)
    	print("build adjList", adjList)

    	visited = [-1] * n
    	parent = [-1] * n
    	distance = [-1] * n

    	print("build distance", distance)

    	def bfs(source):
    		print("start bfs :  source : ", source)
    		visited[source] = 1
    		distance[source] = 0
    		print("distance add source : ", distance)
    		print("visited add source : ", visited)
    		q = collections.deque([source])
    		print("first q : ", q) 
    		while q:
    			node = q.popleft()
    			print("pop node : ", node)
    			for neighbor in adjList[node]:
    				print("loop neighbor : ", neighbor)
    				print("visited[neighbor] : ", visited[neighbor])
    				if visited[neighbor] == -1:
    					visited[neighbor] = 1
    					parent[neighbor] = node
    					distance[neighbor] = distance[node] + 1
    					q.append(neighbor)
    					print("distance[neighbor]  : ", distance[neighbor])
    					print("distance[node]  : ", distance[node])
    					print("distance finally :", distance)
    					print("inside parent  : ", parent)
    					print("after add q ; ", q)
    					print("already visited : ", visited)
    				else:
    					print("already visited : ", visited)
    					print("else parent[node] : ", parent[node], " - neighbor : ", neighbor)
    					if parent[node] != neighbor:
    						#we have cycle
    						print("we have cycle.")
    						print("else distance[node] : ", distance[node])
    						print("else distance[neighbor] : ",distance[neighbor])
    						if distance[node] == distance[neighbor]:
    							return False
    				print("==========")

    		return True



    	#outer loop
    	for v in range(n):
    		print("v start : ", v)
    		print("visited[v]  : ", visited[v])
    		if visited[v] == -1:
    			if bfs(v) == False:
    				return False
    		print("=========================")

    	return True
       


graph = [[1,3], [0,2], [1,3], [0,2]]
graph = [[1,3], [0,2], [1,3,4], [0,2],[4]]

ans = Solution().isBipartite(graph)
print(ans)
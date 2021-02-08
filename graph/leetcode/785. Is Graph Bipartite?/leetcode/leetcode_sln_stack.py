class Solution:
    def isBipartite(self, graph):

    	#blue = 0
    	#red = 1
    	#red = 1-blue = 0 

    	color = {} #color has map

    	for node in range(len(graph)):
    		print("node : ", node)
    		if node not in color:
    			print("node not in color : ", node)

    			stack = [node]
    			print("stack : ", stack)
    			color[node] = 0
    			print("color : ", color)
    			print("===========-------- while start  --------========")
    			while stack:
    				node = stack.pop()
    				print("Pop node : ", node)
    				print("for nei in graph[node] :", graph[node])
    				for nei in graph[node]:
    					print("=========== for start ========")
    					print("nei : ", nei)
    					print("check nei not in color  = nei : ", nei , " - color : ", color )
    					if nei not in color:
    						print("node : ", node)
    						stack.append(nei)
    						print("stack append : ", stack)
    						color[nei] = 1 - color[node]
    						print("color[nei] = 1 - color[node] : ","color[",nei,"]" , " = 1 - " , color[node])
    						print("color[nei] = ", color[nei])
    						print("color finally : ", color)
    					else:
    						print("node :", node)
    						print("nei :", nei)
    						print("try match color[nei] == color[node] : ", color[nei],"==", color[node])
    						if color[nei] == color[node]:
    							print("color[nei] == color[node] : " , color[nei] , " == ", color[node])
    							return False
    				print("=========== for end ========")
    			print("===========-------- while end  --------========")
    	return True
  

graph = [[1,3], [0,2], [1,3], [0,2]]
graph = [[1,2,3], [0,2], [0,1,3], [0,2]]

ans = Solution().isBipartite(graph)
print(ans)
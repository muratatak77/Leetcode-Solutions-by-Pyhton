
'''
	we can apply DFS or BFS approaching for this question.
	I ll try DFS.
	
	we need to understand question main problem.
	We nxn grid. We don't think rows and columns length

         j

	   0  1  2
	0 [1, 1, 0]
i
	1 [1, 1, 0]

	2 [0, 0, 1]

	0 and 0 connected city
	0 and 1 connected
	0 and 2 is not connected
	we can say 
	 	
	 	0-----1
	 	|
	 	2

	 	in DFS traversal, we need to keep a visited array or hash.
	 	when ve visit 0 and 1 means : 
	 	visited[0] = 1
	 	visited[1] = 1 

	 	we don't need again visit row 1 , because we already connected city. and our global count will be 2

		but we don't have visited[2]. 
	finally we can visit last 2-2 cell. we can increment our global answer .

	we have totaly 2 provinces
             
'''
from typing import List
class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:

		#we can iterate i , row
		n = len(isConnected)
		visited = [0] * n
		count = 0

		def dfs(visited, i):
			for j in range(n):
				print("		i : ", i, " - j : ", j)
				#is there a connection and not visited before
				print("		isConnected[i][j] : ", isConnected[i][j] ,  " - visited[j] : ", visited[j])
				if isConnected[i][j] == 1 and visited[j] == 0:
					visited[j] = 1
					print("			visited : ", visited)
					print("			Call DFS : visited : ", visited , " - j : ", j)
					dfs(visited, j)
				print("=================== ============== ===========")

	
		for i in range(n):
			print(" i : ", i)
			if visited[i] == 0:
				dfs(visited, i)
				count += 1
				print("	count : ", count)
			print("---------------------")

		return count



isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# isConnected = [[1,0,0],[0,1,0],[0,0,1]]

isConnected = [
[1,0,0,1],
[0,1,1,0],
[0,1,1,1],
[1,0,1,1]
]
ans = Solution().findCircleNum(isConnected)
print(ans)

'''
	we can apply DFS or BFS approaching for this question.
	I ll try BFS.
	
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

	 
	we have totaly 2 provinces
             
'''
from typing import List
from collections import deque

class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:

		#we can iterate i , row
		n = len(isConnected)
		visited = [0] * n
		count = 0
		q = deque()


		for i in range(n):
			print(" i : ", i, "visited : ", visited)
			if visited[i] == 0:
				q.append(i)
				print("		Q Append : ", q)
				while q:
					node = q.pop()
					print(" 		Q POP : ", node)
					visited[node] = 1
					print(" 		visited : ", visited)

					for j in range(n):
						print(" 				j : ", j)
						if isConnected[i][j] == 1 and visited[j] == 0:
							q.append(j)
							print("					Q Append J: ", q)
				print("==========================")


				count += 1

		return count



isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# isConnected = [[1,0,0],[0,1,0],[0,0,1]]

# isConnected = [
# [1,0,0,1],
# [0,1,1,0],
# [0,1,1,1],
# [1,0,1,1]
# ]
ans = Solution().findCircleNum(isConnected)
print(ans)
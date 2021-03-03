'''
	BFS approaching. Because we need level traversal order. 
	We need go to neighbours then other neighbours.
	
	Look images in the folder. 

'''
from typing import List
from collections import deque

class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:

		q = deque()
		ROWS = len(grid) 
		COLS = len(grid[0])
		fresh_oranges = 0

		#step 1. we initial rotten oranges and fresh oranges count
		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c] == 2:
					q.append((r,c))
				elif grid[r][c] == 1:
					fresh_oranges += 1

		# we can mark time elapsed for every level/round
		q.append((-1,-1))

		print("start fresh_oranges : ", fresh_oranges)
		print(" Initial Q : ", q)
		print("------------------------")

		#step 2, start the rotting process via BFS
		minutes_elasped = -1
		directions = [(1,0),(-1,0),(0,1),(0,-1)]
		while q:
			print(" While starting Q : ", q)
			row , col = q.popleft()
			print(" 	POPLEFT Q:", row,",",col)

			if row == -1: #if we completed one round
				minutes_elasped += 1
				print(" 		Decrease minutes_elasped : ", minutes_elasped)
				if q: #to avoid endless loop
					q.append((-1,-1))

			else:
				#this is the rotten orange
				#it would conteminate its neighbours
				for d in directions:
					dx = row + d[0]
					dy = col + d[1]
					if 0<= dx < ROWS and 0<= dy < COLS and grid[dx][dy] == 1:
						grid[dx][dy] = 2 #would be contamined , like visited array
						fresh_oranges -= 1
						q.append((dx,dy)) #this orange would be contamined other oranges via q
			print("==================")

		print("start fresh_oranges : ", fresh_oranges)
		
		if fresh_oranges == 0:
			return minutes_elasped
		else:
			return -1


grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[0,1]]
res = Solution().orangesRotting(grid)
print("res : ", res)


'''
	T(N) = O(N) = N  is the size of  grid. 
	S(N) = O(N) in the worst case the grid filled all rotten oranges. As a result, the q in the initalize with all the cell grid.

	Output : 

grid = [[2,1,1],[1,1,0],[0,1,1]]


 Initial Q :  deque([(0, 0), (-1, -1)])
	------------------------
	 While starting Q :  deque([(0, 0), (-1, -1)])
	 	POPLEFT Q: 0 , 0
	==================
	 While starting Q :  deque([(-1, -1), (1, 0), (0, 1)])
	 	POPLEFT Q: -1 , -1
	 		Decrease minutes_elasped :  0
	==================
	 While starting Q :  deque([(1, 0), (0, 1), (-1, -1)])
	 	POPLEFT Q: 1 , 0
	==================
	 While starting Q :  deque([(0, 1), (-1, -1), (1, 1)])
	 	POPLEFT Q: 0 , 1
	==================
	 While starting Q :  deque([(-1, -1), (1, 1), (0, 2)])
	 	POPLEFT Q: -1 , -1
	 		Decrease minutes_elasped :  1


	==================
	 While starting Q :  deque([(1, 1), (0, 2), (-1, -1)])
	 	POPLEFT Q: 1 , 1
	==================
	 While starting Q :  deque([(0, 2), (-1, -1), (2, 1)])
	 	POPLEFT Q: 0 , 2
	==================
	 While starting Q :  deque([(-1, -1), (2, 1)])
	 	POPLEFT Q: -1 , -1
	 		Decrease minutes_elasped :  2


	==================
	 While starting Q :  deque([(2, 1), (-1, -1)])
	 	POPLEFT Q: 2 , 1
	==================
	 While starting Q :  deque([(-1, -1), (2, 2)])
	 	POPLEFT Q: -1 , -1
	 		Decrease minutes_elasped :  3


	==================
	 While starting Q :  deque([(2, 2), (-1, -1)])
	 	POPLEFT Q: 2 , 2
	==================
	 While starting Q :  deque([(-1, -1)])
	 	POPLEFT Q: -1 , -1
	 		Decrease minutes_elasped :  4

	==================
	res :  4
[Finished in 0.0s]


'''
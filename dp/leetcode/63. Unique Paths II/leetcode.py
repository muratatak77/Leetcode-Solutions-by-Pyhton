from typing import List
class Solution:
	def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
		
		m = len(grid) # rows
		n = len(grid[0]) # cols

		table = [[0] * m for _ in range(n)]
		
		if grid[0][0] == 1:
			return 0
		
		table[0][0] = 1

		for row in range(1,m):
			if grid[row][0] == 1:
				break
			table[row][0] = 1
		
				
		# fill the first col 
		for col in range(1,n):
			if grid[0][col] == 1:
				break
			table[0][col] = 1
		
		# print("grid : ", grid)

			
		# iterate left cells
		for row in range(1,m):
			for col in range(1,n):
				if grid[row][col] == 1:
					grid[row][col] = 0
				else:
					#equation for last cell in grid
					#f(i,j) = f(i-1,j) + f(i,j-1)
					table[row][col] = table[row-1][col] + table[row][col-1]
		
		# print("grid : ", grid)
		#return last cell in grid
		return table[m-1][n-1]
			

grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

grid = [[0,1],[0,0]]


grid =  [[0]]

grid = [[0,0]]

ans = Solution().uniquePathsWithObstacles(grid)
print(ans)
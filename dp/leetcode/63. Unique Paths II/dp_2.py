'''
	We have a mxn grid.  we can try to find a uniq path inside the gtid. That's why this is a DP problem. 
	
	Robot can go only left and down. if the robot go left and down , meaning we have totaly 2 way. 
		if there is an obstacle in any cell we can use this way again. And we can put 0 , meaning we won't that cell contribute to any path.

	We will iterate the row inside the col of row by the computing cell value.

		inside this iterate we can compute cell to reach last cell.

			if we don't have obstacle = 1
				we can pass 0 , meaning not reachable. 0 doesnt have any effect for total.
			else
				we can say our equation
				m = row, n = col
				f(m,n) = f(m-1,n)+f(m, n-1)
					meaning we can sum left cell total paths +  down cell total path to pass last cell in grid.

'''

from typing import List
class Solution:
	def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
		print("Original Grid :", grid)
		#rows length
		R = len(grid)
		#cols lenght
		C = len(grid[0])

		# print("R : ", R)
		# print("C : ", C)

		#edge case. if we have 1 in the first cell
		if grid[0][0] == 1:
			return 0

		grid[0][0] = 1 # reacing 

		# print("grid 0: ", grid)

		# filling first col by the 1 val of the grid if we don't have any obstacle
		for i in range(1,R):
			if grid[i][0] == 0 and grid[i-1][0] == 1:
				# print("		i : ", i)
				# print("		grid[i][0] == 0 and grid[i-1][0] == 1: ", grid[i][0] ,"==", 0, "and", grid[i-1][0], "==", 1 )
				grid[i][0] = 1
			else:
				grid[i][0] = 0

		# print("grid 1: ", grid)

		# we need to fill by 1 top col of grid if we don't have any obstacle
		for j in range(1,C):
			if grid[0][j] == 0 and grid[0][j-1] == 1:
				# print("		j : ", j)
				# print("		grid[0][j] == 0 and grid[0][j-1] == 1: ", grid[0][j] ,"==", 0, "and", grid[0][j-1], "==", 1 )
				grid[0][j] = 1
			else:
				grid[0][j] = 0

		# print("grid 2 : ", grid)

		for i in range(1,R):
			for j in range(1,C):
				print("			i :" , i, " - j :", j)
				if grid[i][j] == 0:
					#f(m,n) = f(m-1,n)+f(m, n-1)
					grid[i][j] = grid[i-1][j] + grid[i][j-1]
				else:
					grid[i][j] = 0

		return grid[R-1][C-1]

grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

# grid = [[0,1],
# 		[0,0]
# 		]

# grid = [[0,0]]

ans = Solution().uniquePathsWithObstacles(grid)
print(ans)

'''
	T(N) = 	O(MxN)
			M : row, N : col 
			would be number of sub problems. Our grid size MxN =
			Each cell takes constant amout of time.
			
	S(N) = we don't use any extra space = O(1)
'''
        
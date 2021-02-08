class Solution:
	def numIslands(self, grid):

		#print("X Len(Grid) :" , len(grid))
		#print("Y len(grid): ", len(grid[0]))

		def dfs(x,y):
			if (x<0) or (y<0) or (x>=len(grid)) or ( y >=len(grid[0]) ) or (grid[x][y] == 0):
				return 0

			if grid[x][y] == 1:
				result = 1
		
			grid[x][y] = 0
			result += dfs(x-1, y) + dfs(x+1,y) + dfs(x, y-1) + dfs(x, y+1)
			return result

			
		max_island = 0
		for x in range(len(grid)):
			for y in range(len(grid[0])):
				if grid[x][y] != 0: 
					max_island = max(dfs(x,y), max_island)
		return max_island


# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# grid = [
# [1,1,0,0,0],
# [1,1,0,0,0],
# [0,0,0,1,1],
# [0,0,0,1,1]]
#print("grid : ", grid)

ans = Solution().numIslands(grid)
print(ans)

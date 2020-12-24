class Solution:
	def numIslands(self, grid):

		print("X Len(Grid) :" , len(grid))
		print("Y len(grid): ", len(grid[0]))


		def getneighbors(x,y):
			print(">>>>> Start getneighbors  x : ", x , " , y :",  y)

			result  = []

			if x+1 < len(grid):
				print("x+1 : ", x+1 , " < ", len(grid))
				result.append((x+1, y))

			if y+1 < len(grid[0]):
				print("y+1 : ", y+1 , " < ", len(grid[0]))
				result.append((x, y+1))

			if x-1 >= 0:
				print("x-1 : ", x-1 , " >= 0")
				result.append((x-1,y))

			if y-1 >= 0:
				print(" y-1 : ",  y-1 , " >= 0")
				result.append((x,y-1))

			print("<<<<<< Finished getneighbors  result : ", result)

			return result


		def dfs(x,y):
			grid[x][y] = '0'
			neighbors = getneighbors(x,y)
			for (nr, nc) in neighbors:
				if grid[nr][nc] != '0':
					dfs(nr,nc)
			

		island = 0
		for x in range(len(grid)):
			for y in range(len(grid[0])):
				if grid[x][y] != '0':
					dfs(x,y)
					island += 1
		return island



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0"],
  ["1","1","0"],
  ["0","0","1"]
]


grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]


print("grid : ", grid)

ans = Solution().numIslands(grid)
print(ans)

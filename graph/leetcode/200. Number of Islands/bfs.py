import collections

class Solution:
	def numIslands(self, grid):

		print("X Len(Grid) :" , len(grid))
		print("Y len(grid): ", len(grid[0]))


		def getneighbors(x,y):
			print("---------------")
			print("Start x : ", x , " , y :",  y)

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

			print("result : ", result)
			print("---------------")

			return result


		def bfs(x,y):
			q = collections.deque()
			q.append((x,y))
			print("First q append : ", q)
			grid[x][y] = '0'
			while q:
				row,col = q.popleft()
				print("after popleft : row : ", row , " - col : ", col, "  - q : ", q)
				neighbors = getneighbors(row, col)
				print("neighbors : ", neighbors)
				for (nr, nc) in neighbors:
					if grid[nr][nc] != '0':
						q.append((nr,nc))
						grid[nr][nc] = '0'
						print("Q append : ", q)
						print("grid finally: ", grid)
						print("==========")
				print("===================")

			
  

		island = 0
		for x in range(len(grid)):
			for y in range(len(grid[0])):
				if grid[x][y] != '0':
					bfs(x,y)
					island += 1
		return island



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]


print("grid : ", grid)

ans = Solution().numIslands(grid)
print(ans)

'''
	we can apply DFS approach
	be carefull out of the grid

				  c-1

		r-1     1,1,1,0
		r+1     1,1,0,0         

				  c+1

'''             

class Solution:
	def numIslands(self, grid):

		def getNeighbors(r,c):
			result = []

			if r+1 < len(grid):
				result.append((r+1,c))

			if c+1 < len(grid[0]):
				result.append((r,c+1))
			if r-1 >= 0:
				result.append((r-1,c))
		
			if c-1 >= 0:
				result.append((r,c-1))

			return result

		def dfs(r,c):
			grid[r][c] = '0'
			neighbours = getNeighbors(r,c)
			for nr,nc in neighbours:
				if grid[nr][nc] != '0':
					dfs(nr, nc)

	
		island = 0
		for r in range(len(grid)):
			for c in range(len(grid[0])):
				if grid[r][c] != '0':
					dfs(r,c)
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


grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]


print("grid : ", grid)

ans = Solution().numIslands(grid)
print(ans)

'''
	T(N) = O(MN) M = rows, N = cols
	O(S) = O(MN) grid by MN
'''
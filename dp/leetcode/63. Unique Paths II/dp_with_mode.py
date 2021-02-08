def uniquePathsWithObstacles(grid):

	m = len(grid)
	n = len(grid[0])

	priny("m : ", m)

	table = [ [0] * m for _ in range(n)]

	print("Build table : ", table)

	#base case
	#top-left corner
	if grid[0][0] == 1:
		return 0
	

	table[0][0] == 1

	#top row
	for col in range(1,n):
		if grid[0][col] == 1:
			break
		table[0][col] = 1

	#top col
	for row in range(1,m):
		if grid[row][0] == 1:
			break
		table[row][0] = 1

	for row in range(1,m):
		for col in range(1,n):
			if grid[row][col] == 1:
				table[row][col] = 0
			else:
				table[row][col] = table[row-1][col] + table[row][col-1]

	return table[m-1][n-1]



grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

grid = [[0,1],
		[0,0]
		]

grid = [[0,0]]

ans = uniquePathsWithObstacles(grid)
print(ans)


        
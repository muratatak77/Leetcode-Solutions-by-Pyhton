def maxPath(grid):

	#build extra grid for keep and caching vertex
	##base case
	m = len(grid)
	n = len(grid[0])
	# table = [[None]*n for _ in range(m)]
	table = grid
	print("Build Table from scracth : ", table)

	table[0][0] = grid[0][0]

	for j in range(1,n):
		table[0][j] = table[0][j-1] + grid[0][j]

	for i in range(1,m):
		table[i][0] = table[i-1][0] + grid[i][0]

	print("Build Table in base case : ", table)

	#internal computing case
	for row in range(1,m):
		for col in range(1,n):
			table[row][col] = grid[row][col] + max(table[row-1][col], table[row][col-1])

	print("Build Table internal computing case : ", table)

	return table[m-1][n-1]


grid = [
[1,3,1],
[1,5,1],
[4,2,1]
] 
	
ans = maxPath(grid)
print(ans)
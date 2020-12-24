def countPaths(m,n):
	size = m*n
	
	table = [[None]*n for _ in range(m)]

	print(table)

	for i in range(m):
		table[i][0] = 1

	print("table 1 :", table)


	for j in range(n):
		table[0][j] = 1

	print("table 2 :", table)

	for row in range(1,m):
		for col in range(1,n):
			#compute table[row][col]
			table[row][col] = table[row-1][col]+table[row][col-1]

	print("table 2 :", table)

	return table[m-1][n-1]


ans = countPaths(3,3)
print(ans)


def numberOfPaths(matrix):

	#top-left corner
	if matrix[0][0] == 0:
		return 0
	
	if matrix[-1][-1] == 0:
		return 0

	m = len(matrix)
	n = len(matrix[0])

	if n == 1 and m == 1:
		if matrix[0][0] == 1:
			return 1

	MOD = (10**9) + 7

	table = [ [0] * n for _ in range(m)]
	print("table 0 ", table)


	#base case
	table[0][0] == 1

	print("table 1 ", table)

	#top row
	for col in range(1,n):
		if matrix[0][col] == 0:
			break
		print("col : ", col)
		table[0][col] = 1

	#top col
	for row in range(1,m):
		print(matrix[row][0])
		if matrix[row][0] == 0:
			break
		table[row][0] = 1

	print("table  2 ", table)

	for row in range(1,m):
		for col in range(1,n):
			if matrix[row][col] == 1:
				table[row][col] = ( table[row-1][col] + table[row][col-1] ) % MOD

	print("table  3 ", table)

	return table[m-1][n-1]


matrix = [
  [1,1,1,1],
  [1,1,1,1],
  [1,1,1,1]
]

# matrix = [
#   [1,1],
#   [1,0]
# ]

# matrix = [
#   [1,1],
#   [0,1]
# ]



# matrix = [ 
# [1, 1, 0],
# [1, 1, 0],
# [0, 0, 1]]


matrix = [ [1, 1, 1, 0, 1, 1, 1] ]

# matrix = [[1]]

ans = numberOfPaths(matrix)
print(ans)



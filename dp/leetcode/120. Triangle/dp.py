def minTotal(triangle):
		
	row_size = len(triangle)
	print("row_size : ", row_size)

	#set up table with the same size as the triangular triangle
	table = [[0 for cols in range(row_size)] for _ in range(row_size)] 
	print("table : ", table)

	#set up base cases
	table[0][0] = triangle[0][0]

	print("table 2: ", table)

	#base case
	#we can summaziation left and right side cells values
	#we have just one way for the first 2 row because the first row has just one value, the second row has just 2 values. 
	for row in range(1,row_size):
		table[row][0] = table[row-1][0] + triangle[row][0]
		table[row][row] = table[row-1][row-1] + triangle[row][row]

	print("table 3: ", table)

	#General traversal cases
	#Our recurrence equation in pascal triangle appoarch:
	# f(i,j) = min(col[i-1][j-1], col[i-1][j]) + triangle[i][j]
	#start from row 2 
	for row in range(2,len(table)):
		for col in range(1,row):
			print("   row , col :",  row, col)
			print("		min(table[row-1][col-1], table[row-1][col]) :", min(table[row-1][col-1], table[row-1][col]))
			print("		triangle[row][col] : ", triangle[row][col])
			table[row][col] = min(table[row-1][col-1], table[row-1][col]) + triangle[row][col]
			print("	      table :", table)
	
	print("table 3: ", table)
	
	return min(table[-1])

triangle = [
	 [2],
	[3,4],
   [6,5,7],
  [4,1,8,3]
]


ans = minTotal(triangle)
print(ans)
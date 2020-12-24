#doesnt
def triangle(rowNumbers):
	

	table = [ [1] * (rowNumbers) for row in range(rowNumbers)]

	# table[0][0] = 1

	# for col in range(1,n):
	# 	table[0][col] = 1

	# for row in range(1,m):
	# 	table[row][0] = 1

	print("table : ", table)

	for row in range(2,len(table)):
		for col in range(1,row):
			table[row][col] = table[row-1][col] + table[row-1][col-1]


	print("Finally table: " , table)

	return table

rowNumbers = 5
ans = triangle(rowNumbers)
print("ans : ", ans)
def countStairs(n):

	table = [None] * n

	table[1] = 1
	table[2] = 2

	print(table)

	for i in range(3,n+1):
		table[i%3] = table[(i-1)%3] + table[(i-2)%3]

	print(table)

	return table[(n-1)%3]


ans  = countStairs(9)
print(ans)
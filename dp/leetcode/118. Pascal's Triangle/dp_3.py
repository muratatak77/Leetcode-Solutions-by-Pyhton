'''
	we need a 2D array DP table.
	we can fill all cell is 1 as intially

	for i in range(2,len(dp))
		for j in range()
			

 	 	j =	0,1,2,3 
	i=0 	1
	i=1		1 1
	i=2		1 2 1
			1 3 3 1 


		we can start i=2 , j = 1 



'''
def triangle(rowNumbers):


	dp = [[1 for _ in range(rowNumbers) ] for _ in range(rowNumbers)]

	print("dp : ", dp)

	for i in range(2,len(dp)):
		for j in range(1,i):
			dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
			

	print("dp : ", dp)
	return dp

rowNumbers = 5
ans = triangle(rowNumbers)
print("ans : ", ans)
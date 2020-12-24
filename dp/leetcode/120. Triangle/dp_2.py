'''
	we can find first row size to iterate.


'''
def minTotal(triangle):

	row_size = len(triangle)

	# we need a extra 2D table , we can fill 0 all cells
	table = [[0 for _ in range(row_size)] for _ in range(row_size)]

	#base cases 1
	# we can set first cell directly
	table[0][0] = triangle[0][0]
	
	#base cases 2
	# we need to fill left and right side first
	# we can go by doing the summaization for every side
	for i in range(1,row_size):
		table[i][0] = table[i-1][0] + triangle[i][0] 
		table[i][i] = table[i-1][i-1] + triangle[i][i]

	# general traversal case
	# we can fill inside
	for r in range(2,len(table)):
		for c in range(1,r):
			table[r][c] = min(table[r-1][c-1], table[r-1][c]) + triangle[r][c]
	

	return min(table[-1])


triangle = [
	[2],
	[3,4],
    [6,5,7],
    [4,1,8,3]
]


ans = minTotal(triangle)
print(ans)


''''
	T(N) = O(N^2)
	S(T) = O(N^2)
	

'''
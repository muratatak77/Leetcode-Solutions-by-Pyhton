# https://leetcode.com/problems/triangle/discuss/824306/C%2B%2B-or-O(1)-Memory-or-NO-EXTRA-ARRAY-USED-or-5-Lines

def minTotal(triangle):

	n = len(triangle)
	for i in range(n-2,-1,-1):
		for j in range(0,len(triangle[i])):
			triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
	
	print("triangle : ", triangle)

	return triangle[0][0]

triangle = [
	 [2],
	[3,4],
   [6,5,7],
  [4,1,8,3]
]


ans = minTotal(triangle)
print(ans)
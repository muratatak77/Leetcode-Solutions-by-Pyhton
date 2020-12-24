class Solution(object):
	def minimumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		if len(triangle) == 1:
			return triangle[0][0]
		min_total = float("inf")
		
		for i in range(1, len(triangle)):
			for j in range(len(triangle[i])):
				print("i : ", i ,  " - j :", j)
			 	# base cases: first and last column.
				if j == 0:
					triangle[i][j] += triangle[i-1][j]
					print(" First element.j == 0. Triangle :", triangle)
				elif j == len(triangle[i]) - 1:
					triangle[i][j] += triangle[i-1][j-1]
					print("	j final element. Triangle :", triangle)

				else:
					triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
					print("	j inside element. Triangle :", triangle)

			 	 # if we are in the last row, update the min_total if necessary. `
				if i == len(triangle) - 1:
					min_total = min(min_total, triangle[i][j])
					print("			i last element : Triangle ", triangle)
					print("			min_total : ", min_total)

				print(" --------------------------------------  ")
		return min_total




triangle = [
	[2],
	[3,4],
	[6,5,7],
	[4,1,8,3]
]


ans = Solution().minimumTotal(triangle)
print(ans)
from typing import List
class NumMatrix:

	def __init__(self, matrix: List[List[int]]):
	
		m = len(matrix) #row
		n = len(matrix[0]) #col

		print("m (row) :", m)
		print("n (column):", n)

		if m == 0 or n == 0:
			self.ps = []
			return

		ps = [[0 for _ in range(n)] for _ in range(m)]

		ps[0][0] = matrix[0][0]

		# print("Pre sum : ", ps)
		
		#first row filling
		for row in range(1,m):
			ps[row][0] = ps[row-1][0] +  matrix[row][0]

		# print("Pre sum : ", ps)

		#first column filling
		for col in range(1,n):
			ps[0][col] = ps[0][col-1] + matrix[0][col]

		# print("Pre sum : ", ps)

		for row in range(1,m):
			for col in range(1,n):
				print("row-col : ",row, "-", col)
				ps[row][col] = ps[row-1][col] + ps[row][col-1] - ps[row-1][col-1] + matrix[row][col]
				print("	ps :", ps)
		print("Pre sum : ", ps)

		self.ps = ps

	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

		if len(self.ps) == 0 or len(self.ps[0]) == 0:
			return 0
		elif row1 == 0 or col1 == 0:
			return self.ps[row2][col2]
		elif row1 == 0:
			return self.ps[row2][col2] - self.ps[row2][col-1]
		elif col1 == 0:
			return self.ps[row2][col2] - self.ps[row1-1][col2]

		return self.ps[row2][col2] - self.ps[row1-1][col2] - self.ps[row2][col1-1] + self.ps[row1-1][col1-1]




matrix = [[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],[1, 2, 0, 1, 5],[4, 1, 0, 1, 7],[1, 0, 3, 0, 5]]

# matrix = [[3, 0, 1, 4],[5, 6, 3, 2],[1, 2, 0, 1],[4, 1, 0, 1],[1, 0, 3, 0]]
# 
# matrix = [[3, 0, 1],[5, 6, 3],[1, 2, 0],[4, 1, 0]]


matrix = NumMatrix(matrix)
res = matrix.sumRegion(2, 1, 4, 3)
res = matrix.sumRegion(1, 1, 2, 2)
print("res : ", res)




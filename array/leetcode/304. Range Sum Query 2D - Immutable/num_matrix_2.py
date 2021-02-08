'''
	
	We can apply prefix sum in 2d Array approacing for this question.
	
	First : We can think a cache or pre-computing initialy. We can accumulative summaization. 
	
	Second: We can get according to the col and row params directly from 2D array.

	
	Our thoughts first should be big picture. How to computing an area in 2D array. 

		You can see images. 

		in Sum_od image , we can see cumulative region sum biggest area.

		We can extraxt sum(ob) from sum(abcd)

		finally we can get a formula : 

			sum(abcd) = sum(ob) - sum(oc) + sum(oa)

			oa is a common area for both calculation that's why we can sum.

	
	how to sum in itialy: 
	like : 
	matrix = [       n
				[3, 0, 1, 4, 2],
				[5, 6, 3, 2, 1],
			m	[1, 2, 0, 1, 5],
				[4, 1, 0, 1, 7],
				[1, 0, 3, 0, 5]
			 ]

	for first row : [3, 3, 4, 8, 10] cumulative sum.
	for first column : [ 
						[3],
						[8],
						[9],
						[13], 
						[14] 
					  ] 
						cumulative sum.

	and we need to sum cell by cell. we can start (1,1) sum 
		inside cumulative sum region formula : 

		ps(1,1) = ps(0,1) + ps(1,0) - ps(0,0) + matrix(1,1)

		ps = [       n
				[3, 3, 4, 8, 10],
				[8, 6, 3, 2, 1],
			m	[9, 2, 0, 1, 5],
				[13, 1, 0, 1, 7],
				[14, 0, 3, 0, 5]
			 ]


'''



from typing import List
class NumMatrix:

	def __init__(self, matrix: List[List[int]]):
		
		self.ps = []	
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return

		m = len(matrix) # for row len
		n = len(matrix[0]) # for col len


		#create a prefix sum 2d array
		ps = [[0 for _ in range(n)] for _ in range(m)]
		print("ps : ", ps)

		#0,0 set
		ps[0][0] = matrix[0][0]

		# first row filling
		for row in range(1,m):
			ps[row][0] = ps[row-1][0] + matrix[row][0]

		#first column filling
		for col in range(1,n):
			ps[0][col] = ps[0][col-1] + matrix[0][col]

		#filling inside 
		for row in range(1,m):
			for col in range(1,n):
				ps[row][col] = ps[row-1][col] + ps[row][col-1] - ps[row-1][col-1] + matrix[row][col]
		self.ps = ps

		print("PS : ", self.ps)

	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

		'''
			col1,   col2
		0
		
	row1

	row2

		'''

		#edge cases
		if len(self.ps) == 0 or len(self.ps[0]) == 0:
			return 0
		elif row1 == 0 and col1 == 0:
			return self.ps[row2][col2]
		elif row1 == 0:
			return self.ps[row2][col2] - self.ps[row2][col1-1]
		elif col1 == 0:
			return self.ps[row2][col2] - self.ps[row1-1][col2]

		return self.ps[row2][col2] - self.ps[row2][col1-1] - self.ps[row1-1][col2] + self.ps[row1-1][col1-1]

	

matrix = [[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],[1, 2, 0, 1, 5],[4, 1, 0, 1, 7],[1, 0, 3, 0, 5]]
# matrix = [[3, 0, 1, 4],[5, 6, 3, 2],[1, 2, 0, 1],[4, 1, 0, 1],[1, 0, 3, 0]]
# matrix = [[3, 0, 1],[5, 6, 3],[1, 2, 0],[4, 1, 0]]

matrix = [[-4,-5]]



matrix = NumMatrix(matrix)
# res = matrix.sumRegion(2, 1, 4, 3)
# res = matrix.sumRegion(0,0,1,0)
# res = matrix.sumRegion(1, 2, 2, 4)

res = matrix.sumRegion(0,0,0,0)
res = matrix.sumRegion(0,0,0,1)
res = matrix.sumRegion(0,1,0,1)

print("res : ", res)


'''
	T(N) = O(1)	time per query, 
	Pre computation : O(mn). But we care just get sum region O(1)

	S(N) = O(mn) to store cumulative region sum.
'''




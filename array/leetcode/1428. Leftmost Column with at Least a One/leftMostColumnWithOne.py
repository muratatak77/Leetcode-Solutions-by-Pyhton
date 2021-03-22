'''
	We can start to check from top right cell and move only left and right
	
	if we reach 1 from the cell we can decrement just col 
		curr_col -= 1
	
	if we reach 0 from the cell we can increment just row
		curr_row += 1

	we can iterate just left and down. 
	Finally we can check curr_col is in the final column.
	if we never left from the last column means we still stay start point , it must have been all 0's.
		we can return -1
	else
		we can return curr col + 1 (for index +1 )

'''

class Solution:
	def leftMostColumnWithOne(self, binaryMatrix):
		
		rows, cols = 3,4

		curr_col = cols -1
		curr_row = 0

		#go to left means current col grater and equal from 0
		#go to down means current row less than matrix row size
		while curr_col >= 0 and curr_row < rows:
			if binaryMatrix[curr_row][curr_col] == 0:
				curr_row += 1
			else:
				curr_col -= 1

		#if current col still is in the start point, means it must have been all 0's.
		if curr_col == cols -1:
			return -1
		else:
			return curr_col + 1



mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
mat = [[0,0],[0,1]]
res = Solution().leftMostColumnWithOne(mat)
print("res : ", res)

'''
	T(N) = O(N + M) 
		N is number of rows , M is number of cols. Each steo we are moving 1 step left or 1 step down.
		Therefor we will always finish looking at either one of the M rows or N columns.
		at most N + M steps.
	
	S(N) = O(1) 



'''

'''
Question: 
	Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

------------------------------------------------
Solution:


	we can start bottom-left position to iterative matrix.
	if target less than the target
		we can go up from the current cell, because a column already sorted top to bottom
			like row =- 1



	if target grater than the target
		we can go right from the current cell, because a row already sorted left to right
			like col += 1

	if we find target we can return true 
	else false

'''

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

    	#edge cases null check the matrix
    	if not matrix:
    		return False

    	height = len(matrix)
    	width = len(matrix[0])

    	#edge cases 
    	if height == 0 or width == 0:
    		return False

    	#start pointer will be bottom-left
    	col = 0
    	row = height - 1

    	while col < width and row >= 0:
    		if matrix[row][col] > target:
    			row -= 1
    		elif matrix[row][col] < target:
    			col += 1
    		else: #found it
    			return True

    	return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

res = Solution().searchMatrix(matrix, target)
print("res : ", res)

'''
	T(N) = O(n+m) row/col decrement/increment exatly once. 
			row can only be decrement m times, col can only be increment n times causing the 'while' loop to terminate, the loop can not run for more than n+m iterations.
			Because all other work us constant, the overall time complexity is lienar time.
	S(N) = O(1) no extra space.
	
'''

        
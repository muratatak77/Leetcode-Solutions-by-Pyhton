'''
	we can walk trough with row and col iteration.
		we can check every col and row : starting with word first char.
		if relative char starts same word first char and we can check right , bottom, left and top cell. 
			if we find second char from any neighbor we can walk to cells. 
			But if we can't find  same char  in the all directions we can backtrack 
	we can apply backtracking appoarch
	
	like : 

	A B C E
	S F C S
	A D E E
'''
class Solution:
	def exist(self, board, word):

		self.row_size = len(board)
		self.col_size = len(board[0])
		self.board = board

		for row in range(self.row_size):
			for col in range(self.col_size):
				if self.helper(row, col, word):
					return True
		return False

	def helper(self, row, col, suffix):

		#base case , leaf nodes
		#if we consume all words chars we find solution return True
		if len(suffix) == 0:
			return True

		#backtracink case , contracints 
		#check current status , before the jumping into recursive case
		if col < 0 or col == self.col_size or row < 0 or row == self.row_size or self.board[row][col] != suffix[0]:
			return False

		#recursive case
		# mark the choice before exploring further
		self.board[row][col] = '#'

		#explore 4 neighbors 
		for rowOffset, colOffset in [(0,1),(-1,0),(0,-1),(1,0)]:
			#backtracking with the consuming suffix 
			if self.helper(row+rowOffset, col+colOffset, suffix[1:]):
				return True

		self.board[row][col] = suffix[0]

		return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

res = Solution().exist(board, word)
print("res : ", res)


'''
 Time comp :   
 	N : number of cells in board
 	L : length of the word to be matched
 	every char has 4 choices but we won't go back where we come from thats why : 3 
 	T(N) = O(Nx3^L)
 S(N) : O(L)
'''




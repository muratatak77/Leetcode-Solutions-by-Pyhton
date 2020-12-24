'''
	We can apply BFS solution. DFS is not good for this solution because DFS will be scan every cell and will be exausting.

	We can walk trough with a Queue and to maximum a dice size. (1-6)
	if we have without -1 in a cell we can mark for next element. if we have -1 we can contunie not doing any mark in next element.
	
	we need a visited array to track visited cells.
	When we reach maxSquare we can return current visited cell.

'''
import collections


class Solution:
	def snakesAndLadders(self, board):

		size = len(board)
		maxSquare = size * size

		def bfs(n):

			q = collections.deque([n])
			visited = {1:0} # second : {15,1}, {}

			while q:
				curr = q.popleft()
				for i in range(1,7):

					nxt = curr + i # we need to iterate all dice side (i + 1, i + 2 ... i + 6)
					if nxt > maxSquare:
						continue

					(r,c) = getRowCol(nxt)

					if board[r][c] != -1:
						nxt = board[r][c]

					if nxt not in visited:
						q.append(nxt)
						visited[nxt] = visited[curr] + 1
						if nxt == maxSquare:
							return visited[nxt]
			return -1

		def getRowCol(n):
			row = (maxSquare-n)//size
			c = (n-1)%(2*size)
			if c < size:
				col = c
			else:
				col = 2*size-1-c
			return (row,col)
		

		return bfs(1)

			
board = [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]


board = [
[-1,-1,-1],
[-1,-1,-1],
[-1,5,-1]
]

board = [[1,1,-1],[1,1,1],[-1,1,1]]

ans = Solution().snakesAndLadders(board)
print("Answer : " , ans)

'''
T(N) = O(N^2) , where N is the length of the board.
S(N) = O(N^2)
'''
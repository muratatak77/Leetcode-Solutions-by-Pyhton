import collections

class Solution:
	def snakesAndLadders(self, board):

		size = len(board)
		maxSquare = size * size
		print("Size : ", size)
		print("maxSquare : ", maxSquare)


		def numToRowCol(n):
			print("  start numToRowCol >>>>>>>>>> n : ", n)
			row = (maxSquare-n)//size
			print("    row = (maxSquare-n)//size. row =(", maxSquare, "-" ,n, ")//", size," = ", row)
			print("    row : ", row)

			c = (n-1) % (2*size)
			print("    c = (n-1) % (2*size) : c = ", (n-1),"% (", 2*size , ") = ", c)
			if c < size:
				col = c
			else:
				col = 2*size-1-c
			print("    col :" , col, " , row : ", row)
			print("  <<<<<<<<, end numToRowCol")

			return (row,col)


		def minMoves(n):
			q = collections.deque([n])
			print("Initial q : ", q)
			visited = {n:0} #records shortest path distance from source to this vertex
			print("Initial visited : ", visited)
			while q:
				curr = q.popleft()
				print("Popleft curr :", curr)
				for i in range(1,7):
					print(">>>>>>>>>>>>  for start")
					nxt = curr + i
					print("Nxt : ", nxt)
					if nxt > maxSquare:
						continue

					(r,c) = numToRowCol(nxt)
					print("numToRowCol r,c : ", (r,c))

					if board[r][c] != -1:
						print("board[r][c] dif then -1:", board[r][c])
						nxt = board[r][c]
						print("forwards or backwords : ", nxt)

					if nxt not in visited:
						q.append(nxt)
						visited[nxt] = visited[curr] + 1
						print("Finally q : ", q)
						print("Finally visited : ", visited)
						print("nxt : ", nxt)
						if nxt == maxSquare:
							return visited[nxt]
				print(">>>>>>>>>>>>  for end")

			return -1


		return minMoves(1)

			
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
[-1,8,-1]
]

board = [[1,1,-1],[1,1,1],[-1,1,1]]

ans = Solution().snakesAndLadders(board)
print("Answer : " , ans)
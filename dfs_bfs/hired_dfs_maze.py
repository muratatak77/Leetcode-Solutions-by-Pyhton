'''
	We can apply DFS approching for this question.

	maze = [
	[0,0,1,0,0],
	[0,0,0,0,0],
	[0,0,0,1,0],
	[1,1,0,1,1],
	[0,0,0,0,0]
	],

	start = [0,4], 

	destination = [4,4]

	if we reach to the destination we can return Trun inside the DFS.

	we can iterate and we can check our way is right way
			we need go left bottom right and up.
			means we can go from (x,y) to left :(0,-1) , right: (0,1), bottom: (1,0), up: (-1,0)


		but if we have 1 we can skip for this case. Because 1 means there is wall.
		
		and we can check seen before this cell. we can use a set for checking cell whether visited or not before.
		
		and if DFS return True we can return True

	after the for iterate we can return False

	look relavant images.


'''

class Solution:
	def hasPath(self, maze,n):

		#edge cases
		if not maze:
			return False
		if len(maze) == 0:
			return False

		#m = x
		#n = y
		m,n,seen = len(maze), len(maze[0]), set()

		def dfs(i,j):
			print("START > i,j :", i, " - ", j)

			if [i,j] == [m-1,n-1]: return True

			for dx, dy in ((0,-1),(0,1),(-1,0),(1,0)):
				print("	  dx , dy:", "(",dx,",",dy,")")
				x,y = i,j

				#if cell out the maze we can skip this case 
				#or if we have wall (1) we can skip.
				#we can go until if unsuitable case. means this cell can go until the end of appropiate cell
				print("		x+dx = ", x+dx, " / y+dy = ", y+dy)
				while 0 <= x+dx < m  and 0 <= y+dy < n and  not maze[x+dx][y+dy]: 
					x,y = x+dx,y+dy # we  need to move to a new pozisions

				print("					x,y:",x,",",y)
					#if seen or visited this cell before we can't call recursive call 
				if (x,y) not in seen:
					seen.add((x,y))
					print("						Seen : ", seen)
					if dfs(x,y): return True
				print("=================================")
			return False

		return dfs(0,0)


maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
n = 3

# maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
# start = [0,4]
# destination = [3,2]

res = Solution().hasPath(maze, n)
print("res : ", res)

 
''''


T(N) = O(MN) n = col and m = row size
S(N) = 0(MN) visited set of size m * n
Output : 



m :  5
n :  5
START > i,j : 0  -  4
	  dx , dy: ( 0 , -1 )
		x+dx =  0  / y+dy =  3
					x,y: 0 , 3
						Seen :  {(0, 3)}
START > i,j : 0  -  3
	  dx , dy: ( 0 , -1 )
		x+dx =  0  / y+dy =  2
					x,y: 0 , 3
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  0  / y+dy =  4
					x,y: 0 , 4
						Seen :  {(0, 3), (0, 4)}
START > i,j : 0  -  4
	  dx , dy: ( 0 , -1 )
		x+dx =  0  / y+dy =  3
					x,y: 0 , 3
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  0  / y+dy =  5
					x,y: 0 , 4
=================================
	  dx , dy: ( -1 , 0 )
		x+dx =  -1  / y+dy =  4
					x,y: 0 , 4
=================================
	  dx , dy: ( 1 , 0 )
		x+dx =  1  / y+dy =  4
					x,y: 2 , 4
						Seen :  {(2, 4), (0, 3), (0, 4)}
START > i,j : 2  -  4
	  dx , dy: ( 0 , -1 )
		x+dx =  2  / y+dy =  3
					x,y: 2 , 4
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  2  / y+dy =  5
					x,y: 2 , 4
=================================
	  dx , dy: ( -1 , 0 )
		x+dx =  1  / y+dy =  4
					x,y: 0 , 4
=================================
	  dx , dy: ( 1 , 0 )
		x+dx =  3  / y+dy =  4
					x,y: 2 , 4
=================================
=================================
=================================
	  dx , dy: ( -1 , 0 )
		x+dx =  -1  / y+dy =  3
					x,y: 0 , 3
=================================
	  dx , dy: ( 1 , 0 )
		x+dx =  1  / y+dy =  3
					x,y: 1 , 3
						Seen :  {(1, 3), (2, 4), (0, 3), (0, 4)}
START > i,j : 1  -  3
	  dx , dy: ( 0 , -1 )
		x+dx =  1  / y+dy =  2
					x,y: 1 , 0
						Seen :  {(2, 4), (0, 4), (0, 3), (1, 0), (1, 3)}
START > i,j : 1  -  0
	  dx , dy: ( 0 , -1 )
		x+dx =  1  / y+dy =  -1
					x,y: 1 , 0
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  1  / y+dy =  1
					x,y: 1 , 4
						Seen :  {(2, 4), (0, 4), (0, 3), (1, 4), (1, 0), (1, 3)}
START > i,j : 1  -  4
	  dx , dy: ( 0 , -1 )
		x+dx =  1  / y+dy =  3
					x,y: 1 , 0
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  1  / y+dy =  5
					x,y: 1 , 4
=================================
	  dx , dy: ( -1 , 0 )
		x+dx =  0  / y+dy =  4
					x,y: 0 , 4
=================================
	  dx , dy: ( 1 , 0 )
		x+dx =  2  / y+dy =  4
					x,y: 2 , 4
=================================
=================================
	  dx , dy: ( -1 , 0 )
		x+dx =  0  / y+dy =  0
					x,y: 0 , 0
						Seen :  {(2, 4), (0, 4), (0, 0), (0, 3), (1, 4), (1, 0), (1, 3)}
START > i,j : 0  -  0
	  dx , dy: ( 0 , -1 )
		x+dx =  0  / y+dy =  -1
					x,y: 0 , 0
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  0  / y+dy =  1
					x,y: 0 , 1
						Seen :  {(0, 1), (2, 4), (0, 4), (0, 0), (0, 3), (1, 4), (1, 0), (1, 3)}
START > i,j : 0  -  1
	  dx , dy: ( 0 , -1 )
		x+dx =  0  / y+dy =  0
					x,y: 0 , 0
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  0  / y+dy =  2
					x,y: 0 , 1
=================================
	  dx , dy: ( -1 , 0 )
		x+dx =  -1  / y+dy =  1
					x,y: 0 , 1
=================================
	  dx , dy: ( 1 , 0 )
		x+dx =  1  / y+dy =  1
					x,y: 2 , 1
						Seen :  {(0, 1), (2, 4), (0, 4), (2, 1), (0, 0), (0, 3), (1, 4), (1, 0), (1, 3)}
START > i,j : 2  -  1
	  dx , dy: ( 0 , -1 )
		x+dx =  2  / y+dy =  0
					x,y: 2 , 0
						Seen :  {(0, 1), (2, 4), (0, 4), (2, 1), (0, 0), (0, 3), (2, 0), (1, 4), (1, 0), (1, 3)}
START > i,j : 2  -  0
	  dx , dy: ( 0 , -1 )
		x+dx =  2  / y+dy =  -1
					x,y: 2 , 0
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  2  / y+dy =  1
					x,y: 2 , 2
						Seen :  {(0, 1), (2, 4), (0, 4), (2, 1), (0, 0), (0, 3), (2, 0), (1, 4), (2, 2), (1, 0), (1, 3)}
START > i,j : 2  -  2
	  dx , dy: ( 0 , -1 )
		x+dx =  2  / y+dy =  1
					x,y: 2 , 0
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  2  / y+dy =  3
					x,y: 2 , 2
=================================
	  dx , dy: ( -1 , 0 )
		x+dx =  1  / y+dy =  2
					x,y: 1 , 2
						Seen :  {(0, 1), (2, 4), (1, 2), (0, 4), (2, 1), (0, 0), (0, 3), (2, 0), (1, 4), (2, 2), (1, 0), (1, 3)}
START > i,j : 1  -  2
	  dx , dy: ( 0 , -1 )
		x+dx =  1  / y+dy =  1
					x,y: 1 , 0
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  1  / y+dy =  3
					x,y: 1 , 4
=================================
	  dx , dy: ( -1 , 0 )
		x+dx =  0  / y+dy =  2
					x,y: 1 , 2
=================================
	  dx , dy: ( 1 , 0 )
		x+dx =  2  / y+dy =  2
					x,y: 4 , 2
						Seen :  {(0, 1), (2, 4), (1, 2), (0, 4), (2, 1), (0, 0), (0, 3), (2, 0), (1, 4), (4, 2), (2, 2), (1, 0), (1, 3)}
START > i,j : 4  -  2
	  dx , dy: ( 0 , -1 )
		x+dx =  4  / y+dy =  1
					x,y: 4 , 0
						Seen :  {(0, 1), (2, 4), (1, 2), (0, 4), (2, 1), (4, 0), (0, 0), (0, 3), (2, 0), (1, 4), (4, 2), (2, 2), (1, 0), (1, 3)}
START > i,j : 4  -  0
	  dx , dy: ( 0 , -1 )
		x+dx =  4  / y+dy =  -1
					x,y: 4 , 0
=================================
	  dx , dy: ( 0 , 1 )
		x+dx =  4  / y+dy =  1
					x,y: 4 , 4
						Seen :  {(0, 1), (4, 4), (2, 4), (1, 2), (0, 4), (2, 1), (4, 0), (0, 0), (0, 3), (2, 0), (1, 4), (4, 2), (2, 2), (1, 0), (1, 3)}
START > i,j : 4  -  4
res :  True
[Finished in 0.1s]
'''
		

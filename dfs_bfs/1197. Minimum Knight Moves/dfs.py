'''


'''

class Solution:
	def minKnightMoves(self, x: int, y: int) -> int:

		x = abs(x)
		y = abs(y)

		print("x : ", x, " - y : ", y)

		seen = set((0,0))
		directions = [(2,1),(-2,1),(-2,-1),(2,-1),(1,2),(-1,-2),(-1,2),(1,-2)]
		steps = 0

		def dfs(cur_x, cur_y):
			nonlocal steps
			
			if cur_x == x and cur_y == y:
				return steps

			for d in directions:
				print(" 	in process d : ", d)
				new_x = cur_x + d[0]
				new_y = cur_y + d[1]
				print("		new_x : ", new_x, " - new_y :", new_y)

				if (new_x,new_y) not in seen and -2<= new_x <= x+2 and -2<= new_y <= y+2:
					seen.add((new_x, new_y))
					dfs(new_x, new_y)


		dfs(0,0)

		return steps


x = 2
y = 1
res = Solution().minKnightMoves(x, y)
print("res : ", res)
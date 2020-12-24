class DSU:
	def __init__(self, N):
		self.p = list(range(N))
		print("self.p :", self.p)


	def find(self, x):
		print("					find start. x :", x, " - p[x] :", self.p[x])
		if self.p[x] != x:
			self.p[x] = self.find(self.p[x])
			print("						self.p[x] != x - Paraent has chaned : ", self.p)
		return self.p[x]

	def union(self, x, y):
		print("	 			start union : x:", x, "- y: ", y)
		xr = self.find(x)
		yr = self.find(y)
		print("						xr : ",xr , " - yr :", yr)
		self.p[xr] = yr
		print("					end union : parent : ", self.p)

class Solution(object):
	def regionsBySlashes(self, grid):
		N = len(grid)
		print("N : ", N)
		dsu = DSU(4 * N * N)
		for r, row in enumerate(grid):
			print("r : ", r , " - row :", row)

			for c, val in enumerate(row):
				print("  c :", c , " - val :", val)

				root = 4 * (r*N + c)
				print("  	root :", root)
				if val in '/ ':
					print("    		we have / ")
					dsu.union(root + 0, root + 1)
					dsu.union(root + 2, root + 3)

				if val in '\\ ':
					print("    		we have \\ ")
					dsu.union(root + 0, root + 2)
					dsu.union(root + 1, root + 3)

				print("	   root : ", root)

				# north/south
				if r+1 < N: 
					print("			r+1 < N. r : ", r)
					dsu.union(root + 3, (root+4*N) + 0)
				if r-1 >= 0: 
					print("			r-1  >= 0. r : ", r)

					dsu.union(root + 0, (root-4*N) + 3)

				# east/west
				if c+1 < N:
					print("			c+1  < N. c : ", c)
					dsu.union(root + 2, (root+4) + 1)
				if c-1 >= 0:
					print("			c-1 >= 0. c : ", c)
					dsu.union(root + 1, (root-4) + 2)

				print("------------------------")

		return sum(dsu.find(x) == x for x in range(4*N*N))


grid = [
  " /",
  "/ "
]


grid = [
  " /",
  "  "
]

grid = [
  "\\/",
  "/\\"
]

res = Solution().regionsBySlashes(grid)
print("res :", res)
class Solution(object):
	def gardenNoAdj(self, n, paths):
		"""
		:type n: int
		:type paths: List[List[int]]
		:rtype: List[int]
		"""
		result = [0 for i in range(0, n)]
		print("result : ", result)

		adj_list = [[] for i in range(n)]

		for x, y in paths:
			adj_list[x-1].append(y-1)
			adj_list[y-1].append(x-1)

		print("adj_list :", adj_list)
			
		for cur in range(n):

			choice = [1,2,3,4]
			print("cur : ", cur)

			if adj_list[cur]:

				neis = adj_list[cur]
				print("  neis : ", neis)

				for nei in neis:
					nei_clr = result[nei]
					print("	    nei_clr : ", nei_clr)

					if nei_clr in choice:
						print("		   nei_clr in choice we can remove nei_clr", nei_clr)
						choice.remove(nei_clr)

			cur_flr = choice.pop(0)
			print("    cur_flr : ", cur_flr)

			result[cur] = cur_flr
			print("result : ", result)

			print("---------------------")
		return result

n = 3
paths = [[1,2],[2,3],[3,1]]


# n = 4
# paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]


res = Solution().gardenNoAdj(n, paths)
print("res :", res)

'''
	first of all, we can think this question is a graph question. 
	Because we have same pairs = path .  
	And we need to fill a result array.
	We can say every garden a vertex - node , every path is a edge. hence, we need to generate a adjency list using the vertex and path. 
	- adjlist array = length should be N
	- result array = len should be N

	we can iterate in len(N)

		we need a set we can say neighbor_flower_type, we will use this set check neighhbors whether has or not.
			
		we can do second iterate for 4 type color  by index : (1,5) : flower_type

			we need to check together our flower type set and our adj list neighbors. 
			if we have added before in set we can contunie else we need to add result array.

		if we reach different flower type we can add result to get from adj list. 

'''
class Solution(object):
	def gardenNoAdj(self, n, paths):
		"""
		:type n: int
		:type paths: List[List[int]]
		:rtype: List[int]
		"""

		result = [0 for _ in range(n)]
		print("result : ", result)

		adj_list = [[] for _ in range(n)]

		#fill the adj list
		#if we pur directly [[1,2],[2,3],[3,1]], we gonna get out of index. becuase we dont have 3 index in adj list
		
		for x,y in paths:
			print("x :", x , " - y :", y)
			adj_list[x-1].append(y-1)
			adj_list[y-1].append(x-1)
		#will be [[1, 2], [0, 2], [1, 0]]


		print("adj_list : ", adj_list)
		#iterate for every garden
		for garden in range(n):

			#new set each garden
			nei_flower_type = set()

			# we need neighors in the current garden
			# [1,2]
			for nei in adj_list[garden]:
				print("			nei : ", nei)
				#we can add directly from result current nei to set, result = [0,0,0], [1,0,0]
				nei_flower_type.add(result[nei]) # {0}, {1,0}

			print("nei_flower_type : ", nei_flower_type)

			for flower_type in range(1,5):
				if flower_type in nei_flower_type: # 1, 2
					continue
				else:
					result[garden] = flower_type # result[0] = 1, 
					break

			print("result : ", result)
			print("----------------")
		return result




n = 3
paths = [[1,2],[2,3],[3,1]]


# n = 4
# paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]


res = Solution().gardenNoAdj(n, paths)
print("res :", res)


'''
	 V: number of vertex 
	 E: number of edges
	 O(V+E)

'''

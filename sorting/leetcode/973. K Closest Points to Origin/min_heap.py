import heapq
from typing import List

class Solution:
	def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
		
		heap = []
		dist_items = lambda i: points[i][0]**2 + points[i][1]**2
		
		for i in range(len(points)):
			print(dist_items(i))
		print("-------------")
		
		for (x, y) in points:
			dist = -(x*x + y*y)
			print("dist : ", dist)
			print("heap size : ", len(heap))
			if len(heap) == K:
				print("it will added dist: ", dist , " x,y : ", x,y)
				heapq.heappushpop(heap, (dist, x, y))
				print("First heap :", heap)
				print("-------------")
			else:
				heapq.heappush(heap, (dist, x, y))
				print("second heap :", heap)
				print("-------------")

		
		return [(x,y) for (dist,x, y) in heap]





points = [[1,3],[-2,2],[1,4],[-1,2],[2,3]]
K = 2

# points = [[1,3],[-2,2]]
# K = 1

# points = [[3,3],[5,-1],[-2,4]]
# K = 2

res = Solution().kClosest(points, K)
print("res : " , res)
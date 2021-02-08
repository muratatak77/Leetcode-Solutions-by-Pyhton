import random
class Solution(object):
	def kClosest(self, points, K):
		return self.selection(points, K)

	def selection(self, points, K):
			left = 0
			right = len(points)-1

			while True:
				if left == right: break
				pvt_idx = self.partition(left, right)
				if pvt_idx < K:
					left = pvt_idx + 1
				else:
					right = pvt_idx

			return points[:K]

	def partition(self, left, right):

		pvt_idx = random.randint(left, right)
		pivot = self.distance(points[pvt_idx])

		points[pvt_idx], points[right] = points[right], points[pvt_idx]

		store_idx = 0
		for i in range(left, right):
			if self.distance(points[i]) < pivot:
				points[i], points[store_idx] = points[store_idx], points[i]
				store_idx += 1


		points[store_idx], points[right] = points[right], points[store_idx]
		return store_idx


	def distance(self, points):
		return points[0]**2+points[1]**2



points = [[1,3],[-2,2],[1,4],[-1,2],[2,3]]
K = 2
res = Solution().kClosest(points, K)
print("res : " , res)
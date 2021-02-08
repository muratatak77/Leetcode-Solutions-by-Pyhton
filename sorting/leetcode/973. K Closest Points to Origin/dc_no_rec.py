import random
class Solution(object):
	
	def KClosest(self, points, K):
		# dist = self.get_dist(points)

		def select(points, K):

			left = 0
			right = len(points)-1

			while True:
				if left == right: break
				pvt_idx = partition(points, left, right)

				#is partition index less than K , meaning we need to find new partition index to left iterator next element pivot index
				#if pivot index equal K or grater than we need just a set right params so we will left right part for next partition 
				if pvt_idx < K:
					left = pvt_idx + 1
				else:
					right = pvt_idx


			return points[:K]


		def partition(points, left, right):

			# select a random pvt_idx between 
			pvt_idx = random.randint(left, right)
			# pvt_idx = (left + right) // 2

			pivot = dist(points[pvt_idx])

			# 1. move pivot to right
			points[pvt_idx], points[right] = points[right], points[pvt_idx]

			# 2. move all smaller elements to the left
			store_index = left
			for i in range(left, right):
				if dist(points[i]) < pivot:
					points[store_index], points[i] = points[i], points[store_index]
					store_index += 1

			# 3. move pivot to its final place
			points[right], points[store_index] = points[store_index], points[right]  
			return store_index


		def dist(p1):
			total = p1[0]**2 + p1[1]**2
			return total

		return select(points, K)



points = [[1,3],[-2,2],[1,4],[-1,2],[2,3]]
K = 2

# points = [[1,3],[-2,2]]
# K = 1

# points = [[3,3],[5,-1],[-2,4]]
# K = 2

res = Solution().KClosest(points, K)
print("res : " , res)

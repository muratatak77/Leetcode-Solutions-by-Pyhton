import random
class Solution(object):
	def kClosest(self, points, K):
		dist = lambda i: points[i][0]**2 + points[i][1]**2
		for i in range(len(points)):
			print("dist " , str(i), " : " , dist(i) )
		print("--------------------")

		def sort_points(i, j, K):
			# Partially sort_pointss A[i:j+1] so the first K elements are
			# the smallest K elements.
			print("first i : " , str(i), " - j :" , str(j) )
			if i >= j: return

			# Put random element as A[i] - this is the pivot
			rnd = random.randint(i, j)
			print("Random rnd : " , rnd)
			points[i], points[rnd] = points[rnd], points[i]
			print("after first i : " , str(i), " - j :" , str(j) )
			print("points", points)

			mid = partition(i, j)
			print("mid : ", mid)

			print("======== i : " , str(i), " - j :" , str(j) )
			left_length =  mid - i + 1
			print(" >>>>>>>> left_length : " , left_length)
			print(" ...... K : " , K)



			if K < left_length:
				print(" K < left_length : " , K , " < ", left_length)
				sort_points(i, mid - 1, K)
			elif K > left_length:
				print(" K > left_length : " , K , " > ", left_length)
				sort_points(mid + 1, j, K - left_length)
			elif K == left_length:
				print(" K = left_length. Done return points: " , K , " = ", left_length)
				return points


		def partition(i, j):
			# Partition by pivot A[i], returning an index mid
			# such that A[i] <= A[mid] <= A[j] for i < mid < j.
			oi = i
			pivot = dist(i)
			print("pivot  :" , pivot)
			i += 1
			print(">> i : " , str(i), " - j :" , str(j) )

			while True:
				
				while i < j and dist(i) < pivot:
					i += 1
					print("i increment : ", str(i))
					print("------")
				
				while i <= j and dist(j) >= pivot:
					j -= 1
					print("j decrement : ", str(j))
					print("------")

				if i >= j: break

				points[i], points[j] = points[j], points[i]
				print(">>>> points  :" , points)

			points[oi], points[j] = points[j], points[oi]
			print(">>>> son points  :" , points)
			print("----------------------------------------------")

			return j

		sort_points(0, len(points) - 1, K)
		print("--------------------")
		return points[:K]



points = [[1,3],[-2,2],[1,4],[-1,2],[2,3]]
K = 2
res = Solution().kClosest(points, K)
print("res : " , res)
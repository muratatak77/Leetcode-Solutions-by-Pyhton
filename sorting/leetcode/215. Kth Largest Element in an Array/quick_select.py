import random
# from random import randint

class Solution():

	def findKthLargest(self, nums, k):

		def select(left, right, kth):

			if left == right:
				return nums[left]

			# pivot_idx = (left+right)//2
			pivot_idx = random.randint(left, right)
			pivot_idx = partition(left, right, pivot_idx)


			if pivot_idx == kth:
				return nums[kth]

			elif pivot_idx < kth:
				return select(left, pivot_idx-1, kth)

			else:
				return select(pivot_idx+1, right, kth)


		def partition(left, right, pivot_idx):

			# 1. select pivot element and move to first
			pivot = nums[pivot_idx]
			print("pivot : " + str(pivot))

			nums[pivot_idx],nums[right] = nums[right],nums[pivot_idx]
			print("nums : " + str(nums))

			# 2. move all smaller element to the left
			store_idx = left
			for i in range(left,right):
				print("nums[i] : " + str(nums[i]) + " - pivot : " + str(pivot))
				if nums[i]<pivot:
					nums[store_idx], nums[i] = nums[i], nums[store_idx]
					print("nums[i] : " + str(nums[i]))
					store_idx = store_idx + 1

			# 3 . move pilot to the final place , partition position 
			nums[right], nums[store_idx] = nums[store_idx], nums[right]

			# print("store_idx : " + str(store_idx))
			print("nums after swap : " + str(nums))
			print("store_idx : " + str(store_idx))
			return store_idx

		return select(0, len(nums) - 1, len(nums) - k)	


arr = [3,2,1,5,6,4]
k = 2
res = Solution().findKthLargest(arr, k)
print(res)

			

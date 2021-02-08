# Complete the function below.
import random
from random import randint

class Solution:
	def findKthLargest(self, nums, k):



		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		def partition(nums, left, right, pivot_index):
			pivot = nums[pivot_index]
			# 1. move pivot to end
			nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
			
			# 2. move all smaller elements to the left
			store_index = left
			for i in range(left, right):
				if nums[i] < pivot:
					nums[store_index], nums[i] = nums[i], nums[store_index]
					store_index += 1

			# 3. move pivot to its final place
			nums[right], nums[store_index] = nums[store_index], nums[right]  
			
			return store_index
		
		def select(nums, left, right, k_th):
			"""
			Returns the k-th smallest element of list within left..right
			"""

			if left == right:       # If the list contains only one element,
				return list(set(nums[k_th:]))
			
			# select a random pivot_index between 
			pivot_index = random.randint(left, right)     
							
			# find the pivot position in a sorted list   
			pivot_index = partition(nums, left, right, pivot_index)
			
			# the pivot is in its final sorted position
			if k_th == pivot_index:
				return list(set(nums[k_th:])) #return start k_th 

			# go left
			elif k_th < pivot_index:
				return select(nums, left, pivot_index - 1, k_th)
			# go right
			else:
				return select(nums, pivot_index + 1, right, k_th)

		# kth largest is (n - k)th smallest 
		
		def unique(list1): 
			unique_list = [] 
			for x in list1: 
				if x not in unique_list: 
					unique_list.append(x) 
			return unique_list

		return select(unique(nums), 0, len(unique(nums)) - 1, len(unique(nums)) - k)


nums = [1, 5, 4, 4, 2]
k = 2

nums = [4,2,1,11,11,6,2,10,4,3,10,6,5,6,7,2,10,10,4,6,5,8]

k = 7

res = Solution().findKthLargest(nums,k)
print(res)
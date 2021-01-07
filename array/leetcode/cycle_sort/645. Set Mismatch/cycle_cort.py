'''
	We can apply cycle sort approach in this question

	first we try to find index and item is useful sorting logic. 
	should be : 
		index : 0 , item : 1
		index : 1, 	item : 2

		if we find any wrong match between index and item we can swap useful place in this array.
		like : 
		index : 2, item : 2

		item should be 3. but we have 2.
		we need swap with the right place in this array.

	
	and second part we can iterate and check : nums[i] == i+1

	nums[i] = multiple item
	i+1 = missing item


'''
from typing import List

class Solution:
	def findErrorNums(self, nums: List[int]) -> List[int]:

		n = len(nums)

		#first part 
		#cycle sorting
		for i in range(0,n):
			# 1,2,2,4
			while nums[i] != i+1:
				d = nums[i]-1

				#sanity check	
				#is d is a valid check
				#duplicate check
				#we ll make duplicate check in this case
				if nums[d] != nums[i]:
					nums[i], nums[d] = nums[d], nums[i]
				else:
					break

		print("nums : ", nums)

		#second part
		#current item is equal the right sorting variable
		for i in range(0,n):
			if nums[i] != i+1:
				return [ nums[i], i+1]

nums = [1,2,2,4]
nums = [1,2,3,4,5,5]
nums = [3,2,2]
res = Solution().findErrorNums(nums)
print("res : " , res)


'''
	T(N) = O(N) we jave just fully 2 loop. We don't have any inside loops
	S(N) = O(1) we don't have any extra space

'''
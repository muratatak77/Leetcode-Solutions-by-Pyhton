'''
	we can apply cycle sort approach in this question.
	we have 2 parts:
	first parts : 
		try to get ideal nums list. Means get a almost sorting list.
		we can walk trough in a loop 
			if we have a difference expect list items.
				we need a expect value we can say destination and we can call 'd'
				if this destination beetween 0 and n  and expect value is not same
				we can swap to put a right place current item.

	second part:
	classic loops and check current item is not equal expect item (i+1)
		if we have a different items we can return i + 1

	no we can return n+1

'''

from typing import List

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		
		i = 0
		n = len(nums)

		if 1 not in nums:
			return 1

		if n == 1:
			return 2
		
		while i < n:
			#expect value for ideal list
			#if we have [1,2,0] we need a ideal list : [1,2,0]
			#so destination value nums[i]-1
			d = nums[i]-1
			print("d : ", d, " - i :", i)
			
			# sanity check 
			# should be positive and not duplicate
			if 0 <= d < n and nums[d] != nums[i]:
				print("we'll swap. nums[i] :", nums[i], " - nums[d]: ", nums[d])
				nums[i], nums[d] = nums[d], nums[i]
				print("after swap ; ", nums)
			else:
				i += 1
				print(">>>>>>>>>>>>>>>>>  i + 1 : " , i)

		print("result nums : ", nums)
				
		for i in range(n):
			print(" ----- i : ", i)
			if nums[i] != i+1:
				# if we have [1,2,0] case we need return 3 = i+1
				return i+1
		
		#in [1,2,3] case our answer will be 4. n = 3 + 1 = 4
		return n+1



nums = [7,8,9,11,12]
nums = [3,4,-1,1]
nums = [3,4,5,6]
# nums = [1,2,3]
# nums = [1,2,0]
res = Solution().firstMissingPositive(nums)
print("res : ", res)

'''
	T(N) = O(N) Just 1 while and 1 for loop
	S(N) = O(1) No extra space using
'''
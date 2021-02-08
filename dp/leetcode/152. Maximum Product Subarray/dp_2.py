'''
	Brute force
		we can apply brute force approach. we can do iterate each number for every nums. 
		and we can max with the yb max methods. 
		Time comp will be O(N^2)


	DP :
	in one iterate :
	first we can think 2 pass. one pass keeps keep to accumulate pozitive numbers. max method.
	second pass negative numbers so min method

	we have to keep min. like we can reach negative numbers first and when we reach second negatieve numbers, if we get multiply and can take a pozitif number. 

	like :
		nums = [2,-5,3,-4,1] 
		we have 2 negative numbers. if we can not keep min second pass we can loss to get max number.

		max_so_far = max(curr, max_so_far * curr, min_so_far * curr)
		min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
		
		curr	   : 2, -5,  3,  -4
		max_so_far : 2, -5,  3, 120 (-30 * -4)
		min_so_far : 2,-10,-30, -12
    
    result = 120

'''

from typing import List

class Solution:
	def maxProduct(self, nums: List[int]) -> int:

		if not nums:
			return 0

		if len(nums) == 0:
			return 0
		
		max_so_far = nums[0]
		min_so_far = nums[0]
		result = max_so_far

		for i in range(1,len(nums)):
			curr = nums[i]
			temp_so_far = max(curr, max_so_far*curr, min_so_far*curr)
			min_so_far = min(curr, max_so_far*curr, min_so_far*curr)
			max_so_far = temp_so_far
			result = max(result, max_so_far)
		return result


nums = [2,1,0,-7,3,-4,1]
nums = [2,-5,3,1,-4,0, -10, 2,8]
nums =  [2,-5,3,-4,1] 

res = Solution().maxProduct(nums)
print("res :", res)

'''
	T(N) = O(N)  nums iterate
	S(N) = O(1)   no addtional space
'''
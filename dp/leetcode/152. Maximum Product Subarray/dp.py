from typing import List

class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		if len(nums) == 0:
			return 0

		max_so_far = nums[0]
		min_so_far = nums[0]
		result = max_so_far

		for i in range(1, len(nums)):
			curr = nums[i]

			temp_max = max(curr, max_so_far * curr, min_so_far * curr)
			print("	max_so_far : ", temp_max)
			min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
			print("	min_so_far : ", min_so_far)
			
			# temp_max = max(curr, max_so_far*curr)

			print("temp_max : ", temp_max)

			max_so_far = temp_max

			result = max(max_so_far, result)

			print("		result ; ", result)

		return result


nums = [2,1,0,-7,3,-4,1]
nums = [2,-5,3,1,-4,0, -10, 2,8]
nums =  [2,-5,3,-4,1] 

res = Solution().maxProduct(nums)
print("res :", res)
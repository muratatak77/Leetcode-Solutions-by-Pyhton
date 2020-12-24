'''
	We think how to get a series sum?
		If we a formula to get a series sum, we can match normal sum of this series.
		Difference  of this process we can get missing number

		sum any series formula = n*(n+1)/2 
		normal sum series = sum(nums)
		get missing elem > sum_series - normal_sum 

'''

from typing import List

class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		if not nums:
			return 0

		n = len(nums)
		
		if n == 0:
			return 0

		sum_series = n*(n+1)//2
		actual_sum = sum(nums)
		return sum_series - actual_sum


nums = [0,1,2,4]
nums = [0]
res = Solution().missingNumber(nums)
print("res : ", res)

'''
	T(N) = O(N)
		series sum formula works O(1), but summing cost us O(N), so this alg is overall linear.
		Because we don't know about which number is missing. 
	S(N) = O(1) there is no any extra space process

'''
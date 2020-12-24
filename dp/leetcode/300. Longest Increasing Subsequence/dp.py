'''
	we can apply a DP solution for this question.
	we can generate a DP table been length array size
	first element will be 1 in DP

	after we can iterate 2 loops. i start from 1 , j start from 0
		every item will check to start from j , to i
		if nums[i] > nums[j]
			we can find max_val = max(max_val, dp[j])

		finally we can set dp[i] = max_val +1 
		and we can keep a general ans_max variable. 
			max_ans = max(max_ans, dp[i])

'''
from typing import List
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		if not nums:
			return 0
		if len(nums) == 0:
			return 0

		dp = [None] * (len(nums)+1)
		dp[0] = 1
		print("dp : ", dp)

		ans_max = 1
		for i in range(1,len(nums)):
			max_val = 0
			for j in range(0,i):
				print("	nums[i] :", nums[i], " - nums[j] : ", nums[j])
				if nums[i] > nums[j]:
					max_val = max(max_val, dp[j])
					print("		max_val : ", max_val)
					print("		-----------------------")

			dp[i] = max_val + 1
			print("  dp[i] :", dp[i])
			ans_max = max(ans_max, dp[i])

			print("  ans_max : ", ans_max)
			print("--------------------")

		return ans_max


nums = [10,9,2,5,3,7,101,18]

res = Solution().lengthOfLIS(nums)

print("res : ", res)


'''
T(N) = O(N^2) 2 loops 
S(N) = O(N) just DP table array size of n
'''
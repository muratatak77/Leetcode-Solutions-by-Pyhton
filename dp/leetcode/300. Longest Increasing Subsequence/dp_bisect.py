'''
	we can apply AP and Bisect left. 
	first  we can generate a dp = list()
	iterate num in nums
		if there is no any item in DP  - or current val is grater than last item of DP
			we can add num to DP directly
		else
			call bisect_left : will get left most item.
			we can set directly dp[insert_point_from_bst] = val
'''


from typing import List
from bisect import bisect_left


class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		if not nums:
			return 0
		dp = list()

		for val in nums:
			
			print(" val : ", val)
			print(" DP : ", dp)

			if not dp or val > dp[-1]:
				print("	dp will append val : ", val)
				dp.append(val)
			else:
				print("			we will send to bisect . dp ; ", dp ,  " - val :" , val)
				insert_point = bisect_left(dp, val)
				print(" 		insert_point :", insert_point)
				dp[insert_point] = val
				print(" 		DP after bisect : ", dp)
			print("-------------------------------------")

		print("Final DP :", dp)
		return len(dp)


nums = [10,9,2,5,3,7]

res = Solution().lengthOfLIS(nums)

print("res : ", res)


'''
	T(N) = O(N log N) : Binary search
	S(N) = O(N) dp array
'''
'''
	if a question include some words like "in array, contiguous subarray of given length k" , We can apply sliding window approach for this question.

	first 
		we need to get total till the 'K'

	and we can start k and till the length of nums

	we need a global_sum and local_sum. 
	local_sum keeps total , global_sum is gonna be keep max sum

	in a sliding window , we can slide each total K size, in the current array.
	
	nums = [1,12,-5,-6,50,3]

	first total till the k > (1+12-5-6) = 2
	second total > 12,-5,-6,50 = 51

	question is how to contunie to keep our total. 


'''
from typing import List
class Solution:
	def findMaxAverage(self, nums: List[int], k: int) -> float:

		global_sum = 0
		local_sum = 0

		local_sum = sum(nums[:k])
		global_sum = local_sum

		for i in range(k,len(nums)):
			local_sum += nums[i] - nums[i-k]
			global_sum = max(global_sum, local_sum)

		return global_sum/k


nums = [1,12,-5,-6,50,3]
k = 4
res = Solution().findMaxAverage(nums, k)
print("res :", res)


'''
	T(N) = O(N) we have just 1 iterate
	S(N) = O(1) There is no extra space
'''
		

'''
Problem : 
	Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

	Return the running sum of nums.

	 

	Example 1:

	Input: nums = [1,2,3,4]
	Output: [1,3,6,10]
	Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


	Solution : 
		We can iterate by keeping a prefix sum. 
		and we can change nums array

'''

from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
    	if not nums:
    		return 0

    	n = len(nums)
    	if n == 0:
    		return 0

    	prefix_sum = 0
    	for i in range(n):
    		prefix_sum = prefix_sum + nums[i]
    		nums[i] = prefix_sum

    	return nums



nums = [1,2,3,4]
nums = [1,1,1,1,1]
nums = [3,1,2,10,1]
res = Solution().runningSum(nums)
print("res ; ", res)


'''
 T(N) = O(N) 1 loop 
 S(N) = O(1) no extra space we did inline
 '''
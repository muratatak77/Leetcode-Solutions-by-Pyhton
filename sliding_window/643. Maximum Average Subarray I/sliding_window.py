'''
Question : 
	Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. 
	And you need to output the maximum average value.
	
	Input: [1,12,-5,-6,50,3], k = 4
	Output: 12.75
	Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

--------------

	We can apply sliding window sum approach. 

	like nums = [1,12,-5,-6,50,3], k = 4

	initialy we can get a first total using by adding up to 'K' in nums. 
		
		1+12-5-6 = 13-11 = 2

		our window total  = 2 in initialy.

		and we can start an iterator start K and to the lenght of nums array.

			for i in range(k,n):

				# we can find a next index total by extracting nums[i] - nums[i-k]. (look at the images for logic)
				# we can slide window to the right just 1 index. and we can get new total

				windowtotal += nums[i] - nums[i-k] 
							   50      - 1         = 49

				and finally we can use max method and getting max total.


'''
from typing import List
class Solution:
	def findMaxAverage(self, nums: List[int], k: int) -> float:

		if len(nums) < k:
			return 0

		wsum = sum(nums[:k]) # first total to the K.
		wmaxsum = wsum

		for i in range(k,len(nums)):
			wsum += nums[i] - nums[i-k]
			wmaxsum = max(wmaxsum, wsum)

		return float(wmaxsum)/k

nums = [1,12,-5,-6,50,3]
k = 4
res = Solution().findMaxAverage(nums, k)
print("res :", res)


'''
	T(N) = O(N) we have just 1 iterate
	S(N) = O(1) There is no extra space
'''
		

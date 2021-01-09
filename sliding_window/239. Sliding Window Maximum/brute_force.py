'''
	In Brute force approacing we can apply sliding window fix length solution.
	Our function is (N-k+1)
	We can walk trough first index to N-k+1

		like = nums = [1,3,-1,-3,5,3,6,7], k = 3

		start first index to the 6 index. (1,3,-1,-3,5,3)

		and we can check for each i > K item  max(nums[i:i+k])


'''
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        if n*k == 0:
        	return []

        result = []
        for i in range(n-k+1):
        	max_number = max(nums[i:i+k])
        	result.append(max_number)

        return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = Solution().maxSlidingWindow(nums, k)
print("res : ", res)
        	

'''
	T(N) = O(Nk) N : number of element is array.
			max(nums[i:i+k]) > k
	S(N) = O(N-K+1) for an output array
'''
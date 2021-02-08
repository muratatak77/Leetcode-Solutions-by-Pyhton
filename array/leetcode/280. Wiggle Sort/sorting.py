'''
	we can called zig-zag approach
	if i index is even should be nums[i] > nums[i+1] 
	if i index is odd should be nums[i] < nums[i+1] 

	we can make an if case together reverse appoarch
	
'''

from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
        	if (i%2 == 0 and nums[i]>nums[i+1]) or (i%2 == 1 and nums[i]< nums[i+1]):
        		nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
        	

nums = [3,5,2,1,6,4]
res = Solution().wiggleSort(nums)
print("res  :", res)

'''
Medium

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]


------------------------------

T(N) = O(N)
S(N) = O(1)

'''
'''
	[1,1,1]
	we can check every sub array inside the 2 loops. 
	we can call start, end for two checking points
		for every start and end points we need extra an iterate walk trough beetween start and end points
			to calculate sum sub array.

	for start
		for end
		 	sum = 0
		 	for i in start to end
		 		sum += nums[i]
		 	if sum == k:
		 		count += 1

	return count

'''

from typing import List
class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		n = len(nums)
		count = 0

		for start in range(n):
			for end in range(start, n):

				sum_pre = 0
				for i in range(start,end+1):
					sum_pre += nums[i]

				if sum_pre == k:
					count += 1

		return count

nums = [1,1,1]
k = 2
res  = Solution().subarraySum(nums, k)
print("res : ", res)


'''
	T(N) = O(N^3) .  Every possible sub array takes O(n^2) time. 
	For each of the subarray we calculate the sum taking O(n) in the worst case. 
	S(N) = O(1) No extra space

'''

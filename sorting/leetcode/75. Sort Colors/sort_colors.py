'''
	we can apply by the 3 pointer solution.
	We need p0,p2,and curr variables.
	p0 is keeping 0-
	p2 is keeping 2

	curr is just curr item.

	if we cross number 2 we can move end of array, but if we accross the 0 we need to move left of the array.

		   p0		 p2
	arr = [2,0,2,1,1,0]
		  curr	

		  if arr[curr] == 2:
			#carry to right
			swap(curr,p2) 

		  if arr[curr] == 0:
			#carry to left
			 swap(curr, p0)

		  if arr[curr] == 1:
			#just increment curr
			 curr += 1

'''

from typing import List
class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		
		#start points 
		p0 = 0
		curr = 0

		#end points
		p2 = len(nums)-1

		while curr < p2:
			if nums[curr] == 0:
				nums[curr], nums[p0] = nums[p0], nums[curr]
				p0 += 1
				curr += 1
				
			elif nums[curr]== 2:
				nums[curr], nums[p2] = nums[p2], nums[curr]
				p2 -= 1

			else:
				curr += 1

		return nums

nums = [2,0,2,1,1,0]
res = Solution().sortColors(nums)
print("res : ", res)

'''
	T(N) = O(N)
	S(N) = O(1) No extra space , inplace pass
'''


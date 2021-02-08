'''
	We can apply cycle sort approacing for this problem.
	
	like  :
	nums = [1,3,4,2,2]

	we will make to swap some item in this array for appropiate it's incides.
	
	like after swipe : 

		2,1,2,3,4
		
		how ?

		we start an iteration i;


			while nums[i] != i:  
				if we get an equal current index this item means in the right index in original array. We don't touch.
				but if this index in not match to an array item we need to swap.
					we need an destination params to straight an ideal list.
					d = nums[i]
					if nums[i] != nums[d]
						swap(nums[i],numd[d])
			





 
'''

from typing import List
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:

		n = len(nums)
		for i in range(0,n):
			print("i: ", i)
			while nums[i] != i:
				d = nums[i]
				print(" d : ", d)
				if nums[i] != nums[d]:
					nums[i], nums[d] = nums[d], nums[i]
					print("		 nums after swap :", nums)
				else:
					print("BREAK")
					break

		print("nums : ",  nums)

		for i in range(0,n):
			if nums[i] != i:
				return nums[i]


nums = [1,3,4,2,2]

res = Solution().findDuplicate(nums)
print("res : ", res)
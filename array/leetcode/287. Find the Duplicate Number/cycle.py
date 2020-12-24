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
    				break

    	print("nums : ",  nums)

    	for i in range(0,n):
    		if nums[i] != i:
    			return nums[i]


nums = [1,3,4,2,2]

res = Solution().findDuplicate(nums)
print("res : ", res)
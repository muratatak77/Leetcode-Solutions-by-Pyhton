'''
	We can apply fast and slow pointer approach for this question.
	
		Slow pointer goes one by one acccording to nums index
			slow = nums[slow]

		Fast pointer goes twice according to nums inside nums index.
			fast = nums[nums[fast]]

	And we can find common intersection so they can reach in the same item.
		
	And again slow pointer start 0, we don't touch fast pointer index.
	We can start to ahead by one by this time.
		slow = nums[slow]
		fast = nums[fast]

		if they are same bingo..

'''
from typing import List
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:

		slow = 0
		fast = 0
		#find intersection
		while True:
			print("slow 0: ", slow)
			print("fast 0: ", fast)
			slow = nums[slow]
			fast = nums[nums[fast]]
			print("slow 1: ", slow)
			print("fast 1: ", fast)
			if slow == fast:
				break
			print("-----")

		#find cycle trough same way
		slow = 0
		while slow != fast:
			print("slow 0: ", slow)
			print("fast 0: ", fast)
			slow = nums[slow]
			fast = nums[fast]
			print("slow 1: ", slow)
			print("fast 1: ", fast)
			print(">> -----")

		return slow



nums = [1,3,4,2,2]
res = Solution().findDuplicate(nums)
print("res : ", res)

''' 
	T(N) = O(N) while loop
	S(N) = O(1) no extra space
'''


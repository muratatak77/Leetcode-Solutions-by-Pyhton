'''
	we can apply 2 pointer approach that they would be left and right.
	this solution is in-place and linear time solution.

'''
from typing import List
class Solution:
	def reverseString(self, s: List[str]) -> None:
		"""
		Do not return anything, modify s in-place instead.
		"""
		
		#edge case
		if not s:
			return ""

		left = 0
		right = len(s)-1

		while left < right:
			s[left],s[right] = s[right],s[left]
			left += 1
			right -= 1

		return s

s = ["h","e","l","l","o"]
res = Solution().reverseString(s)
print("res : ", res)
'''
	We can apply a recurcive approcing for this question.
	like : 
								2326
	
				2 326					  23 26	

			2 3 26					23 2 6    23 26 (+1)

		23 2 6		23 26 (+1)   232 6 (+1)		

	232 6 (+1)
(
we did and we can return ans = 1. 
and we can increemnt)

Finally we can get totaly 4.

Cases : 
	if we have 0 we can skip 

'''

class Solution:
	def numDecodings(self, s: str) -> int:


		def helper(index, s):
			print("index : ,", index)
			#leaf node case
			#if we reach end of the recursion we can return 1
			if index == len(s):
				return 1

			#if we have 0 , we can skip
			if s[index] == '0':
				return 0

			if index == len(s)-1:
				return 1

			#recursive case
			#call helper just added 1 to the index (index+1)
			ans = helper(index+1, s)

			#call helper just added 2 (index+2)
			if int(s[index:index +2]) <= 26:
				ans += helper(index+2,s)

			return ans

		return helper(0,s)


s = "2326"
res = Solution().numDecodings(s)
print("res : ", res)
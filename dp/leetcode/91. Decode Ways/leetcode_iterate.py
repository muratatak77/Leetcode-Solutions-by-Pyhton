'''
	
'''

class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		print("S: ", s)

		if not s:
			return 0

		# Array to store the subproblem results
		dp = [0 for _ in range(len(s) + 1)]

		print("DP : ", dp)

		dp[0] = 1
		# Ways to decode a string of size 1 is 1. Unless the string is '0'.
		# '0' doesn't have a single digit decode.
		dp[1] = 0 if s[0] == '0' else 1

		print("DP 2 : ", dp)


		for i in range(2, len(dp)):
			print(" i : ", i)
			# Check if successful single digit decode is possible.
			if s[i-1] != '0':
				dp[i] += dp[i-1]
				print("   one digit: ", s[i-1])
				print("   DP 3 : ", dp)
				print("------------------- ")

			# Check if successful two digit decode is possible.
			two_digit = int(s[i-2 : i])
			print("		two_digit : ", two_digit)
			if two_digit >= 10 and two_digit <= 26:
				dp[i] += dp[i-2]
				print("		DP 4 : ", dp)
				print("		------------------- ")

		return dp[len(s)]


s = "226"
s= "1020"
s= "2223"
s= "2326"
res = Solution().numDecodings(s)
print("res :", res)
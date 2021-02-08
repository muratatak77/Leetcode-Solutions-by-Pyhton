'''
	we can apply DP approach. 
	we gonna generate 1d DP array lenght of len(s) + 1.  + 1  = We need start index 1. index 0 should be 1 every time.
	we will check one digit and second digit in a loop.

		one digit should grater than 0
		two digits should beetween 10 and 26

		we can sum for first digit , total one previous and curent item,
		for two digits we can sum  2 previoueses item and current item

'''
class Solution(object):
	def numDecodings(self, s):
	
		dp = [0 for _ in range(len(s)+1)]	
		print("DP : ", dp)

		dp[0] = 1

		if s[0] != '0':
			dp[1] = 1

		print("DP : ", dp)

		for i in range(2, len(dp)):
			one_digit = int(s[i-1:i])
			two_digits = int(s[i-2:i])

			if one_digit >= 1:
				dp[i] += dp[i-1]
			if two_digits >= 10 and two_digits <= 26:
				dp[i] += dp[i-2]

		print("DP : ", dp)

		return dp[len(s)]


s = "226"
s= "1020"
s= "2223"
s = "0"
s = "01"
res = Solution().numDecodings(s)
print("res :", res)

'''
 T(N) = O(N)  N length of string.
 
 S(N) = O(N) 

'''
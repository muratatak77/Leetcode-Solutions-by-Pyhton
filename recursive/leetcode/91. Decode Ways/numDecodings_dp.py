'''
	We can apply a dp iterative approcing for this question.
	we need to generate a dp 1D array 

	like : 
	s = "2326"
	dp = [0,0,0,0,0]

	first we can put just 1 , for passing

	if we don't have 0 as a first char, we can add 1

	item = 2
	dp = [1,1,0,0,0]

	and we can start a iterate to fill other items
	
	we can increment just 1 :

		s = 3 
		we can bring 
			dp[i] = dp[i-1]
			dp = [1,1,1,0,0]

	we can check before 2 chars

		s= 23
		we can bring
			dp[i] += dp[i-2:i]  # [1,1] = 2
			dp = [1,1,2,0,0]

	---------

		s = 2
			dp = [1,1,2,2,0]

		s = 32 > 26 X

	---------

		s = 6
			dp = [1,1,2,2,2]


		s = 26 = 26 
			dp = [1,1,2,2,4]

	return dp[len(s)]

'''

class Solution:
	def numDecodings(self, s: str) -> int:

		dp = [0] * (len(s)+1)
		print("dp : ", dp)

		dp[0] = 1

		if s[0] == 0:
			dp[1] = 0
		else:
			dp[1] = 1

		print("dp : ", dp)

		for i in range(2,len(dp)):
			#check first item
			if s[i-1] != '0':
				dp[i] = dp[i-1]

			#check both items
			two_digit = int(s[i-2:i])
			if two_digit >= 10 and two_digit <= 26:
				dp[i] += dp[i-2]

			print("dp : ", dp)

		return dp[len(s)]


s = "2326"
res = Solution().numDecodings(s)
print("res : ", res)

'''
	T(N) = O(N) , N len of the string. We iterate the length of dp is N +1 
	S(N) = O(N), lenght of DP array

'''
'''
	If we think brute force: 
		we need to check every substring and whether is palindrome or not.
		Time complexity will be N^3

	We can imprrove this quesition using by DP approach.

		 - for every single char is palindrome  > a
		 - 2 chars both the same  > aa
		 - if we have string size > 2 we need to check first and last char and if remain char is palindrome finally this string will be palindrome.


		a b a c
		0 1 2 3
		
		some examples:

		 0 - 0 >  a - a > is palindrome
		 0 - 1 >  a - b > is not palindrome
		 0 - 2 >  a - b - a > is palindrome

		
		on the grid ; 



		 0    1    2     3
		 a    b    a     c
	0 a  1       
	
	1 b        1    

	2 a             1 

	3 c					 1

		 - we can see on the grid dioginal line is palindrome everytime. Because one char everytime is palindrome.
		 - go second case 
				grid[0,1] > ab  > is not a palindrome. 
				grid[0,2] > aba > palindrome we can put 1 in this cell. and we can increment a global answer +1.
				grid[0,3] > abac > not palindrome.
		
				if we see grid[1,0] > "ba" is same thing with the  grid[0,1] > "ab" . Thats why we don't need bottom left half of diogonal part in the grid.
				Becuase is mirrod bottom left and top right. 

				grid[1,2] > ba > is not palindrome
				grid[1,3] > bac is not palindrome

				grid[2,3] > ac > is not palindrome


'''

class Solution:
	def countSubstrings(self, s: str) -> int:
		
		n = len(s)
		if n <= 0:
			return 0

		ans = 0

		#generate a grid
		dp = [[0] * n for _ in range(n)]
		print("Initial Grid : ", dp)

		#base case , single letter chars
		for i in range(n):
			dp[i][i] = 1
			ans += 1

		# #base case, double letters substrings
		# for i in range(n-1):
		# 	if s[i] == s[i+1]:
		# 		dp[i][i+1] = 1
		# 		ans += 1

		print("dp : ", dp , " - ans : ", ans)

		#all other cases : substring of length 3 to n. WE found single and double chars
		# for k in range(3,n+1):
		# 	i = 0
		# 	for j in range(i+k-1,n+1):
		# 		if dp[i+1][j-1] == 1 and s[i] == s[j]:
		# 			dp[i][j] = 1
		# 			ans += 1
		# 	i+=1

		for col in range(1,len(s)):
			for row in range(col):
				print("col : ", col, " - row : ", row)
				#double letter check
				if (row==col-1) and (s[col]==s[row]):
					dp[row][col]=1
					ans +=1
					print("	dp 1 : ",  dp)
				#all other cases
				elif dp[row+1][col-1]==1 and s[col]==s[row]:
					dp[row][col]=1
					ans +=1
					print("	dp 2: ",  dp)


		return ans

s = "aaa"
s = "aabaaca"
res = Solution().countSubstrings(s)
print("res : ", res)


'''
	T(N) = O(N^2)
	O(N) = O(N^2)
	
'''













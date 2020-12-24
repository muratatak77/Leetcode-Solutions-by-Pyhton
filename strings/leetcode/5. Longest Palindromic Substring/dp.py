def longestPalindrome(s):

	if not s:
		return ""
	
	n = len(s)
	if n == 1:
		return s

	dp = [[0] * n for _ in range(n)]
	# mark all elements of some order diagonal  as true as all (i,j) can only have a single char 
	# and they have always a palindrome

	for i in range(0,n):
		dp[i][i] = 1

	start = 0 
	end = 0
 
	for i in range(n):
		for j in range(i):			
			if s[i] == s[j]:
				if i-j == 1 or dp[j+1][i-1] == 1:
					dp[j][i] = 1
					if (end-start < i-j):
						print("end - start : ", end - start)
						print("i - j : ", i - j)
						start = j
						end = i
			else:
				dp[j][i] == 0
	return s[start:end+1]



s = "babad"
res = longestPalindrome(s)
print(res)
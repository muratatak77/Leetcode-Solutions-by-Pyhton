#doesnt work
def longestPalindrome(s):

	if not s:
		return ""
	
	n = len(s)
	if n == 1:
		return s

	left = 0
	right= 0
	ans = left, right

	for i in range(n):
		left = i
		right = i

		while left >= 0 and right < n and s[left] == s[right]:
			left -= 1
			right += 1
		ans = left+1, right-1

		print("left : ", left)
		print("right : ", right)

		left = i
		right = i+1

		while left >= 0 and right < n and s[left] == s[right]:
			left -= 1
			right += 1
		ans = left+1, right-1

	print("left : ", left)
	print("right : ", right)
	return s[ans[0]:ans[1]+1]


s = "babad"
res = longestPalindrome(s)
print(res)

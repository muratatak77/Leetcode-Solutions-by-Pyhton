def longestPalindrome(s):

	if not s:
		return ""
	
	n = len(s)
	if n == 1:
		return s

	start, end = 0,0
	for i in range(n):
		print("i : ", i)
		len1 = expandAroundCenter(s,i,i)
		print("len1 : ", len1)
		len2 = expandAroundCenter(s,i,i+1)
		print("len2 : ", len2)
		max_len = max(len1, len2)
		print("max_len : ", max_len)

		if max_len > end-start:
			print("We ll set start and end ")
			start = i - (max_len-1)//2
			print("start : ", start)
			end = i + max_len//2
			print("end : ", end)

		print("==============")

	return s[start:end+1]

def expandAroundCenter(s, left, right):
	L = left
	R = right
	print("L : " , L , " - R :", R)
	while L >= 0 and R < len(s) and s[L] == s[R]:
		print("s[L] : ", s[L], " - s[R] :", s[R])
		print("We have found s[L] = s[R]. L : " , L , " - R :", R )
		L -= 1
		R += 1
	print("Return from expandAroundCenter : " , R-L-1)
	return R-L-1

s = "babad"
res = longestPalindrome(s)
print(res)
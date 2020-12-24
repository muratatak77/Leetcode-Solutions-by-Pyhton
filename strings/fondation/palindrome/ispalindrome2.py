def isPalindrome(s):

	i, j = 0, len(s) - 1
	print("initial i : ", i , " - j : ", j)

	while i < j:
		print("s[i] : ", s[i])
		print("s[j] : ", s[j])
		while i < j and not s[i].isalnum():
			i += 1
			print("  i : ", i , " - j : ", j)
			print("  s[i] : ", s[i])

		while i < j and not s[j].isalnum():
			j -= 1
			print("  i : ", i , " - j : ", j)	
			print("  s[j] : ", s[j])

		if i < j and s[i].lower() != s[j].lower():
			return False

		i += 1
		j -= 1
		
		print("-  i : ", i , " - j : ", j)
		print("==========================")

	return True


s = "r,e.dd.e,r"
s = "r.....r"
print(isPalindrome(s))
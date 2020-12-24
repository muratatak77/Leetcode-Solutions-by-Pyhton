def convert(str1,str2):
	
	if len(str1) != len(str2):
		return False

	if str1 == str2:
		return True

	if len(set(str2)) >= 26:
		return False

	conversions = {}

	for c1,c2  in zip(str1,str2):
		if c1 == c2 and c1 not in conversions:
			continue
		
		if c1 in conversions:
			if conversions[c1] != c2:
				return False
		else:
			conversions[c1] = c2

	return True


str1 = "aabcc"
str2 = "ccdee"

str1 = "leetcode"
str2 = "codeleet"

str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "bcdefghijklmnopqrstuvwxyza"


res = convert(str1, str2)
print("res : ", res)
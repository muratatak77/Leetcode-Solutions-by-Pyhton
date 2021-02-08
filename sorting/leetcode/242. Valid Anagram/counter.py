def isAnagram(s,t):

	if len(s) != len(t):
		return False

	counter1= {}
	counter2= {}

	for char in s:
		counter1[char] = counter1[char] + 1 if char in counter1 else 1

	for char in t:
		counter2[char] = counter2[char] + 1 if char in counter2 else 1

	return counter1 == counter2



s1 = "anagram"
s2 = "nagaram"

res = isAnagram(s1, s2)
print(res)
def isAnagram(s1, s2):

	if not s1 or not s2:
		return False

	if len(s2) != len(s1):
		return False

	counter = []
	for i in range(1,27):
		counter.append(i)

	print(counter)

	for i in range(len(s1)):
		counter[ord(s1[i]) - ord("a")] += 1
		counter[ord(s2[i]) - ord("a")] -= 1
		# counter[s2[i]] -= 1 if s1[i] in counter else 1
	
	print(counter)



# def isAnagram(s,t ):
#     counterS, counterT = {}, {}
#     for char in s:
#         counterS[char] = counterS[char] + 1 if char in counterS else 1
#     for char in t:
#          counterT[char] = counterT[char] + 1 if char in counterT else 1
#     return counterS == counterT



s1 = "anagram"
s2 = "nagaram"

res = isAnagram(s1, s2)
print(res)
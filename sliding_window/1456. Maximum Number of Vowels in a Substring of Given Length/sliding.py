'''
Q : 
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).
------------------------------------------------


Solution : 


	We can apply sliding wondow fix lenght approach fot this question.
	s = "abciiidef" 
	k = 3
	
	we can store a set all vowel chars. 

	set = ('a','i','e','u','o')
	in initial we can walk trough in loop to K.

	second part :
	we can walk trough again in loop start K  to len(s)

		if s[i] include in a vowelset we can increment our local counter  label.
		for next item in sliding window if s[i-k] in vowelset, we can decrement our local label.

'''
class Solution:
	def maxVowels(self, s: str, k: int) -> int:

		if not s:
			return 0
		if len(s) == 0:
			return 0
		
		vowelset = set('aieuo')
		numvowel = 0
		globalmax = 0
		#initial
		for i in range(k):
			if s[i] in vowelset:
				numvowel += 1

		globalmax = numvowel

		#reamin after k
		for i in range(k,len(s)):
			if s[i] in vowelset:
				numvowel += 1
			if s[i-k] in vowelset:
				numvowel -= 1

			globalmax = max(globalmax, numvowel)

		return globalmax

s = "abciiidef"
s = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"

k = 3
k = 33

res = Solution().maxVowels(s, k)
print("res :", res)

'''
	T(N) = O(N)
	S(N) = O(1)
'''
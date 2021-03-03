'''
	We can apply gready approaching. 

	palindrome means: same string if we reverse again same.

	as a first:
		we need 2 variable. 
		
		low = 0
		high = len(string)

		we can check low and high in an iterate.
		if they are same ok we can contunie iterate and we can increment low , we can decrement high
			
			low++
			high--

		else:

			we need remove first char from string and we can check ispalindrome or not
			we need remove last char from string and we can check again ispalindrome or not

			if is not palindrome in any case we can return false

		finally we can return True
'''
class Solution:
	def validPalindrome(self, s: str) -> bool:
		
		if not s:
			return s

		def ispalindrome(low, high):
			while low < high:
				if s[low] != s[high]:
					return False
				low += 1
				high -= 1
			return True

		low = 0
		high = len(s)-1

		while low<high:
			if s[low] == s[high]:
				low += 1
				high -= 1
			else:
				#we can remove str[low], and we need to check again is palindrome or not
				return ispalindrome(low+1, high) or ispalindrome(low, high-1)
		
		return True

s = "abca"
s = "abecbea"
s = "aba"

res = Solution().validPalindrome(s)
print("res :", res)


'''
	T(N) = O(N) N is the length of string
	s(N) = O(1) no extra space
'''
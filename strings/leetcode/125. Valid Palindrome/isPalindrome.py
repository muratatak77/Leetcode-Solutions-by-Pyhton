class Solution:
	def isPalindrome(self, s: str) -> bool:

		i, j = 0, len(s) - 1

		print("i : ", i , " - j : ", j)


		while i < j:

			print("			i : ", i , " - j : ", j)


			while i < j and not s[i].isalnum():
				print("s[i] : ", s[i])
				i += 1
				print("					i : ", i , " - j : ", j)

				# print("			s[i] : ", s[i])

			
			# print(" 		>>     i : ", i , " - j : ", j )

			while i < j and not s[j].isalnum():
				j -= 1
				print(" 2					i : ", i , " - j : ", j)

				# print("			s[j] : ", s[j])

			if s[i].lower() != s[j].lower():
				return False


			i += 1
			j -= 1

			print("-----------------------")

		return True



s = "A man, a plan, a canal: Panama"
res = Solution().isPalindrome(s)
print("res : ", res)
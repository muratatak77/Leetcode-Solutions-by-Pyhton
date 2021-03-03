'''
	we can use find method
	we can set in initial first item as a prefix.
	s = ["flower","flow","flight"]
	
	prefix = "flower"

	while loop :

		"flow".find("flower") = -1
			we can remove last char from prefix.
			then prefix will be 'flowe'. (we can use substring method.)

	"flow".find("flowe") = -1

	"flow".find("flow") = 0 

		if we have 0 we can exit iterate and we can return prefix

'''

from typing import List
class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:

		if not str:
			return ""
		prefix = strs[0]
		print("Initial prefix : ", prefix)

		for i in range(1,len(strs)):
			print("	i ; ", i)
			print("	strs i: ", strs[i])
			print("	strs[i].find(prefix): ", strs[i].find(prefix))

			while strs[i].find(prefix) != 0:

				prefix = prefix[0:len(prefix)-1]

				print("prefix : ", prefix)

				if not prefix or len(prefix)==0:
					return ""
				print("--------- while loop ----- ")
			print(">>>>>>>>> for loop -----")


		return prefix

s = ["flower","flow","flight"]
res = Solution().longestCommonPrefix(s)
print("res : ", res)


'''
	O(N) = O(S) S is sum of the all chars in Strings in the worst case. We can iterate and compare all chars.
	S(N) = O(1) 

'''
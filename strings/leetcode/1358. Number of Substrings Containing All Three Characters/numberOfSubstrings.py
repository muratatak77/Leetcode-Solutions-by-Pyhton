from collections import defaultdict
class Solution:
	def numberOfSubstrings(self, s: str) -> int:
		counter = defaultdict(int)
		size = len(s)
		print("SIZE : ", size)

		ans = 0
		j = 0

		for i, val in enumerate(s):

			print("		i :", i, "- val :", val)

			counter[s[i]] +=1

			print("			counter :", counter)

			while counter['a'] > 0 and counter['b'] > 0 and counter['c'] > 0:
				ans += size - i
				print("				ans : ", ans)
				counter[s[j]] -=1
				print("				counter : ", counter)
				j +=1
				print("				j : ", j)

			print("-------------------------------------------")
		return ans


s = "abcabc"
# s = "aaacb"

res = Solution().numberOfSubstrings(s)

print("res : ", res)
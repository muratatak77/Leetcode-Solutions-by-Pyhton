class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		n = len(s)
		ans = 0
		# mp stores the current index of a character
		mp = {}

		i = 0
		# try to extend the range [i, j]
		for j in range(n):
			print("s[j] :", s[j])
			print("j : ", i)

			if s[j] in mp:
				i = max(mp[s[j]], i)
				print(" 		i : ", i)

			ans = max(ans, j - i + 1)
			print("ans : ", ans)
			mp[s[j]] = j + 1
			print("map : ", mp)
			print("============")

		return ans

		

s = "abcabcbb"
s = "abcdeafbdgcbb"
res = Solution().lengthOfLongestSubstring(s)
print("res: ", res)
'''


'''
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		chars = [0] * 128
		print("chars : ", chars)

		left = right = 0

		res = 0
		while right < len(s):
			print("right : ", right)
			r = s[right]
			chars[ord(r)] += 1
			print("		r : ", r)
			print("		ord(r) : ", ord(r))
			print("		chars : ", chars)


			while chars[ord(r)] > 1:
				l = s[left]
				print(" 			l : ", l)
				chars[ord(l)] -= 1
				print("				chars : ", chars)
				left += 1
				print(" 			left : ", left)

			res = max(res, right - left + 1)
			print(" res : ", res)

			right += 1
		return res


s = "abcabcbb"
s = "abcdeafbdgcbb"
res = Solution().lengthOfLongestSubstring(s)
print("res: ", res)

			
'''
	T(N) = O(N) index j will travel n times
	S(N) = Hashmap = O(min(m,n)) The size of set uppor bounded by the size of the string n
	and size pf the charset/alphabet m

'''
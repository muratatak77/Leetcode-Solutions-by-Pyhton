class Solution:
	def countSubstrings(self, s: str) -> int:
		
		n = len(s)
		if n <= 0:
			return 0
		ans = 0

		def coundPalindromeAroundCenter(lo,hi):
			print("	call > lo : ", lo , " - hi : ", hi)
			count = 0
			while lo >= 0 and hi < len(s):
				print("		lo : ", lo , " - hi : ", hi)
				print("		s[lo] :", s[lo],  " - s[hi] :", s[hi])
				if s[lo] != s[hi]:
					break
				lo -= 1
				hi += 1
				count += 1
				print("			count :", count)
				print("			-------------------------")
			return count
			
		for i in range(n):
			print(" i : ", i)
			ans += coundPalindromeAroundCenter(i,i)
			ans += coundPalindromeAroundCenter(i,i+1)
			print("--------------------------------------")


		return ans



s = "aaa"
s = "aabaaca"
res = Solution().countSubstrings(s)
print("res : ", res)



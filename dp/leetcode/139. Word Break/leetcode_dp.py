class Solution:
	def wordBreak(self, s, wordDict):

		hmap = {}
		for word in wordDict:
			hmap[word] = 1
		print("hmap : ", hmap)

		table = [False] * (len(s)+1)
		table[0] = True

		print("table :", table)
		for i in range(1,len(table)):
			for j in range(0,i+1):

				print("   j : ", j , " - i : ", i)
				print("  s[j:i]:  ", s[j:i] )
				print("  table[j] :  ", table[j]  )
				print("		table :", table)

				if table[j] and s[j:i] in hmap:
					table[i] = True
					print("       >>>>>>> table[i] = True: ", table[i])
					break
				print("   ========= j end =================")
			print("========= i end =================")	
		
		print("		table :", table)

		return table[-1]




s = "leetcode"
# s = "leeecode"
wordDict = ["leet", "code"]


# s = "applepenapple"
# wordDict = ["apple", "pen"]


ans = Solution().wordBreak(s,wordDict)
print(ans)




# Success
# Details 
# Runtime: 36 ms, faster than 88.17% of Python3 online submissions for Word Break.
# Memory Usage: 13.9 MB, less than 81.93% of Python3 online submissions for Word Break.
# Next challenges:
# Word Break II
# Show off your acceptance:
# Time Submitted
# Status
# Runtime
# Memory
# Language
# 08/31/2020 11:29	Accepted	36 ms	13.9 MB	python3


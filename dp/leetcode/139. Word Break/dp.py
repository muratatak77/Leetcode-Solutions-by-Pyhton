class Solution:
    def wordBreak(self, s, wordDict):

    	hmap = {}
    	for word in wordDict:
    		hmap[word] = 1
    	print("hmap : ", hmap)

    	table = [False]*(1+len(s))
    	print("table : ", table)

    	for i in range(1,len(table)):
    		# print(" i :" , i)
    		# print(" s[:i] :" , s[:i])

    		table[i] = (s[:i] in hmap)
    		# print(" table[i] : ", table[i])

    		for j in range(1,i+1):
    			print("   j : ", j , " - i : ", i)
    			print("   s[i-j:i]: ", s[i-j:i])
    			print("   table[i-j]:  ", "table[", i-j ,"] :", table[i-j] )
    			if s[i-j:i] in hmap and table[i-j] == True:
    				print("       table[i] = True: ", table[i])
    				table[i] = True
    				break

    			# print("   ========= j end =================")

    		# print("========i end ==================")

    	print("Final table : ", table)
    	print("Final table[-1] : ", table[-1])

    	return table[-1]


s = "leetcode"
# s = "leeecode"
wordDict = ["leet", "code"]


# s = "applepenapple"
# wordDict = ["apple", "pen"]


ans = Solution().wordBreak(s,wordDict)
print(ans)



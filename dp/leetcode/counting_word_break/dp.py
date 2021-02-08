def wordBreak(s, wordDict):

	hmap = {}
	for word in wordDict:
		hmap[word] = 1

	table = [0] * (1+len(s))

	for i in range(1, len(table)):
		
		if s[:i] in hmap:
			table[i] += 1

		for j in range(1,i+1):

			if s[i-j:i] in hmap:
				table[i] += table[i-j]
				print("table :", table)

	print("finally table : ", table)
	return table[-1]



s = "leetcode"
# s = "leeecode"
wordDict = ["leet", "code"]


# s = "applepenapple"
# wordDict = ["apple", "pen"]


ans = wordBreak(s,wordDict)
print(ans)
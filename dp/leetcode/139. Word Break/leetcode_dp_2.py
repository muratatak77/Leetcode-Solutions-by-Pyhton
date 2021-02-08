'''
	we have a word and word dictinoary. We need to check a word whether include in dict words or not. 
	We can generate a extra an array to check  whether equal or not our word in dicts words.
	
	like "leetcode"
	
	first extra space we can call  'table' will be :
	
	table =[ T, F, F, F, F,  F, F, F, F] 
	            l  e  e  t   c  o  d  e


	if we have a match we can change False to True. Final element will be False or True according to our matching. 

		we can check by the this way :

		for i in range(0, len(table))
		 for j  in range(0, i+1)

		 	i : 0 , j : 1 ,  

		 	i : 3 , j : 0  s[j:i] > lee 
		 	i : 3 , j : 1  s[j:i] > ee
		 	i : 3 , j : 2  s[j:i] > e
	
			if we have 
		 	i : 4 , j : 0 > s[j:i] > leet 
		 		check in dict : 
		 			table[i] = True
		 			break

		table =[ T, F, F, F, T,  F, F, F, T] 
	                l  e  e  t   c  o  d  e

	    we can return last element .

'''

class Solution:
	def wordBreak(self, s, wordDict):

		hmap = {}
		for word in wordDict:
			hmap[word]= 1

		

		table = [False] * (len(s)+1)
		table[0] = True

		for i in range(1, len(table)):
			for j in range(0,i+1):
				if table[j] and  s[j:i] in hmap:
					table[i] = True
					break

		return table[-1]


s = "leetcode"
# s = "leeecode"
wordDict = ["leet", "code"]

# s = "applepenapple"
# wordDict = ["apple", "pen"]

ans = Solution().wordBreak(s,wordDict)
print(ans)



'''
	T(N) : We have 2  nested loops O(N^2)
	S(N) : O(N) 
'''


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


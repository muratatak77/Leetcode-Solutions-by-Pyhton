'''
	we can use hash map to keep how many repeat in current string.
	we can increment a hash map value if we accross same item again.
		or we can just add with the just 1

	after we can iterate/enumarate in string. 
	
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:

    	hashmap = {}
    	for char in s:
    		if char in hashmap:
    			hashmap[char] += 1
    		else:
    			hashmap[char] = 1

    	print("hashmap : ", hashmap)

    	for idx,ch in enumerate(s):
    		if hashmap[ch] == 1:
    			return idx
    	return -1
    		

s = "leetcode"
s = "loveleetcode"
res = Solution().firstUniqChar(s)
print("res : ", res)
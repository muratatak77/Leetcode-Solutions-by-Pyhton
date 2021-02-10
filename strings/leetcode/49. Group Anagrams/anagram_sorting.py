'''
	we can iterate
	we can pick one 
	like 
	strs = ["eat","tea","tan","ate","nat","bat"]
	eat > sort >  aet. aet will be key , value will be eat
	we can use a list hash map dict(list)
	list_hash = 
		{
			(aet) : [eat]
		}
	
	second item is tea , > sorted > aet we have in hash map , we can update just list  
	
	list_hash = 
		{
			(aet) : [eat, tea]
		}

	and so on...
	

'''
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    	if not strs:
    		return []

    	hash_list = defaultdict(list)

    	for item in strs:
    		key = ''.join(sorted(item))
    		hash_list[key].append(item)

    	print("hash list: ", hash_list)

    	return hash_list.values()

strs = ["eat","tea","tan","ate","nat","bat"]

res = Solution().groupAnagrams(strs)
print("res : ", res)


'''
	T(N) = N : size  of strs , K : max lenght of a string string in strs. we sorted. >   O(NKlogK)
	S(N) = O(NK)
'''
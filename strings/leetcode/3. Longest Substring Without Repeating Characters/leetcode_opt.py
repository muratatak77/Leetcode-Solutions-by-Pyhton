'''
	We can apply sliding window approach in this question.
	
	like we have this string : "abcdeafbdgcbb"

	we can start i and j index from 0.
	In iteration we can walk trough j index. 
	and we will need an hash map to keeps that which index of current item.
	

	hmap = {a:1, b:2, c:3, d:4, e:5}

	so far, we have 5 chars that they are longest substring nonrepatively.
	our global answer ans  = max(ans, j-i+1)
	ans = 5
	because we are in the 5 th position and we have 

	when we have same item in the hash map , we can increment current item in hash map 
	and we don't need keep item in hash map with the same value.
	
	after comes a again
	what is a new poisition : "a b c d e a fbdgcbb" = 6
	we can increment for a value in hmap:

	hmap = {a:6, b:2, c:3, d:4, e:5} 


'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

    	if not s:
    		return 0
    	if len(s) == 0:
    		return 0

    	ans = 0
    	hmap = {}
    	i = 0

    	for j in range(len(s)):
    		if s[j] in hmap:
    			i = max(hmap[s[j]],i)
    		ans = max(ans, j-i+1)
    		hmap[s[j]] = j+1

    	return ans


s = "abcabcbb"
# s = "abcdeafbdgcbb"
res = Solution().lengthOfLongestSubstring(s)
print("res: ", res)

    		
'''
	T(N) = O(N) index j will travel n times
	S(N) = Hashmap = O(min(m,n)) The size of set uppor bounded by the size of the string n
	and size pf the charset/alphabet m

'''
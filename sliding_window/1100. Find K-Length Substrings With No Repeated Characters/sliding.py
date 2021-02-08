'''
Question : 

	Given a string S, return the number of substrings of length K with no repeated characters. 

	Example 1:

	Input: S = "havefunonleetcode", K = 5
	Output: 6
	Explanation: 
	There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.

Solution :
	
	We are using sliding window fix length approaching. Fix length = K


	we can store to keep and follow a hasmap. We can call frequescy character
	This hashmap will store What is count for each chars.
	Every loop we will check in the end len(hashmap) == K then we can understand whether increment or decrement our global count value.

	Input: S = "havefunonleetcode", K = 5
	
		hmap = {h:1, a:1, v:1, e:1, f:1}
		we can match len(hmap) with the K. 
		first matching is good and we can increment count = 1

	after we can slide our window for next item in String.
	
		hmap = {h:1, a:1, v:1, e:1, f:1, u:1}
		hmap[S[i-K]] -= s[i-K] 
		if need to remove first char in String and we need to add next item from the hmap.
		hmap will be :
			hmap = {a:1, v:1, e:1, f:1, u:1}
			len(hmap) == K . we can increment our global count.

		case in 'funon'
		map will be
		hmap = {f:1, u:1, n:2, o:1}
			len(hmap) != K . we can not increment our global count.

'''


class Solution:
	def numKLenSubstrNoRepeats(self, s: str, K: int) -> int:

		#edge cases
		if not s:
			return 0

		n = len(s)
		
		if n == 0 or n < K:
			return 0

		#initial process to K
		hmap = {}
		count = 0

		#check and store in hmap for each char 
		for i in range(K):
			if s[i] in hmap:
				hmap[s[i]] += 1
			else:
				hmap[s[i]] = 1


		if len(hmap) == K:
			count = 1

		print("hmap : ", hmap)
		print("count : ", count)


		#remain parts 
		for i in range(K,n):

			if s[i] in hmap:
				hmap[s[i]] += 1
			else:
				hmap[s[i]] = 1


			hmap[s[i-K]] -= 1

			if hmap[s[i-K]] == 0:
				del hmap[s[i-K]]

			print("		hmap : ", hmap, " / Len : ", len(hmap))

			if len(hmap) == K:
				count += 1

		return count


S = "havefunonleetcode"
K = 5

res = Solution().numKLenSubstrNoRepeats(S, K)
print("res : ", res)



'''
	T(N) = O(N)
	S(N) = O(K) we use frequency everytime K.
'''


'''
	1 - We can apply sliding window approach and hash map for this qeustion
	2 - We will insert characters from the begining of the string until we have  K distinct chars in the HashMap
	3 - This chars generate our sliding window. 
	4 - we will keep adding one char to the sliding window
	5 - in each step , we will try to shrink window from the beginning is the lenght of hash map is larger than "K". We will shrink the window 
	until we have no more than K distinct chars in the Hash Map.
	7 - While shringking we will decrement chars freq out of window and remove it from HashMap if its freq becomes zero.

	s= "eceba"
	k= 2

	freq_chars : {e:2, c: 1, b: 1}  > we have 3 distinct chars

	len(freq_chars) > 2

	freq_chars : {c: 1, b: 1, a:1}  > we have 3 distinct chars


'''
class Solution:
	def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
		max_lenght = 0
		window_start = 0
		freq_chars = {}

		for window_end in range(len(s)):
			right_char = s[window_end]
			if right_char not in freq_chars:
				freq_chars[right_char] = 0
			freq_chars[right_char] += 1

			#we need to shrink until len(freq_chars) grater than K
			while len(freq_chars) > k:
				left_char = s[window_start]
				freq_chars[left_char] -= 1
				if freq_chars[left_char] == 0:
					del freq_chars[left_char]
				window_start += 1

			max_lenght = max(max_lenght, window_end - window_start + 1)

		return max_lenght


s = "eceba"
k = 2

res = Solution().lengthOfLongestSubstringKDistinct(s, k)
print("res : ", res)

				
'''
Time Complexity #
The above algorithm’s time complexity will be O(N), where NN is the number of characters in the input string. 
The outer for loop runs for all characters, and the inner while loop processes each character only once; 
therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N)O(N).

Space Complexity #
The algorithm’s space complexity is $O(K), as we will be storing a maximum of K+1K+1 characters in the HashMap.

'''
			

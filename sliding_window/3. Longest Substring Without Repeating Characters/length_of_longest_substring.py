
# @param {String} s
# @return {Integer}
def length_of_longest_substring(s):
	window_start = 0
	max_length = 0
	char_index_map = {}
	n = len(s)
	for window_end in range(n):
		
		right_char = s[window_end]
		#if char index map include right char means , we need to shrink window. 
		#we need to change wondow_start position. 
		if right_char in char_index_map:
			#we need to keep window_start position. like "abba" case
			window_start = max(window_start, char_index_map[right_char] + 1)

		char_index_map[right_char] = window_end
		max_length = max(max_length, window_end - window_start + 1)

	return max_length


s = "aabccbb"
s = "abbbb"
s = "abccde"
s = "dvdf"
s = "abba"
res = length_of_longest_substring(s)
print("res ", res)
'''
	T(N) = O(N) - N number of chars input strings.
	S(N) = O(K) - K is number of distinct chars in input strings. 
				Means K <= N. Worst case all chars might not any repeating chars in the string , so entire string will be adding to the HashMap.
				We can expect a fixed set in the input strings (26 for english chars) , we can say alg runs in fixed space : O(1) : in this case we can use a fixed-size arr instead of HashMap


'''
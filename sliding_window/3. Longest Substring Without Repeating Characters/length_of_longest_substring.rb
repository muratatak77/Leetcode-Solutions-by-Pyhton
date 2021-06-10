=begin

	s = "a a b c a b b"
	window_end = 0 = a
	window_start =  0 = a 
	char_index_map = {a:0}
	---------------
	
	window_end = 1 = a
	window_start =  1 = a 
	char_index_map = {a:1}
	max_len  = 1
	---------------
	
	window_end = 2 = b
	window_start =  1 = a 
	char_index_map = {a:1, b:2}
	max_len = 2
	---------------

	window_end = 3 = c
	window_start =  1 = a 
	char_index_map = {a:1, b:2, c:3}
	max_length = 3-1+1 = 3
	---------------

	window_end = 4 = c
	window_start =  4 = c 

	char_index_map = {a:1, b:2, c:3}
	---------------	
	
=end
# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
	window_start = 0
	max_length = 0
	char_index_map = {}
	n = s.length

	for window_end in 0..n-1
		
		right_char = s[window_end]

		#if char index map include right char means , we need to shrink window. 
		#we need to change wondow_start position. 
		if char_index_map.include? right_char
			puts "		before window_start : #{window_start}"
			puts "		before window_end : #{window_end}"
			window_start = [window_start, char_index_map[right_char] + 1].max
			puts "		after window_start : #{window_start}"
			puts "		after window_end : #{window_end}"
		end

		char_index_map[right_char] = window_end
		puts "char_index_map : #{char_index_map}"
		max_length = [max_length, window_end - window_start + 1].max
		puts "max_length : #{max_length}"
		puts "-----------------------------------"
	end

	return max_length

end


s = "aabccbb"
s = "abbbb"
s = "abccde"
s = "dvdf"
s = "abba"
res = length_of_longest_substring(s)
puts "res : #{res}"

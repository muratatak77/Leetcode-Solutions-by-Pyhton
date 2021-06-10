=begin

we can apply siliding window approach for this question.

		- hash map to remember the frequences all of the chars in the pattern

		- iterate through the string, adding one char at a time in the sliding window

		- if the char matches a char in the freq hash map , decrement in the freq map.
				if the char becomes zero , we got a complete match , increment matched count.

	 - if number of chars matched is equal the number of distint chars in the pattern , we have gotten our required permutation
	 			we can return True

	 - if the window size grater than length of the pattern, shrink the window to make it equal to the pattern size.
	 	At the same time , if the char going out was part of the pattern , put it back in the freq map
		
=end

# @param {String} s1
# @param {String} s2
# @return {Boolean}
def check_inclusion(s1, s2)
	
	pattern = s1

	freq_map = {}

	window_start = 0
	matched = 0

	#fill up the freq map
	pattern.each_char  do |ch|
		if !freq_map.include? ch
			freq_map[ch] = 0
		end
		freq_map[ch] += 1
	end


	#iterate in the string 
	for window_end in (0..s2.length-1)
		#check the right side char
		right_char = s2[window_end]
		if freq_map.include? right_char
			#if we match we can decrement current char in freq map 
			freq_map[right_char] -= 1
			#if we have 0, means we matched all current char in the freq map
			if freq_map[right_char] == 0
				matched += 1
			end
		end

		#check the exact match with the all freq chars map
		if matched == freq_map.length
			return true
		end

		#if grater than or window length of pattern string we need to shrink the window
		if window_end >= pattern.length - 1
			left_char = s2[window_start]
			window_start += 1
			#if this remain char include the freq map we need back + 1
			if freq_map.include? left_char
				if freq_map[left_char] == 0
					matched -= 1
				end
				freq_map[left_char] += 1
			end
		end
	end

	return false

end

s1 = "oidbcaf" 
pattern="abc"

pattern =  "ab"
s1= "eidbaooo"

s1 = "ab"
s2 = "eidboaoo"

s1 = "abc"
s2 = "ccccbbbbaaaa"

res = check_inclusion(s1, s2)
puts("res : #{res}")


=begin
Time Complexity #
The above algorithm’s time complexity will be O(N + M), where ‘N’ and ‘M’ are the number of characters in the input string and the pattern, respectively.

Space Complexity #
The algorithm’s space complexity is O(M) since, in the worst case, the whole pattern can have distinct characters that will go into the HashMap.
=end
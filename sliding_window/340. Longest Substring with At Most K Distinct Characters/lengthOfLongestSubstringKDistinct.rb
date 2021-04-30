def lengthOfLongestSubstringKDistinct(s,k)
	max_lenght = 0
	window_start = 0
	freq_chars = {}

	for window_end in 0..(s.length)-1
		right_char = s[window_end]
		if freq_chars.include? right_char:
			freq_chars[right_char] = 0
		end
		freq_chars[right_char] += 1

		#we need to shrink until len(freq_chars) grater than K
		while freq_chars.length > k do
			left_char = s[window_start]
			freq_chars[left_char] -= 1
			if freq_chars[left_char] == 0
				freq_chars.delete(left_char)
			end
			window_start += 1
		end
		max_lenght = [max_lenght, window_end - window_start + 1].max
	end
	max_lenght
end


s = "eceba"
k = 2
res = lengthOfLongestSubstringKDistinct(s, k)
puts("res : #{res}")

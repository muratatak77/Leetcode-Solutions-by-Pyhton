def length_of_longest_substring(str1, k)
  
  window_start = 0
  max_length  = 0
  max_letter_count = 0
  freq_map = {}

  for window_end in (0..str1.length-1)

    #we need to fill up freq map to find max_letter_count
    right_char = str1[window_end]
    unless freq_map.include? right_char
      freq_map[right_char] = 0
    end
    freq_map[right_char] += 1

    max_letter_count = [max_letter_count, freq_map[right_char]].max

    #we need to check whether if we need shrink the window or not
    if (window_end - window_start + 1 - max_letter_count) > k
      left_char = str1[window_start]
      freq_map[left_char] -= 1
      window_start += 1
    end

    max_length = [max_length, window_end-window_start + 1].max
  end

  return max_length

end


res = length_of_longest_substring("aabccbb", 2)
puts("res : #{res}")

# print(length_of_longest_substring("abbcb", 1))
# print(length_of_longest_substring("abccde", 1))
# print(length_of_longest_substring("AABABBA", 1))


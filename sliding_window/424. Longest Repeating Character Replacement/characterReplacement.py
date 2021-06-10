'''
https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91271/Java-12-lines-O(n)-sliding-window-solution-with-explanation

In case anyone is confused by this solution, here's another way of explaining it:

end-start+1 = size of the current window
maxCount = largest count of a single, unique character in the current window

The main equation is: end-start+1-maxCount

When end-start+1-maxCount == 0, then then the window is filled with only one character

When end-start+1-maxCount > 0, then we have characters in the window that are NOT the character that occurs the most. 

end-start+1-maxCount is equal to exactly the # of characters that are NOT the character that occurs the most in that window. 

Example: For a window "xxxyz", end-start+1-maxCount would equal 2. (maxCount is 3 and there are 2 characters here, "y" and "z" that are not "x" in the window.)

We are allowed to have at most k replacements in the window, so when end-start+1-maxCount > k, then there are more characters in the window than we can replace, 
and we need to shrink the window.

If we have window with "xxxy" and k = 1, that's fine because end-start+1-maxCount = 1, which is not > k. maxLength gets updated to 4.

But if we then find a "z" after, like "xxxyz", then we need to shrink the window because now end-start+1-maxCount = 2, and 2 > 1. The window becomes "xxyz".

maxCount may be invalid at some points, but this doesn't matter, because it was valid earlier in the string, 
and all that matters is finding the max window that occurred anywhere in the string. 
Additionally, it will expand if and only if enough repeating characters appear in the window to make it expand. So whenever it expands, it's a valid expansion.

'''

def length_of_longest_substring(str1, k):
  window_start, max_length, max_repeat_letter_count = 0, 0, 0
  frequency_map = {}

  # Try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char not in frequency_map:
      frequency_map[right_char] = 0
    frequency_map[right_char] += 1

    print("frequency_map : ", frequency_map)

    max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])
    print(" max_repeat_letter_count : ", max_repeat_letter_count)

    # Current window size is from window_start to window_end, overall we have a letter which is
    # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
    # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
    # if the remaining letters are more than 'k', it is the time to shrink the window as we
    # are not allowed to replace more than 'k' letters
    print("   window_end - window_start + 1 - max_repeat_letter_count : ", window_end - window_start + 1 - max_repeat_letter_count)
    if (window_end - window_start + 1 - max_repeat_letter_count) > k:
      print("     Starting window shrink")
      left_char = str1[window_start]
      frequency_map[left_char] -= 1
      window_start += 1
      print("     window_start : ", window_start)

    max_length = max(max_length, window_end - window_start + 1)
    print("     max_length : ", max_length)
    print("     current window : ", str1[window_start:window_end+1])
    print("-------------------------------------------------")
  return max_length


def main():
  print(length_of_longest_substring("aabccbb", 2))
  # print(length_of_longest_substring("abbcb", 1))
  # print(length_of_longest_substring("abccde", 1))
  # print(length_of_longest_substring("AABABBA", 1))

main()

'''
Time Complexity #
The above algorithm’s time complexity will be O(N), where ‘N’ is the number of letters in the input string.

Space Complexity #
As we expect only the lower case letters in the input string, 
we can conclude that the space complexity will be O(26) to store each letter’s frequency in the HashMap, 
which is asymptotically equal to O(1).
'''
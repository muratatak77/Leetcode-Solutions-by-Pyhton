class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:

		pattern = s1
		s1 = s2

		window_start = 0
		matched = 0
		freq_map = {}

		for chr in pattern:
			if chr not in freq_map:
				freq_map[chr] = 0
			freq_map[chr] += 1


		for window_end in range(len(s1)):

			right_char = s1[window_end]
			if right_char in freq_map:
				freq_map[right_char] -= 1
				if freq_map[right_char] == 0:
					matched += 1

			if matched == len(freq_map):
				return True

			#shrink the window
			if window_end >= len(pattern)-1:
				left_char = s1[window_start]
				window_start += 1
				if left_char in freq_map:
					if freq_map[left_char] == 0:
						matched -= 1
					freq_map[left_char] += 1

		return False


s1 = "ab" 
s2 = "eidbaooo"

s1 = "ab"
s2 = "eidboaoo"

s1 = "abc"
s2 = "ccccbbbbaaaa"

res = Solution().checkInclusion(s1, s2)
print("res : ", res)

			


from typing import List
class Solution:
	def compress(self, chars: List[str]) -> int:

		anchor = write = 0
		for read, c in enumerate(chars):
			print("read : ", read, " - c : ", c)
			print("anchor : ", anchor , " - write : ", write)

			if read + 1 == len(chars) or chars[read + 1] != c:
				chars[write] = chars[anchor]
				print("		set matxh chars[write] == chars[anchor]. chars : ", chars)
				write += 1
				print("		write increment :", write)

				if read > anchor:
					print("			read > anchor == ", read , " > ", anchor)
					for digit in str(read - anchor + 1):
						chars[write] = digit
						print("				chars[write] = digit", chars[write], " = ", digit, " /  chars : ", chars)

						write += 1
						print("				write increment :", write)
						print("----------------------------")

				anchor = read + 1
				print("anchor : ", anchor)
			print("========================================")

		return write


chars = ["a","a","b","b","c","c","c"]
# chars = ["a"] 
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","a","b","b","a","a"]
res = Solution().compress(chars)
print("res : ", res)
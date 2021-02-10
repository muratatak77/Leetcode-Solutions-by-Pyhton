class Solution:
	def calculate(self, s: str) -> int:
		inner, outer, result, opt = 0, 0, 0, '+'

		for c in s + '+':
			print(" c : ", c)
			print("	inner = ", inner, " /// opt : ", opt, " /// result = ", result, "/// outer = ", outer)
			if c == ' ': continue
			if c.isdigit():
				inner = 10 * inner + int(c)
				print("	inner : ", inner)
				continue
			if opt == '+':
				result += outer
				outer = inner
				print("	opt == '+' /// result = ", result, " // outher  = ", outer)
			elif opt == '-':
				result += outer
				outer = -inner
				print("	opt == '-' /// result = ", result, " // outher  = ", outer)
			elif opt == '*':
				outer = outer * inner
				print("	opt == '*' /// result = ", result, " // outher  = ", outer)
			elif opt == '/':
				outer = int(outer / inner)
				print("	opt == '/' /// result = ", result, " // outher  = ", outer)
			inner, opt = 0, c

			print("=====================================================")

		print("END inner = ", inner, " // outer  = ", outer, " /// result = ", result)
		return result + outer


s = "3+2*2"
res = Solution().calculate(s)
print("res  :", res)
'''
	we can keep some params to keep valuations.
	
	outer = everytime end evulation keeping. Works just in multiple and division evulations.
	inner = before outer evulation keeping. Works just in multiple and division evulations.
	
	result = keep just addition and extraction operations.
	opt = our before operations not current opt.
	our default operation will be '+'. 
	Everytime we will keep in iterator doing previous evulation.


	like : 30*2+2
	inner = 3
	inner = 30 (inner * 10 + int(char))


	Everytime computing will do between outer and inner params


'''
class Solution:
	def calculate(self, s: str) -> int:
		outer, inner, result, opt = 0,0,0,'+'

		# we need s+ '+' because we can care about every time previous operation evaluation.
		# we need to evualete last computing
		for c in s + '+':
			if c == ' ':
				continue

			if c.isdigit():
				#we need to compute inner * 10 + int()
				#because if second char is digit is a number we need to compute on decimal system
				#if we have 302 in first 3 chars we need to get as a number 302.
				#and inner params will be 0 each end of iterate
				inner = inner * 10 + int(c)
				continue

			if opt == "+":
				#we need addition operate into the result params. and outer will be inner
				#everytime computing will do between outer and inner params
				result += outer
				outer = inner

			elif opt == "-":
				result += outer
				outer = -inner

			elif opt == "*":
				outer = outer * inner

			elif opt == "/":
				outer = int(outer/inner)

			inner, opt = 0, c

		return result + outer
		

s = "3+2*2"
s = " 3+5 / 2 "
s = " 3/2 "

res = Solution().calculate(s)
print("res  :", res)

'''
	O(T) = O(N)
	S(T) = O(1)

'''
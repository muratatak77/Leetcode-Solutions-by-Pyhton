
# @param {String} s
# @return {Integer}
# we can start pushing index 
# 
# ( ) 
# stack = [-1 ]
# 
def longestValidParentheses(s):
	max_ans = 0
	stack = []
	stack.append(-1)

	for i in range(len(s)):
		if s[i] == "(":
			stack.append(i)
		else:
			stack.pop()
			if stack:
				max_ans = max(max_ans, i - stack[-1])
			else:
				stack.append(i)

	return max_ans


s = "(()"
res = longestValidParentheses(s)
print("res : ", res)





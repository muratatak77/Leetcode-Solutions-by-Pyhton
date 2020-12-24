class Solution(object):
	
	def isValid(s):
		
		stack = []

		clossing_mapping = {")":"(","]":"[","}":"{"}

		#we need iterator s chars 
		for char in s:

			if char in clossing_mapping:
				top_element = "#"
				if stack:
					top_element = stack.pop()
				
				if clossing_mapping[char] != top_element:
					return False

			else:
				stack.append(char)		

		#if stack will be empty : valid expression
		#if stack will not be empty : invalid expression
		return not stack




ss = "([)]"

ss = "{([])}"

res = Solution.isValid(ss)
print(res)


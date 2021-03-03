'''
	question : Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

		An input string is valid if:

		Open brackets must be closed by the same type of brackets.
		Open brackets must be closed in the correct order.
	solution : 
		we can use stack data structure for this question :

		we can keep a mapping set for chars. like : 

		mapping = {
			']':'[' , ")":"(", "}":"{"
		}

		S = "()[]{}"

		stack (,

		when we accross the closed char like ")" we can pop from stack and we can check in the mapping usable char.
			if no we can return False


		finally we can return True if stack is empty , or not we can return False

'''
class Solution:
	def isValid(self, s: str) -> bool:
		

		stack = []

		mapping = {']':'[',')':'(','}':'{'}

		for char in s:

			#if we accross closer char
			if char in mapping:
				
				if stack: 		
					top_element = stack.pop()
				else:
					top_element = "#"

				if mapping[char] != top_element:
					return False
			else:
				stack.append(char)

		return not stack

s = "()"
s = "([)]"
res = Solution().isValid(s)
print("res : ",res)


'''
	T(N) = O(N) . we iterate len s
	S(N) = O(N) .  we have a stack.worst case : "(((((((((" we push all bracktes onto the stack 
'''
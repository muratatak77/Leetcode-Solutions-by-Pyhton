'''
	generally we can use a stack in parantheses questions
	we can use a stack to follow balance of paranthesses situation

		like = 
		s = "l e e ( t ( c ) o ) d e )"

		step 1

		when we encounter '(' we can add to the stack index of char.
		when we encounter ')' we can pop from to the stack index of char.
		in iterate process, when we get empty stack and we encounter ')' this char, means there is a unapporepiate parantheses.
			we can keep a set to keep unsuiateble index.

		step 2

		after first iterate we will get stack and set :
		stack = will be empty
		set = < 12 > because just we have final parantheses wasn't appropiate

		we can start a while iterate and we can pop from stack and we can add to set index.
	
		step 3
		we can check all chars and set to build  anew string.

		for i,c in enumarate(s):
			if i not in set:
				new_string.append(c)

		new string will be this way : [l,e,e,(,t,(,c,),o,),d,e]

		and return  "".join(new_string)


'''
class Solution:
	def minRemoveToMakeValid(self, s: str) -> str:
	
		stack = []
		set_remove_idx = set()

		#step 1
		#add or pop the stack if we have unsitable char index add to the set 
		for i,char in enumerate(s):
			if char not in "()":
				continue

			if char == "(":
				stack.append(i)

			elif not stack:
				set_remove_idx.add(i)

			else:
				stack.pop()

		print("stack : ", stack)

		#step2 
		#we will empty stack if still we have index items. Means this items is not appropriate for rules 
		while stack:
			set_remove_idx.add(stack.pop())

		#step3
		#we will check to generate new string
		new_string = []
		for i,c in enumerate(s):
			if i not in set_remove_idx:
				new_string.append(c)

		return "".join(new_string)



s = "lee(t(c)o)de)"
s = "))(("
res = Solution().minRemoveToMakeValid(s)
print("res : ", res)

'''
	T(N) = O(N) - We have 3 loops each loop works O(N) also last row =>  "".join(new_string)
	S(N) = O(N) - 2 array and a set
'''





'''
	we can use 2 stacks in this question.
	
	First stack keeps numbers digits , another keeps string letters.

	we can append just numbers when we reach '[' to the number_stack. 
	we can append just letter when we reach '[' to the str_stack

	and we can keep current string situation in the cur param and num param to keep just digit numbers. 

	like 12[a2[c]]

	we need to convert '12' to the integer 12.
	when we iteate along the string we can add num params 1 and 2 . and we can convert '12' to the integer  : 12.

	and we can append number_stack = [12] 
	than we can keep curr = 'a' and num = 2

	again we accross '[' char.  we can append a to the string stack. we can append 2 to the number stack

	number_stack = [12, 2]
	str_stack = [a]

	when we accross ']' we need pop from both stacks.
		
		k = number_stack.pop()
		k = 2

		cur = c
		repaated = cur * k = cc

		last_curr = stack_str.pop() # a

		cur = repaated + last_curr # acc
	
	when we accross ']' we need pop from both stacks.

		k = number_stack.pop()
		k = 12

		cur = acc
		repaated = cur * k = accaccaccaccaccaccaccaccaccaccacc

		last_curr = stack_str.pop() # 

		cur = repaated + last_curr # accaccaccaccaccaccaccaccaccaccacc

	we can return cur


'''
class Solution:
    def decodeString(self, s: str) -> str:

    	number_stack = []
    	str_stack = []
    	num = ""
    	cur = ""
    	i = 0
    	while i < len(s):
    		if s[i].isdigit():
    			num += s[i]

    		elif s[i] == '[':
    			number_stack.append(int(num))
    			print("number_stack append: ", number_stack)
    			num = ""
    			str_stack.append(cur)
    			print("str_stack append: ", str_stack)

    			cur = ""

    		elif s[i] == "]":

    			k = number_stack.pop()
    			print("number_stack pop: ", number_stack)
    			repated = k * cur
    			last_cur = str_stack.pop()
    			print("str_stack pop: ", str_stack)

    			cur = last_cur + repated

    		#last case for letters
    		else:
    			cur += s[i]
    			print("added cur : ", cur)
    		i+=1

    		print("cur  :", cur)
    		print("====================")

    	return cur

# s = '12[a2[c]]'
s = "3[a2[c]]"
# s = "2[abc]3[cd]ef"
res = Solution().decodeString(s)
print("res:", res)
'''
	T(N) = O(N) N is length of string
	S(N) = O(N + M) N = string stack. Letter max (a..z) , M = number stack (0..9)

'''

''''

s = "3[a2[c]]"


output


cur  : 
====================
number_stack append:  [3]
str_stack append:  ['']
cur  : 
====================
added cur :  a
cur  : a
====================
cur  : a
====================
number_stack append:  [3, 2]
str_stack append:  ['', 'a']
cur  : 
====================
added cur :  c
cur  : c
====================
number_stack pop:  [3]
str_stack pop:  ['']
cur  : acc
====================
number_stack pop:  []
str_stack pop:  []
cur  : accaccacc
====================
res: accaccacc
[Finished in 0.0s]
'''


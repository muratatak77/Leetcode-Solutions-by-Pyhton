'''
actuall this question is fill in the blank question.

we can start to fill first left parantheses 
 after we can add left or right doesnt matter. 
 and we need numleft and numright pointers.
 if numleft pointers and numright pointers equal the 0 
	we can add to the global result 
	
	we have some contraints. 
	like numleft  < 0 or numrught < 0 or numleft > numright 

if n = 2 wil be 4 blanks  _ _ _ _
	
	result will be : 

	(())
	()()
	n = 2
				_ _ _ _ 

				  2-2

			1-2 (   ) 0-1

		0-2 (		    ) 0 - 0 

leaf node :  (())


We can do this by keeping track of the number of opening and closing brackets we have placed so far.

'''

def overall(n):
	result = []

	def helper(numleft, numright, slate):
		print("numleft : ", numleft , " - numright : ", numright, " - slate : ", slate)

		#backtracing case
		if numleft > numright or numleft < 0 or numright < 0:
			return

		#base case , leaf node
		if numleft == 0 and numright == 0:
			result.append("".join(slate[:]))
			print("result append : ", result)
			return
		
		#recursice case
		#include '('
		slate.append('(')
		helper(numleft-1, numright, slate)
		print("     left pop ------ ")
		slate.pop()

		#include ')'
		slate.append(')')
		helper(numleft, numright-1, slate)
		print("     right pop ------ ")
		slate.pop()

	helper(n,n,[])
	return result

n = 3
res = overall(n)
print("res : ", res)


'''
	time complexitiy : 
		height of tree : 2n
			each node has 2 choices.
				T(n) = O(2 ^ 2n)
		and we have copy of slate just for leaf nodes.
			lenght ogf the slate : 2n
				T(n) = O(2^2n) x O(2n) = O(n.4^n)


	Space complexity :
		Explicit space :     
			Same as before = O(n.4^n)
		implicit Space : 
			O(n)

'''



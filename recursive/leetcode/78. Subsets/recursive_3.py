'''
	We will apply sub definition (s,i) and partial solution(slate) recursive approach
	we can suppose like filling the empty spaces
	we can call recursive call exclude way and include way. 
	in exclude way we can not add any item to the partial solution (slate)
	in include way we can add s[i] and we can call recursive call and after return we need to pop from partial solution.

							- - -

			   ()   							(1)

	   	 ()			 (2)        		(1)      	    (1,2)

	()	  (3)    (2)     (2,3)     (1)	   (1,3)	(1,2)	(1,2,3)


'''

def overall(nums):

	result = []

	def helper(s,i, slate):
		#base case , leaf workers
		if i == len(s):
			result.append(slate[:]) #copy/clone of slate we need > O(n)
			return
		else:
			#exclude case
			helper(s,i+1, slate)

			#include case
			slate.append(s[i])
			helper(s,i+1,slate)
			slate.pop()
			
		
	helper(nums,0,[])
	return result


nums = [1,2,3]
res = overall(nums)
print("res : ", res)


'''
T(N) = O(2^N.N)  
S(N) = O(2^N.N)
'''
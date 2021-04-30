'''
n = [1,2,3,4]
k = 2

we can apply backtracink approach for all potential candidates.
we can apply exlude and include sub definition(n,i) and partial solution(slate)

		     			1,2,3,4

			     			_ _ 

	 						_ _

 			- - 				
								
	- -					3     			  2	  (2,3)

- - 		4       3		(3,4)      2          (2,4)


		  1           2              3   

    (e)1, (i)2    (e)1, (i)3        1,4    2,3  2,4     3,4


      			_ _ _ _ 
      		_ 
      	 _
      _

   []   [4]


'''

def overall(n,k):
	result = []

	def helper(n, i, slate):
		
		#backtracking case
		if len(slate) == k:
			result.append(slate[:]) 
			return 

		#base case
		if i == n+1:
			return 

		#exclude case
		helper(n,i+1,slate)


		#include case
		slate.append(i)
		helper(n,i+1,slate)
		slate.pop()

	helper(n,1,[])
	return result
	

n = 4
k = 2
print(overall(n,k))


'''
	T(N) = O(kCkn)   comb formula : N!/(N-k)!.k!
	S(N) = O(Ckn)

'''

'''
n = [1,2,3,4]
k = 2

we can apply backtracink approach for all potential candidates.
we can apply exlude and include sub definition(n,i) and partial solution(slate)

		     	1,2,3,4
		  1           2          3   
    (e)1, (i)2  (e)1, (i)3  1,4    2,3  2,4     3,4


      			_ _ _ _ 
      		_ 
      	 _
      _

   []   [4]


'''

def overall(n,k):
	result = []

	def helper(n, i=1, slate=[]):
		
		#base canse, leaf workers
		if len(slate) == k:
			print("slate append : ", slate[:])
			result.append(slate[:])
			return 

		#we dont need go ahead if reach n+1 
		if i == n+1:
			print(" 			  i == n + 1 ")
			return

		#recursive case, internal node
		#exlude side
		print("       helper exlude call :  i+1 : ", i+1, " - slate: ", slate)
		helper(n,i+1,slate)

		#include case
		slate.append(i)
		print("     		helper include call :  i+1 : ", i+1, " - slate: ", slate)
		helper(n,i+1, slate)
		slate.pop()
		print("					slate pop i: ", i, " - slate : ", slate)
		print("=============================================================================================")

	helper(n)
	return result
	

n = 4
k = 2
print(overall(n,k))


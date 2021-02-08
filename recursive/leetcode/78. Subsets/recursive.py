def overall(s):
	result = []
	#I can apply sub definition problem and partial solution appoarch for this problem.
	
	def helper(s,i,slate):
		print("Call helper :  i : ", i , " slate : ", slate )
		#base case : leaf workers
		if i == len(s):
			result.append(slate[:]) #copy / clone of slate
			return
		else:
			#recursive case:  internal node
			#exclude side. we don't append any char
			helper(s,i+1, slate) 
			
			#include side
			#we need to fill blank next s[i] element
			slate.append(s[i])
			helper(s,i+1,slate)
			slate.pop()

			
	helper(s,0,[])
	return result

nums = [1,2,3]
print(overall(nums))

#space comp. 
# input : O(n)
# Aux space : O(n) 
# Output : result : O(2^n x n)

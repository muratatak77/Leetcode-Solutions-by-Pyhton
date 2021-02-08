'''
	combitonarial enumeration problem(permutation /combination)
	This problem is filling blank problem
	
	we can apply 
	time complexity will be exponential time compl.
	
	We process left to right and as a lazy manager, only take responsibility for filling in the first blank. 
	lazy manager - delegates the rest of the work to subordinates.
	
	 like  :

							_ _ _ _  > lazy manager 
						
						a _ _ _    A _ _ _     > sub ordinates - internal nodes (recursive case)
					
					a1 _ _				A1 _ _
				
				a1b _	 					A1b _
									
			a1b2	a1B2				A1b2		A1B2 		> leaf workers (base cases)




	 we need a global result
	 and helper method includes recursive and base cases 

'''

class Solution(object):
	def letterCasePermutation(self, S):

		result = []
		def helper(S, i, slate):
			
			#base case : leaf workers
			if i == len(S):
				result.append(slate) #master copy from original string. immutable version. We cant change string and we need to add
				return 
			else:
				#recursive case : internal nodes
				if S[i].isdigit():
					helper(S, i+1, slate+s[i])
				else:
					helper(S, i+1, slate+s[i].lower()) # we create original string immutable version. we create new string and we can't change original string
					helper(S, i+1, slate+s[i].upper())

		
		helper(S, 0, "")
		return result


s = "a1b2"
res = Solution().letterCasePermutation(s)
print("res : ", res)



'''
space complexity : 
	input : n
	aux space :  immutable version  O(n^2) - implicit stack space - immutable version. 
	output : O(2^n.N)  2^n = every alpha char has multiple options. 2^n  = 2^2 = 4 / N : length of string
time :  O(2^n.N)



'''

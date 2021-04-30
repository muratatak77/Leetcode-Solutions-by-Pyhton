# https://leetcode.com/problems/permutations/solution/
# https://www.youtube.com/watch?v=KukNnoN-SoY&t=583s&ab_channel=TimeComplexityInfinity
'''
	we can do it recursive function .
									first = 0
									_ _ _            
		
		i = 0						 						i = 1 									i = 2
															first = 0 
															swap(1,0) > 2,1,3
		1 _ _ 												slate = 2 


		first = 1 											first = 1
	

	
	i = 1 				i = 2						i = 1 				i = 2
   swap(1,1) > 1,2,3	swap(1,2) > 1,3,2			swap(1,1) 			swap(1,2) = 2,3,1 
	1 2 _     			1 3_						2 1 _				2,3 _ 
	slate = [1,2]		slate = [1,3]				slate = [2,1]		slate = [2,3]


	first= 2			first = 2 					first= 2			first = 2
	i = 2	 			i = 2						i = 2				i = 2
	1 2 3				1 3 2						slate = [2,1,3]		slate = [2,3,1]


T(N) = O(N!.N)  Factoriel and foor loop 
S(N) = O(N!.N)

'''
def overall(s):
	result = []

	def helper(first):
		#base case, leaf node
		if first == len(s):
			result.append(s[:])
		else:
			for i in range(first, len(s)):
				nums[first],nums[i] = nums[i], nums[first]
				helper(first+1)
				nums[first],nums[i] = nums[i], nums[first]

	helper(0)
	return result


nums = [1,2,3]
print(overall(nums))
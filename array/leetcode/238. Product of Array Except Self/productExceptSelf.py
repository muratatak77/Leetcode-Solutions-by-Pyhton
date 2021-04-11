'''
	First we can count left to the right side. 
		When we count we need an extra array keeping multiply result step by step left to right.
		Our initial value will be 1. 

		left_arr = []
	

	Second we can count right to the left side. 
		When we count we need an extra array keeping multiply result step by step right to left
		Our initial value will be 1. 
		right_arr = []

	like = 
	nums = [1,2,3,4]
	
	let's think we won't count 2  so means nums[1] is missing
	left arr will be finally : 
		initial :
		left_arr[0] = 1

		left_arr[1] = 1*1 =  1
		left_arr = [1,1]
	
		initial :
		right_arr[3] = 1
		right_arr[2] = 1*4 = 4
		right_arr[1] = 4*3 = 12


		final left array multiplty result will be = 1
		final right array multiplty result will be = 12
		if we skip item 2 (nums[1]) result final will be = 12
	


'''

from typing import List
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		
		# The length of the input array 
		length = len(nums)
		
		# The left and right arrays as described in the algorithm
		L, R, answer = [0]*length, [0]*length, [0]*length
		
		# L[i] contains the product of all the elements to the left
		# Note: for the element at index '0', there are no elements to the left,
		# so the L[0] would be 1
		L[0] = 1
		for i in range(1, length):
			
			# L[i - 1] already contains the product of elements to the left of 'i - 1'
			# Simply multiplying it with nums[i - 1] would give the product of all 
			# elements to the left of index 'i'
			L[i] = nums[i - 1] * L[i - 1]
			print("steps array L : ", L)



		print("Final array L : ", L)
		
		# R[i] contains the product of all the elements to the right
		# Note: for the element at index 'length - 1', there are no elements to the right,
		# so the R[length - 1] would be 1
		R[length - 1] = 1
		for i in range(length-2,-1,-1):
			print("i >>> ", i)
			R[i] = nums[i+1]*R[i+1]
			print("		steps array R : ", R)

		
		# Constructing the answer array
		for i in range(length):
			# For the first element, R[i] would be product except self
			# For the last element of the array, product except self would be L[i]
			# Else, multiple product of all elements to the left and to the right
			answer[i] = L[i] * R[i]
		
		return answer


nums = [1,2,3,4]
res = Solution().productExceptSelf(nums)
print("res : ", res)
'''
	T(N) = O(N) N represent element in the nums array. Visit all element just 1 time seperate 3 times.
			We use one itrerator to construct the array L, and one constract the array R and one last to construct the answer array using L  and R.

	S(N) = O(N) 
'''
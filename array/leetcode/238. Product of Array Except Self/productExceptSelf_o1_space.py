from typing import List
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		answer = [0] * n

		#left to the right computation. 
		#we start index 1, we can not compute last item in the nums array
		answer[0] = 1
		for i in range(1,n):
			answer[i] = nums[i-1]*answer[i-1]

		print("answer : ", answer)
			
		#we can walk trough right to the left
		#we will set a right product value keeping current nums item 
		right_product = 1
		for i in range(n-1, -1,-1):
			print(" i :" , i)
			answer[i] = answer[i]*right_product
			right_product *= nums[i] 
			print(" 	answer : ", answer, " - right_product : ", right_product)

		return answer


nums = [1,2,3,4]
res = Solution().productExceptSelf(nums)
print("res : ", res)


'''
	T(N) = O(N) N is the length of the nums array item. We just constract 1 array that it is 'answer'
	S(N) = O(1) because we don't use any computations using by the extra space. The 'answer' array we are using just for result.
	
'''
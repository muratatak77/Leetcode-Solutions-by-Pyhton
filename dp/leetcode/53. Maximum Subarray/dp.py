'''
	we can apply sum and max operations. 
		first we need current sum from the  max(nums[i], curr_sum+nums[i])
		   this operations will be given what is the max current sum.

		 and second we can take max sum by using the max(max_sum, curr_sum)

'''

class Solution:
	def maxSubArray(self, nums):
		n = len(nums)
		curr_sum = max_sum = nums[0]

		for i in range(1, n):
			print("i :", i)
			curr_sum = max(nums[i], curr_sum + nums[i])
			print("curr_sum : ", curr_sum)
			max_sum = max(max_sum, curr_sum)
			print("max_sum : ", max_sum)
			print("----------")
			
		return max_sum



nums = [-2,1,-3,-1,1,2,11,1,-5,4,11]

res = Solution().maxSubArray(nums)
print("res :", res)

'''
	T(N) = O(N)
	S(N) = O(1)
'''
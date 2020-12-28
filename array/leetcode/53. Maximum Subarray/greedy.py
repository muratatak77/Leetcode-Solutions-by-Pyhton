'''
	Q : 
	Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

	Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
------------------------------------------------
	Solution : 
		we can apply a greedy approach.
		we can sum items using by an iterate.
		first we can get max by sum locally. 
		Second we can sum global keeping max value.

		lnums = [-2,1,-3,4,-1,2,1,-5,4]

		local_max = max(nums[i],local_max+mums[i])

		local_max = [-2, 1, -2,4,3, ....]
		global_max = [-2,1,2,4,4, .... ]


'''

def max_sub_array(nums):

	if not nums:
		return 0

	if len(nums) == 1:
		return nums[0]

	local_max = nums[0]
	global_max = nums[0]

	for i in range(1,len(nums)):
		local_max = max(nums[i], local_max+nums[i])
		global_max = max(global_max, local_max)

	return global_max


nums = [-2,1,-3,4,-1,2,1,-5,4]
res = max_sub_array(nums)
print("RES : ", res)


'''
	T(N) = O(N) we have just one loop trough the nums array
	S(N) = O(1) No extra space
	
'''
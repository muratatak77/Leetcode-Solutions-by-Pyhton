# https://leetcode.com/problems/permutations/solution/

def overall(nums):
	result = []
	n = len(nums)

	def helper(first=0):
		if first == n:
			result.append(nums[:])
		else:
			for i in range(first,n):
				nums[first], nums[i] = nums[i], nums[first]
				helper(first+1)
				nums[first], nums[i] = nums[i], nums[first]
	helper()
	return result	


nums = [1,2,3]
print(overall(nums))
class Solution():
	
	def threeSum(self, nums):
		nums.sort()
		print("nums : ", nums)
		res = []
		for i in range(len(nums)):
			if nums[i] > 0:
				break
			if i == 0 or nums[i-1] != nums[i]:
				print("i :" , i)
				self.twoSum(nums, i, res)
		return res


	def twoSum(self, nums, i, res):
		lo = i + 1
		hi = len(nums)-1

		while lo < hi:
			sum = nums[i] + nums[lo] + nums[hi]
			print("sum : " , sum)
			if sum < 0:
				lo += 1
			elif sum > 0:
				hi -= 1
			else:
				res.append([nums[i],nums[lo],nums[hi]])
				lo += 1
				hi -= 1
				while lo<hi and nums[lo] == nums[lo-1]:
					lo += 1
		return res

nums = [-1, 0, 1, 2, -1, -4]
res = Solution().threeSum(nums)
print(res)

					

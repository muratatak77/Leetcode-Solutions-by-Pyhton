class LargerNumKey(str):
    def __lt__(x,y):
        return x+y > y+x


class Solution:
	def largestNumber(self, nums):

		if not 1 <= len(nums) <= 100:
			return ""

		for i in range(len(nums)):
			if nums[i] < 0:
				return ""
			nums[i] = str(nums[i])
				
		largest_num = sorted(nums, key=LargerNumKey)

		if largest_num[0] == '0':
			return 0

		return ''.join(largest_num)



nums = [3,30,34,5,9]
nums = [100,2,20,56,32,9]
res = Solution().largestNumber(nums)
print("res : ", res)
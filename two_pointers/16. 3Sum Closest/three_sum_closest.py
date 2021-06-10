# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
#
#  we have an array and we need to add a triplets items.
# we can pick first i item and we can do an substrack operation selecting by 2 pointers.
# Thats why we can apply 3 pointer approach.
# 
# 

import math

class Solution(object):
		def threeSumClosest(self, nums, target):

			n = len(nums)

			if n == 0:
				return [] 

			smallest_diff = math.inf

			nums.sort()
			target_diff = 0

			for i in range(n):

				left = i+1
				right = n-1

				while (left < right):
					target_diff = target - nums[i] - nums[left] - nums[right]

					#eaxct match
					if target_diff == 0:
						 return target - target_diff

					#negative or positive any case
					check_1 = abs(target_diff) < abs(smallest_diff)
					#be sure negative case works correctly
					check_2 = abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff

					if check_1 or check_2:
						smallest_diff = target_diff

					#we need to go to the left if our diff grater than 0. because we can contunie to scan other items.
					if target_diff > 0:
						left += 1
					else:
						right -= 1

			return target - smallest_diff


# nums = [-3, -1, 1, 2]
# nums = [-2, 0, 1, 2]
nums = [1, 0, 1, 1]
# target=1
# target=2

target = 100
res = Solution().threeSumClosest(nums, target)
print("res : ", res)


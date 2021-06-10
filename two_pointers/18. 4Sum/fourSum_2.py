'''
case = [1,0,-1,0,-2,2]
sort = [1,0,-1,0,-2,2]

'''
class Solution(object):
		def fourSum(self, nums, target):

			def start_process(nums, target):
				result = []
				for i in range(0, len(nums)-3):
					# skip same element to avoid duplicate quadruplets
					if i > 0 and nums[i] == nums[i - 1]:
						continue
					for j in range(i + 1, len(nums)-2):

						# skip same element to avoid duplicate quadruplets
						if j > i + 1 and nums[j] == nums[j - 1]:
							# print("   continue j > i + 1 and nums[j] == nums[j - 1]")
							continue
						search_pairs(nums, target, i, j, result)
				return result

			def search_pairs(nums, target, first,second, result):
				left = second+1
				right = len(nums)-1

				while left < right:
					_sum = nums[first] + nums[second] + nums[left] + nums[right]
					if _sum == target:
						result.append([nums[first], nums[second], nums[left], nums[right] ])
						left += 1
						right -= 1
						while left < right and nums[left] == nums[left-1]:
							left += 1

						while left < right and nums[right] == nums[right+1]:
							right -= 1
					elif _sum < target:
						left += 1
					else:
						right -=1

				return result

			nums.sort()
			return start_process(nums, target)


# def main():
#   print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
#   # print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))

# main()
nums = [1,0,-1,0,-2,2]
target = 0


nums = [-1,0,-5,-2,-2,-4,0,1,-2]
target  = -9


res = Solution().fourSum(nums, target)
print("res : ", res)
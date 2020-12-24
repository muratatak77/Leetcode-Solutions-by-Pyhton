class Solution:

    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, i, res):
        seen = set()
        j = i + 1
        while j < len(nums):
            print("i :", i , " - j :", j)
            print("-nums[i] - nums[j] :   -",nums[i]," - ",nums[j])
            complement = -nums[i] - nums[j]
            print("complement : " , complement)
            print("0 seen : " , seen)
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            print("1 seen : " , seen)
            j += 1
            print("====================")


nums = [-1, 0, 1, 2, -1, -4]
res = Solution().threeSum(nums)
print(res)

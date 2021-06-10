class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            print("right : ", right, " - val : ", val)
            prod *= val
            print("     prod : ", prod)
            while prod >= k:
                prod /= nums[left]
                print("         prod : ", prod)
                left += 1
                print("         left: ", left)
            ans += right - left + 1
            print("              >> ans : ", ans)
            print("----------------------------")
        return ans


nums = [10, 5, 2, 6]
k = 100

res = Solution().numSubarrayProductLessThanK(nums, k)
print("res : ", res)
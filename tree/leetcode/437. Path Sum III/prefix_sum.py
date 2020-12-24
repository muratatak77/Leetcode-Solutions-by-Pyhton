from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k):
        count = curr_sum = 0
        h = defaultdict(int)
        is_total = False
        
        for num in nums:
            # current prefix sum
            curr_sum += num
            
            # situation 1:
            # continuous subarray starts 
            # from the beginning of the array
            if curr_sum == k:
                print("curr_sum == k / ", curr_sum, " == " , k  )
                count += 1
                print(" count : ", count)
                print("--------------")
            
            # situation 2:
            # number of times the curr_sum − k has occurred already, 
            # determines the number of times a subarray with sum k 
            # has occurred up to the current index
            print("before h :" , h)
            print("curr_sum : ", curr_sum)
            count += h[curr_sum - k]
            print("count : h[curr_sum - k]: ", h[curr_sum - k])
            # add the current sum
            h[curr_sum] += 1
            print(" count : ", count)
            print("h : ", h)
            print("====================================")

        return count


nums = [3,4,1,6]
nums = [3,4,1,6,-3]
k = 7

res = Solution().subarraySum(nums, k)
print("res : ", res)
import heapq
import os

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        print("heapify nums :", nums)

        # min = heapq.heappop(nums)
        # print("heappop nums : ", nums)

        # print("min : " + str(min))
        # heapq.heappush(nums, 1)
        # print("heappush 1 : ", nums)
        
        

        while len(nums) > k:
            heapq.heappop(nums)

        return heapq.heappop(nums)

    
        # print("heappop nums : ", nums)
        # heapq.heappop(nums)
        # print("heappop nums : ", nums)
        # return nums[-1]



nums = [3,2,1,5,6,4]
k = 2
res = Solution().findKthLargest(nums, k)

print(res)
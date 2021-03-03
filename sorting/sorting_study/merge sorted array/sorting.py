'''
	we can apply 3 pointers solution. 

	nums1 = [1,2,3,0,0,0]
	nums2 = [2,5,6]

	we can say i is connect nums1 arry.
	j is connecting nums2

	k is nums1 depend.


'''
from typing import List
class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = n-1
        j = n-1
        k = len(nums1)-1

        while i >= 0 and j >= 0:
        	if nums2[j] >= nums1[i]:
        		nums1[k] = nums2[j]
        		k -= 1
        		j -= 1
        	else:
        		nums1[k] = nums1[i]
        		k -= 1
        		i -= 1

        print("nums1 :" , nums1)

        #gather phase
        while j >= 0:
        	nums1[k] = nums2[j]
        	k -= 1
        	j -= 1

        return nums1
        	


nums1 = [1,3,5,0,0,0]
nums2 = [2,4,6]


res = Solution().merge(nums1,nums2)
print("res : ", res)

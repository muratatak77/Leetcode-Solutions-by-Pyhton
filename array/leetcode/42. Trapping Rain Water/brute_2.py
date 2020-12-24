'''
    if we can brute force : 
        
        first we need to go left side from current item. We need max item in the left side
        
        second we can go to right side from the current item and we can get max right item

        and finally we can get min(left,right)  - current main item 
        if this difference grater than 0 we can add to total 

'''

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        for i in range(1,n):
            
            left = float('-inf')
            for j in range(i-1,-1,-1):
                left = max(left, height[j])

            right = float('-inf')
            for j in range(i+1,n):
                right = max(right, height[j])

            diff = min(left,right) - height[i]
            if diff > 0:
                total += diff

        return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

res = Solution().trap(height)
print("res : ", res)

'''
 T(N) = O(n^2) because we can do multiple loops for each element 
 S(N) = O(1)  there is no extra space
'''
# class Solution {
#     public int trap(int[] height) {
#         // method 1
#         // brute force
#         // time - o(n^2)
#         int ans = 0;
#         for(int i=1;i<height.length-1;i++) {
#             int left = Integer.MIN_VALUE;
#             for(int j=i-1;j>=0;j--) {
#                 left = Math.max(left,height[j]);
#             }
#             int right = Integer.MIN_VALUE;
#             for(int j=i+1;j<height.length;j++) {
#                 right = Math.max(right,height[j]);
#             }
#             if(Math.min(left,right)-height[i] > 0)
#                 ans += Math.min(left,right)-height[i];
#         }
#         return ans;
#     }
# }
# 
# 

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

    	total = 0
    	n = len(height)

    	for i in range(1,n):
    		print("i : ", i)
    		left = float('-inf')
    		
    		for j in range(i-1,-1,-1):
    			left = max(left, height[j])
    		
    		print("  left : ", left)

    		right = float("-inf")
    		for j in range(i+1,n):
    			right = max(right, height[j])
    		print("  right : ", right)

    		diff = min(left,right) - height[i]
    		if diff > 0:
    			total += diff
    		
    		print("total : ", total)
    		print("-------------------------")

    	return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
res = Solution().trap(height)
print("res : ", res)





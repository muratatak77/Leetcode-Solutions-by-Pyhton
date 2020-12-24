'''	
	We can apply DP appraoch in this question. 
	We need first a 2D array dp table.
	bottom up dp approach.
	Idea is to get every sub-array of every length of this array and for every separate find the last balloon which needs to burst to maximize the value for that sub-array.
	Once we have calculated that for every separate we can use that information to find max value we can get for that and entire array.
	
	We will fill up the diagonal form and top right corner will be max val and the result.
	every sequare in this result matrix is capable of holding 2 number,
		1 : What is max value we can get for sub array 
		2 : what is the last balloon that needs to burst in that seperate


'''

from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        #generate a dp table
        # nums = [1] + nums + [1]
        print("nums : ", nums)

        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        print("dp : " , dp)


        for l in range(1,n+1):

        	for i in range(0, n-l+1):

        		j = i + l-1

        		print(" l : ", l , " - i :", i ,  " - j : ", j)

        		for k in range(i,j+1):

        			print(" 	k : ", k)

        			leftVal = 1
        			rightVal = 1

        			if (i != 0):
        				leftVal = nums[i-1]

        			if (j != n-1):
        				rightVal = nums[j+1]


        			before = 0
        			after = 0
        			if i != k:
        				before = dp[i][k-1]

        			if j != k:
        				after = dp[k+1][j]

        			dp[i][j] = max(leftVal * nums[k] * rightVal + before + after , dp[i][j])

        			print("		dp : " , dp)

        return dp[0][-1]


'''
	Time complexity : O(N^3)O(N). There are N^2 (left, right) pairs and it takes O(N) to find the value of one of them.

	Space complexity : O(N^2). This is the size of dp.

'''


nums = [3,1,5,8]
# nums = [2,4,3,5]
res = Solution().maxCoins(nums)
print("res : ", res)
'''
    We can reduce time compl. with the a DP solution.
    in the brute force we can use 2 loops them together.
    in DP solution we don't need 2 loops used them together. 
    We can create left and right max 1D dp array. 
        we can use this arrays.
        first, we can keep a left_max_array  start to end troughout height array
        secodn we can keep a right max array end to start troughout height array

        finally we gonna filled up 2 dp array. 
        We can get difference 2 DP array for each item.
            we can keep a total number summaization that get the difference        
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        total = 0
        print("left_max : ", left_max)
        print("right_max : ", right_max)

        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        for i in range(1,n):
            left_max[i] = max(height[i], left_max[i-1])

        print("left_max 2 : ", left_max)

        print("height : ", height)
        for i in range(n-2,-1,-1):
            print(" i : ", i, " - height[i] :", height[i])
            right_max[i] = max(height[i], right_max[i+1])

        print("right_max 2 : ", right_max)

        for i in range(1,n):
            diff = min(left_max[i], right_max[i]) - height[i]
            if diff > 0:
                total += diff

        return total





height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
res = Solution().trap(height)
print("res : ", res)



'''
    T(N) = O(N) we store max left and right side using 2 seperate array and of the end total array
    S(N) = O(N) left and right DP array
'''
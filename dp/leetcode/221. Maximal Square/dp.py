'''
    https://www.youtube.com/watch?v=RElcqtFYTm0&ab_channel=TECHDOSE


    we we think about the brute force we will get exponential time
    we can think DP solution.
        We need a 2D array DP table.
            we can fill db table all cells as 0

            we can iterate rows , cols.
            for current cell we can check this way : 

                if matrix[i][j] is "1"
                    we can check dp table  back left, top , and diagonal cells. we can get min count + 1. 
                        by this way , we can check whether all cells suitable for be square. 

    Important ; 

    We need to make sure there are no adj 0's to add current index to form a larger sequare metrix.

    as we seen in image1 , we can check whether 1 or not. 
    if 1 we can check , left , top and diogonal. 

    If we have all 1 from this way we can get min + 1 
    we get min because if we have 0 we can't get a sequare , that's way we need to get min and + 1. 
    You can check in image 2.

    if we have a zero we can go ahead a sequare. we have still 1 sequare.

    if we look image 3 we can a sequare because every way is eqaul 1. And min(1) + 1 = 2, so we can get a sequare.



'''


from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows = len(matrix)
        print("rows : ", rows)

        if rows == 0:
            return 0
        cols = len(matrix[0])
        print("cols : ", cols)

        #we add +1 because we will check previous 1 left , top dioganol and top.
        #We don't want to extra check. check image_4
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1) ]
        
        print("dp initial : ", dp)

        largest = 0
        
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                print("   i :", i , " - j : ", j)
                print("   matrix i :", i-1 , " - j : ", j-1)

                if matrix[i-1][j-1] == "1":
                    
                    print("    matrix[i-1][j-1] :", matrix[i-1][j-1])
                    dp[i][j] = min( min(dp[i][j-1], dp[i-1][j-1]), dp[i-1][j]) + 1
                    print("      dp set : ", dp)

                    if largest < dp[i][j]:
                        largest = dp[i][j]
                        print("            We find new largest : ", largest)
            print("-------- ---------- ----------- ----------")

        return largest*largest


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix = [["0","1"],["1","0"]]
# matrix = [["0"]]

res = Solution().maximalSquare(matrix)
print("res : ", res)


'''
 T(N) : O(mn) for matrix
 S(N) : O(mn)

'''
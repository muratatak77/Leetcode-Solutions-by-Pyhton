'''
i= 0	1
i= 1	1 1 
1= 2	1 2 1
		1 3 3 1


	This is a DP.
	we can do 2 iterates for row = i, for col = j
		in each i iterate, we can build a row array to i+1
		we can put first and last element as 1
			and we can do second iterate to len(row)-1
				result[j] = result[i-1][j-1] + result[i-1][j]

'''
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

    	result = []	
    	for i in range(numRows):

    		row = [None for _ in range(i+1)]
    		row[0], row[-1] = 1, 1

    		for j in range(1, len(row)-1):
    			row[j] = result[i-1][j-1] + result[i-1][j]

    		result.append(row)

    	return result

rowNumbers = 5
ans = Solution().generate(rowNumbers)
print("ans : ", ans)


'''
	T(N) = O(rowNumbers^2) 
	we have 2 for iterate. outher loop : O(rowNumbers) , inside loop each time takes O(row) number.
	Therefore , 
		1. row = 1
		second row = 2 cells
		3. row = 3 cells

		1+2+3....+ r =  r(r+1)/2 = O(r^2)

	S(N) = O(rowNumbers^2) = We need to store each number that we update in triangle.
'''

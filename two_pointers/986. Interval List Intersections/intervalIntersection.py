'''
	we have sorted arrays

	We need apply two pointer approach for this position
	first we can say i and second input is j

	firstList =  [[0,2],[5,10],[13,23],[24,25]]
	secondList = [[1,5],[8,12],[15,24],[25,26]]

	in this example : 

		if we get first items, we can reach this range : 

		0,1,2,3,4,5
		
		First State: 

		first  = 0,1,2 
		second = 1,2,3,4,5
		
		if we care about intersections for first items : 0 , 1
			we can get max(0,1) = 1  

		and second items : 2,5
			min(2,5) = 2
	
			finally we can get intersections for just first items in the both arrays. : [1,2]


		Second State: 		

			How we gonna move which pointer. 
				
				first  = 0,1,2 
				second = 1,2,3,4,5


				in this case we have some left behind numbers in second range. 
				2 > 5. we need to iterate smaller one range. like 2 
				because we need to count 2,3,4,5 numbers.

					if first[i][1] < second[j][1]
						i+= 1
					else
						j+=1 

				


				[5,10]
				[1,5]

				1,2,3,4,	5,6,7,8,9,10
				1,2,3,4,5,	6,7,8,9,10

				in further case
				max(5,1) = 5
				min(10,5) = 5
	
				there are some left behing numbers first range, we can increment second iterate
				10 > 5
					j+= 1
	

'''
from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

    	A = firstList
    	B = secondList
    	ans = []
    	i,j = 0,0
    	while i < len(A) and j < len(B):
    		lo = max(A[i][0], B[j][0])
    		hi = min(A[i][1], B[j][1])

    		if lo <= hi:
    			ans.append([lo,hi])

    		if A[i][1] < B[j][1]:
    			i += 1
    		else:
    			j += 1

    	return ans

firstList =  [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
res = Solution().intervalIntersection(firstList, secondList)
print("res : ", res)


Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


'''
	O(T) = O(M+N)
	S(T) = O(M+N)
'''
        
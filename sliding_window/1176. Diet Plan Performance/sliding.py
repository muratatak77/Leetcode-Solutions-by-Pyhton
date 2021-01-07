'''
	This problem is kind of sliding window fix lenght counting. (days = k)
	We could apply sliding window summaziation approching.
		wsum += calories[i] - calories[i-k]

		arr = [1,2,3,4,5]  k = 2
		initial 1+2 = 3

		for i in range(k,len(arr)):
			#we slide window left to right to the next index
			wsum += arr[i](3) -  arr[i-k] (2-2= 0 > 1) == 2


'''
from typing import List
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

    	#check null cases
    	if not calories:
    		return 0

    	n = len(calories)
    	if n == 0:
    		return 0
    	#initial computation
    	wsum = sum(calories[:k])
    	points = 0
    	if wsum < lower:
    		points -= 1
    	elif wsum > upper:
    		points += 1
    		
    	#remain items computation
    	for i in range(k,n):
    		wsum += calories[i] - calories[i-k]
    		if wsum < lower:
    			points -= 1
    		elif wsum > upper:
    			points += 1


    	return points

calories = [1,2,3,4,5]
k = 1
lower = 3
upper = 3


calories = [3,2]
k = 2
lower = 0
upper = 1

res = Solution().dietPlanPerformance(calories, k, lower, upper)
print("res : ", res)

'''
	T(N) = O(N)
	S(N) = O(1)
'''
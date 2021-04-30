'''
	key words : "given an integer k, in array consecutive sequence"
	We can use sliding window approach for this question.
		
		calories = [1,2,3,4,5]
		k = 2

		initial we can get a total till k.
		total = sum(calories[:k])
		if total > lower
			point +=1 
		else total > upper:
			point -=1 


		after we can start k to len(calories) a iterative
			we can apply sliding window summaization method
			total += nums[i] - nums[i-k]


'''
from typing import List
class Solution:
	def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

		total = 0
		points = 0
		total = sum(calories[:k])
		if total < lower:
			points = -1
		elif total > upper:
			points = 1

		for i in range(k,len(calories)):
			#we can apply sliding window summaization method
			total += calories[i] - calories[i-k]
			if total < lower:
				points -= 1
			elif total > upper:
				points += 1

		return points

	
calories = [1,2,3,4,5]
k = 1
lower = 3
upper = 3


# calories = [3,2]
# k = 2
# lower = 0
# upper = 1

res = Solution().dietPlanPerformance(calories, k, lower, upper)
print("res : ", res)

'''
	T(N) = O(N)
	S(N) = O(1)
'''
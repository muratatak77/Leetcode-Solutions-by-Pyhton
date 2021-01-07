'''
	Given an array of integers arr and two integers k and threshold.

	Return the number of sub-arrays of size k and average greater than or equal to threshold.

	 

	Example 1:

	Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
	Output: 3
	Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

	-------------------------------------------

	We can apply sliding window fix lenght approaching. 

	"Return the number of sub-arrays of size k and average greater than or equal to threshold." means 

		sum(arr[:k]) >=  treshold * k 

		grater than or equal treshold multiple k. because we will get avarage. 

			total / k is getting the avarage. grater than or equal to trashold meaning multiple K.

	
	After we can walk trough starting by K and length of array. We can slide our fix window. 

			wsum += arr[i] - arr[i-k]


'''

from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

    	wsum = sum(arr[:k])

    	count = 0
    	if wsum >= threshold * k:
    		count = 1

    	for i in range(k,len(arr)):
    		wsum += arr[i] - arr[i-k]
    		if wsum >= threshold*k:
    			count += 1

    	return count
        

arr = [2,2,2,2,5,5,5,8] 
k = 3
threshold = 4
res = Solution().numOfSubarrays(arr, k, threshold)
print("res : ", res)


'''
	T(N) = O(N)
	S(N) = O(1)
'''
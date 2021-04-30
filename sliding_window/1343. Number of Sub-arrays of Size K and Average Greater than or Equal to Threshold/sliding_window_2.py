'''


'''

from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

    	wsum = sum(arr[:k])
    	count = 0
    	if wsum // k >= threshold:
    		count = 1

    	for i in range(k,len(arr)):
    		wsum += arr[i] - arr[i-k]
    		if wsum // k >= threshold:
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
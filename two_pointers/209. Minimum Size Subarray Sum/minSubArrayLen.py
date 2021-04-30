'''
	1 - we will add-up items from the beginning of the array until their sum becomes greater than or equal "s"
	2 - These elements will constitute our sliding window. 
	3 - We will keep adding one element in the sliding window. 
	4 - In each step, we will also try to shrink the window from the beginning. We will shrink the window until the window's sum is smaller than "s" again.
		Check if the current window length is the smallest so far, 
		Subtract the first element of the window from the running sum to shrink the siliding window.
'''
import math
from typing import List
class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:

		arr = nums
		s = target

		window_sum = 0 
		min_length = math.inf
		window_start = 0

		for window_end in range(len(arr)):
		#get total for each index
			window_sum += arr[window_end]
			#when we reach s we can shirk the window as small as possible until the "window_sum" is smaller than s
			while window_sum >= s:
				min_length = min(min_length, (window_end-window_start)+1)
				window_sum -= arr[window_start]
				window_start += 1

		if min_length == math.inf:
			return 0

		return  min_length

s = 7
arr = [2,3,1,2,4,3]
res = Solution().minSubArrayLen(s,arr)
print("res : ", res)


'''
	T(N) = O(N) 
		For iterate visit all element just one time 
			while each elements only once
			O(N+N) > which is asymptotically equivalent to O(N)
			
	S(N) = O(1) There is no extra space

'''
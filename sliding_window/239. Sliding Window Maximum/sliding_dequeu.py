'''
	WE can apply sliding window approaching for this question.
	We can use a Queue data structure for keeping max item for every slide window. 
		Initial : 

			nums = [1,3,-1,-3,5,3,6,7], k = 3
			We can check first K th item and initiate first item in the Q.
			Q : 1
				and we can check second item with the Q
				second item is grater than first item. We can pop 1 from Q and we can push 3.
			Q : 3
				3rd item is less than final item in our Q. skip this case 

			#remain items:
				We can start K and len(nums):
				We can slide next item , 
				in the Sliding window approaching we need to check first item. 
					if Q[0] == nums[i-k]
						popleft from Q. because we need to remove first item 
						when we pass to next item in sliding window.

					pushin process in the above.
					result.append(Q[0])


'''
from typing import List
from collections import deque
class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		
		q = deque()
		result = []

		def pushin(val):
			print("We got val in puhsin : ", val,  " / Q : ", q)
			while q and q[-1] < val:
				q.pop()
				print(" 		After POP : ", q)
			q.append(val)

		#initial to the k
		for i in range(k):
			pushin(nums[i])
			print("		After pushin Q: ", q)
			print("		-------")

		#push the first item to the result array.
		result = [q[0]]

		#remain items check
		for i in range(k,len(nums)):
			
			# when slide window to the next item 
			# we need to check whether first item in the Q or not
			print(" q[0] : ", q[0])
			if q[0] == nums[i-k]:
				q.popleft()
				print("We got equal  item. Popleft :", q)

			pushin(nums[i])
			print("		After pushin Q: ", q)
			result.append(q[0])
			print(" 		Result APPEND : ", result)
			print("-----------------")

		return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = Solution().maxSlidingWindow(nums, k)
print("res : ", res)

'''
	T(N) = O(N)  2 seperate loops.
	S(N) = O(N)  an autput array : O(N-k+1)
				 deque  : O(k)
'''

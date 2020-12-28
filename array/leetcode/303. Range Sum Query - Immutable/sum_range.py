'''
	if we are thinking Brute Force : 
		get i and j inside the one loop iterate. 
		T(N) = O(N), S(N) = O(1)

	we can get better optimum solution :

	We can do it initial keeping in the array sums items in a loop.
	We could trade in extra space for speed. 
	By pre-computing all range sum possibilities and store its results in a hash table or just array.
	We can speed up the query to constant time.

	initial pre-computing:

	nums = [1,1,1,1,1,1]
	we can compute all range sum in itial : 
		prefix_sum = [1,2,3,4,5,6]

	in sumRange method we can directly get 
		prefix_sum[j]  - prefix_sum[i-1]

		if we have i = 2 , j = 5
		totaly [1,1,1,1] = 4

		we can get from prefix_sum = [1,2,3,4,5,6]  --> 6 - 2 = 4 
'''

class NumArray(object):
	"""docstring for NumArray"""
	def __init__(self, nums):
		self.prefix_sum = []
		running_sum = 0
		for i in range(len(nums)):
			running_sum += nums[i]
			self.prefix_sum.append(running_sum)

		print("self.prefix_sum : ", self.prefix_sum)


	def sumRange(self,i,j):

		if i == 0:
			return self.prefix_sum[j]
		
		return self.prefix_sum[j] - self.prefix_sum[i-1]


# nums = [-2, 0, 3, -5, 2, -1]
nums = [1,1,1,1,1,1]
i = 0
j = 2

i = 2
j = 5

numArray = NumArray(nums)
res = numArray.sumRange(i,j)
print("res : ", res)

'''
	T(N) = O(1) get from array item constant time. We have initial O(N^2) time but in pre-computing. 
	Pre-computation done in the constructer takes O(N^2).

	S(N) = O(N) we are using one extra space that it is prefix_sum
'''

# import collections

# This problem is a window sliding problem. We need a queue to store the max element throughout the subarray size
# arr = [1, 3, -1, -3, 5, 3, 6, 7]
# w = 3
# 
# 
# 1,3,-1
# q = [1,2]
# result = [3]
# 
# 3,-1,-3
# q = [1,2,3]
# result = [3,3]
# 
# -1, -3, 5
# index = 4  - 1 = 3
# popleft q = [2,3]
# pop q = [2] , pop q = []
# q = [4]
# result = [3,3,5]
# 

import collections

def max_in_sliding_window(arr, w):
	if not arr:
		return []
	if not w: 
		return []

	n = len(arr)
	q = collections.deque()
	result = []

	for i in range(n):

		#size check current index and first element in the q
		# The queue must be a maximum is 3 items. 
# 		# That's why we need to compare the subarray size and current index. 
# 		# If we subtract the first element in the queue from the current index from and if the result equals the subarray size, we need "pop left" from the queue.
		if q and i - q[0] == w:
			q.popleft()

		#to find max element compare current item and q last item in the array 
		# Every time the first item should be the max element in the subarray. 
# 		# If the next item grater than from the queue last element, we need to pop from the queue.
		while q and arr[q[-1]] < arr[i]:
			q.pop()

		q.append(i)

		#check reach subarray size 
		#if the current index grater-equal than the subarray index size, we can add to the result array 
		if i >= w-1:
			result.append(arr[q[0]])

	return result


# def max_in_sliding_window(arr, w):
# 	n = len(arr)
# 	queue = collections.deque()
# 	result = []

# 	for i in range(n):
# 		print("index : ", i, " - item : ", arr[i])
# 		print("queue : ", queue)
# 		# print("------")
# 		# The queue must be a maximum is 3 items. 
# 		# That's why we need to compare the subarray size and current index. 
# 		# If we subtract the first element in the queue from the current index from and if the result equals the subarray size, we need "pop left" from the queue.
# 		if queue and i - queue[0] == w:
# 			print("i - queue[0] : ", i ,"-", queue[0])
# 			queue.popleft()
# 			print("after queue pop left : ", queue)
			
# 		# Every time the first item should be the max element in the subarray. 
# 		# If the next item grater than from the queue last element, we need to pop from the queue.
# 		while queue and arr[queue[-1]] < arr[i]:
# 			print("arr[queue[-1]] < arr[i] : ", arr[queue[-1]], "<", arr[i])
# 			queue.pop()
# 			print("after queue.pop() : ", queue)

# 		queue.append(i)
# 		print("after append queue : ", queue)
		
# 		# if the current index grater-equal than the subarray index size, we can add to the result array 
# 		if i >= w-1:
# 			result.append(arr[queue[0]])
# 			print("result : ", result)

# 		print("----------------------------------------------------")
# 	return result


arr = [1, 3, -1, -3, 5, 3, 6, 7]
w = 3




print(max_in_sliding_window(arr,w))
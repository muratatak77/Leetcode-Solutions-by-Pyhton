import heapq
from collections import Counter

def topK(arr, k):

	if k == 0 or k >= 10^5:
		return arr

	arr = Counter(arr)   

	return heapq.nlargest(k, arr)


arr = [1, 5, 4, 4, 2]
k = 2

arr = [4,2,1,6,2,10,4,3,10,6,5,6,7,2,10,10,4,6,5,8]
k = 7

res = topK(arr,k)
print(res)




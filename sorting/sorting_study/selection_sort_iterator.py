import sys


# https://www.youtube.com/watch?v=xWBP4lzkoyM
# Logic : Array is considered into parts unsorted and sorted (initially whole array is sorted)
# selection 			1. Select the lowest element in the remaning array ( if a[j] < a[min_idx])
# swapping  			2. bring in to the starting position (a[i], a[min_idx] = a[min_idx], a[i])
# counter shifht: 3. change the counter for unsorted array by one (i)

def selection_sort_iterator(A):
	# Traverse through all the elements
	for i in range(0,len(A)-1):
		min_idx = i

		# Traverse through second iterator to find min index
		for j in range(i+1, len(A)):	
			if A[j] < A[min_idx]:
				min_idx = j

		# swap the found minimum element with the starting position
		# Bring in to the starting position 
		A[i], A[min_idx] = A[min_idx], A[i]
	return A

arr = [13,11,12,5,6,1]
res = selection_sort_iterator(arr)
print("result : " + str(res))
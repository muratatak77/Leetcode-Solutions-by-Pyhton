def bubble_sort(A):
	# first  : we can iterator through all Aay. we can say (i) iterator
	n = len(A)
	for i in range(0, n-1):

		# second : we can start second iterate from right to left way. Start last element j to the ith element. 
		for j in range(n-1, i, -1):
			if A[j-1] > A[j]:
				# third  : We can find the min element the left by repeated swap.
				A[j], A[j-1] = A[j-1], A[j]


A = [13,12,11,5,6]
# A = [5,1,4,2,8,9]
bubble_sort(A)
print("res : " + str(A))



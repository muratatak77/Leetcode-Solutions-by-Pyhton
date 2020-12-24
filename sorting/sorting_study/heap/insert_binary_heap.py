import math

def insert(A, n):
	i = n
	temp = A[n]

	while i>1 and temp > A[i//2]:
		A[i] = A[i//2]
		i = i//2
		print(i)

	A[i] = temp
	return A

A = [0,30,20,15,5,10,12,6,50]
A = [0,50, 30, 15, 20, 10, 12, 6, 5, 35]

n = 7
n = 8
insert(A, n)
print(A)


# O(longN)
# 
# 
# Operations on Max Heap:
# getMax(): It returns the root element of Max Heap. Time Complexity of this operation is O(1).
# extractMax(): Removes the maximum element from MaxHeap. Time Complexity of this Operation is O(Log n) as this operation needs to maintain the heap property (by calling heapify()) after removing root.
# insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree. If new key is smaller than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
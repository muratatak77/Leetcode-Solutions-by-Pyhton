def insert(A, n):
	i = n
	temp = A[n]
	while i>1 and temp < A[i//2]:
		A[i] = A[i//2]
		i = i//2
	A[i] = temp

def create_heap(A):
	for i in range(2,8):
		insert(A,i)

A = [0,10,20,30,25,5,40,35]
res = create_heap(A)
print(str(A))

#DOESNT WPORK
#
def insert(A, n):
	i = n
	temp = A[n]
	while i>1 and temp < A[i//2]:
		A[i] = A[i//2]
		i = i//2
	A[i] = temp


def delete(A, n):
	A[1],A[n] = A[n],A[1]
	i = 1
	j = i * 2

	while j < n-1:
	 	if j < n-1 and A[j+1] > A[j]:
	 		j += 1 

	 	if A[i] > A[j]:
	 		A[i],A[j] = A[j],A[i]
	 		i = j
	 		j = j *2
	 	else:
	 		break



def sort(H):
	for i in range(2,8):
		insert(H,i)

	print("after insert Heap " ,H)

	for i in range(1,7,-1):
		delete(H, i)

H = [0,14,15,5,20,30,8,40]
print("Initial Heap " + str(H))
sort(H)
print("Sorted Heap " + str(H))
def delete(A, n):
	x = A[n]
	i = 1
	j = i * 2

	while j < n-1:
	 	if A[j+1] > A[j]:
	 		j += 1 

	 	if A[i] < A[j]:
	 		A[i],A[j] = A[j],A[i]
	 		i = j
	 		j = j *2
	 	else:
	 		break

	A[n] = x


# first binary heap = [0,40,35,30,15,10,25,5] # binary heap

A = [0,5,35,30,15,10,25,40]
n = 7
delete(A, n)
print(A)


#after deletion and insert 
# A = [0, 25, 15, 30, 5, 10, 40, 35]
#insert and after deletion 
#A = [0, 25, 15, 10, 5, 40, 35, 30]
#every insert and after deletion getting ascending sorted

# we delete element and copy last place

#heap sort 
#1. create heap of 'n' element
#2. Delete n elements 1-by-1
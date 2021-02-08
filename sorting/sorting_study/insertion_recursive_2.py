def insertion_rec(A,n):
    # base case
    if n<=1:
        return

    insertion_rec(A,n-1)

    nth = A[n-1]
    j = n-2
    while j>=0 and A[j]>nth:
        A[j+1] = A[j]
        j = j-1
    A[j+1]=nth
    return A

A = [12, 11, 13, 5, 6] 
insertion_rec(A, len(A))
print ("Sorted Aay is:" + str(A)) 

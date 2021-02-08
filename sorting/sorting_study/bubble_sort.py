def bubble_sort(arr):
	n = len(arr)
	print("n : " + str(n))
	print("================")

# in the bobble sort : 
# first : we can iterator through all array. we can say (i) iterator
# 
# second : we can start to iterator from first element to n-i-1 element. 
# we will put biggest element at the end of array. after put the element as the next, we 
# will iterate remind element (n-i-1). we will have sorted right to left.
# 
# thirth : if the element grater than the  next element , we will swap.
# 
	for i in range(0, len(arr)):
		print("i : " + str(i))
		
		for j in range(0, n-i-1):
			print("j : " + str(j))
			
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				print("arr : " + str(arr))



	print(" =============== ")





arr = [13,12,11,5,6]
bubble_sort(arr)
print("res : " + str(arr))



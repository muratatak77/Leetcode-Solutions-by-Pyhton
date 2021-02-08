def decrease_conquer_insertion_sort(arr):

	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1

		while j > 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
			
		arr[j+1] = key
Decrease or reduce problem instance to smaller instance of the same problem and extend solution.
Conquer the problem by solving smaller instance of the problem.
arr = [11,14,12, 5,6]
decrease_conquer_insertion_sort(arr)
print("result : " + str(arr))
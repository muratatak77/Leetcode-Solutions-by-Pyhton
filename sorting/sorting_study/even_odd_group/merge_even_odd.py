def mergeGroup(arr):

	i = 0
	for j in range(len(arr)):
		if arr[j]%2 == 0:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	return arr


arr = [1,2,3,4,6,9,5]

res = mergeGroup(arr)
print("res : ", res)




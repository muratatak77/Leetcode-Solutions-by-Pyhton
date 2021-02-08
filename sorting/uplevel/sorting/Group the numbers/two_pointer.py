# Complete the function below.

# two pointer pass appoarch 

def solve(arr):

	i = 0
	j = len(arr)-1
	
	while i < j:
		if (arr[j] % 2 == 0) and (arr[i] % 2 != 0):
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j -= 1
		elif arr[j] % 2 != 0:
			j -= 1
		elif arr[i] % 2 == 0:
			i = i+1
	return arr

arr = [1,3,5,6,9,4,8,6,1,3]
arr = [1, 2, 3, 4]
arr = [1, 2, 3, 4,6,3,7,9,2,2,5,1,2,3,9,0,6,3,6,8]

res = solve(arr)
print(res)
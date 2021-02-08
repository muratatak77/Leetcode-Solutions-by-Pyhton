def radix_sort(arr):

	max_number = max(arr)

	exp = 1
	while  max_number//exp > 0:
		arr = counting_sort(arr, exp)
		exp += 10
	return arr


def counting_sort(arr, exp):
	n = len(arr)

	#we need output array for result
	output = [0] * n

	#counting array
	count = [0] * 10

	# we need to build counting array
	for i in range(0,n):
		index = arr[i]//exp
		count[index%10] += 1

	#change count[i] so that count[i] now contains actual position of this digit in output array
	for i in range(1,10):
		count[i] += count[i-1]

	#build the output array
	i = n-1
	while i >= 0:
		index = arr[i] // exp
		c_index = count[int(index%10)] - 1
		output[c_index] = arr[i]
		count[int(index % 10)] -= 1
		i -= 1

	# copy outpur array to arr so that arr now contains sorted numbers
	for i in range(0,n):
		arr[i] = output[i]

	return arr


arr = [170,3,90,2,12,45,33]
res = radix_sort(arr)
print(res)
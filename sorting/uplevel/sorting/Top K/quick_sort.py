# Complete the function below.
import random
from random import randint

def topK(arr, k):

	if k == 0 or k >= 10^5:
		return arr

	# arr = list(arr)
	# arr = Counter(arr)
	# arr = unique(arr)

	print("arr 1 :", arr)
	return select(arr, 0, len(arr)-1, len(arr) - k)

def select(arr, left, right, k_top):

	if left == right:
		return arr[left]

	pivot_index = random.randint(left, right)
	pivot_index = partition(arr, left, right, pivot_index)

	print("k_top :" , k_top)
	print("arr[pivot_index] :" , arr[pivot_index])

	if k_top == arr[pivot_index]: #and k_top + 1 == arr[pivot_index + 1]:
		return { arr[k_top] , arr[k_top+1] }
	elif k_top < arr[pivot_index]:
		return select(arr, left, pivot_index - 1, k_top)
	else:
		return select(arr, pivot_index + 1, right, k_top )


def partition(arr, left, right, pivot_index):

	#get pivot
	pivot = arr[pivot_index]
	
	print("pivot_index ", pivot_index)
	print("pivot ", pivot)

	#change pivot position to the right
	arr[pivot_index],arr[right] = arr[right], arr[pivot_index]

	#move all elements to the left
	store_index = 0
	for i in range(left, right):
		if arr[i] < pivot:
			arr[store_index], arr[i] = arr[i], arr[store_index]
			store_index += 1
	
	print("before arr : ", arr)

	#move pivot final position
	arr[right], arr[store_index] = arr[store_index], arr[right]
	print("last arr : ", arr)
	return store_index

def unique(list1): 
	unique_list = [] 
	for x in list1: 
		if x not in unique_list: 
			unique_list.append(x) 
	return unique_list


arr = [1, 5, 4, 4, 2]
k = 2

# arr = [4,2,1,6,2,10,4,3,10,6,5,6,7,2,10,10,4,6,5,8]
# k = 7

res = topK(arr,k)
print(res)




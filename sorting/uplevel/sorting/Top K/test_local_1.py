# Complete the function below.
# divide - conquer appoarch.
# quick select like quick sort
# k th largest element meaning n-k smallest element, hence one could implement k th smallest element
# O(N) avarage time complexity. Normally quick sort would result in O(nlogn). Here there is no deal with both parts since now.
# n-k smallest element : that reduces avarage time complexity to O(n)
# choose random pivot
# use a partition algoritm to place sorted position, move smaller elements to the left of pivot, and larger or equals one to the right.

import random
from random import randint

from collections import Counter

def topK(arr, k):
    if k == 0 and k <= 100000:
        return arr
    
    if len(arr) == 0 and len(arr) <= 100000:
        return arr

    count = Counter(nums)
    arr = list(count.keys())
    print("arr : ", arr)

    # arr = unique_list(arr)
    
    if len(arr) < k:
        return arr
        
    return select(arr, 0, len(arr)-1, len(arr)-k )
    
def select(arr, left, right, k_th):
    
    if left == right:
        return arr[k_th:]
    
    pivot_index = random.randint(left, right)
    pivot_index = partition(arr, left, right, k_th)
    
    if k_th == pivot_index:
        return arr[k_th:]
    elif k_th < pivot_index:
        return select(arr, left, pivot_index-1, k_th)
    else:
        return select(arr, pivot_index+1, right, k_th)
    

def partition(arr, left, right,pivot_index):
    
    pivot = arr[pivot_index]
    # move pivot to the right
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    
    #move smaller element rather than pivot to the left
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    
    #final place for pivot
    arr[right], arr[store_index] = arr[store_index], arr[right]
    
    return store_index
    

    
# def unique_list(list1):
#     u_list = []
#     for x in list1:
#         if x not in u_list:
#             u_list.append(x)
#     return u_list
    


# nums  = [11,4,8,9,6,6,2,10,2,8,1,2]
# k = 9

nums = [4,2,1,6,2,10,4,3,10,6,5,6,7,2,10,10,4,6,5,8]
k = 7

res = topK(nums,k)
print(res)

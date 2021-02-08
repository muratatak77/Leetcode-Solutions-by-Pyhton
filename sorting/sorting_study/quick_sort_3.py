def quickSort(arr, start, end):
    
    if start >= end:
        return
    p = getPartition(arr, start, end)
    quickSort(arr, start, p-1)
    quickSort(arr, p+1, end)
    return arr

def getPartition(arr, left, right):
    
    p_index = (left+right)//2
    pivot = arr[p_index]

    #moved pivot element to the right
    arr[right], arr[p_index] = arr[p_index], arr[right]

    #moved smallest element than the pivot to the left
    store_index = left
    for i in range(left, right):
        if arr[i]<pivot:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    #changed  store index with the right
    arr[right], arr[store_index] =  arr[store_index], arr[right]  

    return store_index

arr = [6,3,5,2,4,1]
res = quickSort(arr, 0, len(arr)-1)
print(res)


# import random

# def quick_sort(array, start, end):
#     print("start : ", start)
#     print("end : ", end)

#     if start >= end:
#         print("invalid case ----- ")
#         return 

#     p = partition(array, start, end)
#     print("Got partition index : ", p)
#     quick_sort(array, start, p-1)
#     quick_sort(array,p+1, end)

#     return array

# def partition(arr, left, right):

#     #random pivot
#     #
#     print("We ll process :" , arr[left:right+1], " - left : ", left , " - right :" , right)
#     mid = (left + right)//2
#     # mid = random.randint(left, right)     
#     pivot = arr[mid]
#     print("pivot : ", pivot)

#     #moved pivot to the end 
#     arr[right],arr[mid] =  arr[mid], arr[right]
#     print("0 arr :", arr)

#     #moved aall smallest element to the left
#     store_index = left
#     for i in range(left, right):
#         if arr[i]<pivot:
#             arr[i], arr[store_index] = arr[store_index], arr[i]
#             store_index += 1

#     print("arr 1 : ", arr)

#     arr[right], arr[store_index] = arr[store_index], arr[right]
#     print("arr 2 : ", arr)
#     print("===========================")
#     return store_index


# arr = [3,2,1,5,6,4,10,7,8,2,10,15,14,11,0]
# arr = [50,40,30,20,10]

# res = quick_sort(arr, 0, len(arr)-1)
# print(res)
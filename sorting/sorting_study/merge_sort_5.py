def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
        combine_sort(arr, left, right)
        return arr

def combine_sort(arr, left, right):
    
    #for 2 halves
    i ,j = 0,0

    #for main iterator
    k = 0    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    #for left remain values
    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1

    #for remain right values
    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1

    return arr

arr = [3,4,1,2,8,9,0,12]
res = merge_sort(arr)
print(res)
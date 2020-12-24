def divide(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        divide(left)
        divide(right)
        combine(left, right, arr)

def combine(left, right, arr):

    #we need i and j for halves (left, right)
    i=0
    j=0
    #we will use main arr iterator
    k=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k+=1

    while i < len(left):
        arr[k] = left[i]
        i += 1 
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

arr  = [13,12,15,5,6]
# arr  = [1,1,1,1,1,1,1]
divide(arr)
print("sorted : " +str(arr))

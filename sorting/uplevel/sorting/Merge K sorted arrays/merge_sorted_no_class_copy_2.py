# This solution divide - conquer algoritms. after work. merge sort. 
# Complete the mergeArrays function below.
# I sent a basic solution before. But I need to repeat sorting algoritms. 
# I found a java solution in uplevel attempts part.  This solution is not mine. :) just I try to learn and repeat divide - conquer algoritms
#
def mergeArrays(arr):
    is_asc = is_asc_(arr)
    return divide(arr, 0, len(arr)-1, is_asc)

#I applied merge sort.
def divide(arr, start, end, is_asc):


    #if arr has just 1 element
    if len(arr) == 1:
        return arr[0]
        
    #if we complete sorted process
    if start >= end:
        return arr[end]
    
    mid = (start+end)//2
    left = divide(arr, start, mid, is_asc)
    right = divide(arr, mid+1, end, is_asc)

    print("left : " , left)
    print("right : " , right)

    return merge(arr, left, right, is_asc)
    
    
def merge(arr, left, right, is_asc):
    #for 2 halves
    l = 0
    r = 0
    #we need new array
    merged = []
    
    while l < len(left) and r < len(right):
        #we need to check array ascending or desc 
        check = False
        if is_asc:
            check = left[l] < right[r] #ascending sort
        else:
            check = left[l] > right[r] #descending sort
        
        if check:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    
    print("merged 1 >>>>> ", merged)

    #for remaning  left side elements
    while l < len(left):
        merged.append(left[l])
        l += 1
        
    #for remaning right side elements
    while r < len(right):
        merged.append(right[r])
        r += 1
    print("merged 2 >>>>>  ", merged)
    
    return merged


def is_asc_(arr):
    k = len(arr)
    n = len(arr[0])
    redirect_asc = True
    for i in range(k):
        if arr[i][0] > arr[i][n-1]:
            redirect_asc = False
            break
    return redirect_asc


arr = [[1, 3, 5, 7],[2, 4, 6, 8],[0, 9, 10, 11], [12,15,17,23]]
res = mergeArrays(arr)
print(res)

    
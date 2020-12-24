def merge_arrays(arr):
    is_asc = is_asc_(arr)
    divide(arr,0,len(arr)-1, is_asc)

def divide(arr, start, end, is_asc):
    if len(arr) == 1:
        return arr[0]

    if start>=end:
        return arr[end]

    mid = (start+end)//2
    left = divide(arr, start, mid, is_asc)
    right = divide(arr, mid+1, end, is_asc)
    return merge(arr, left, right, is_asc)

def merge(arr, left, right, is_asc):

    lindex = 0
    rindex = 0
    merged = []
    # merged = [None] * (len(left) + len(right))

    while lindex < len(left) and rindex < len(right):
        check = False
        if is_asc:
            check = left[lindex] < right[rindex]
        else:
            check = left[lindex] > right[rindex]

        if check:
            merged.append(left[lindex])
            lindex += 1
        else:
            merged.append(right[rindex])
            rindex += 1

    while lindex < len(left):
        merged.append(left[lindex])
        lindex += 1

    while rindex < len(right):
        merged.append(right[rindex])       
        rindex += 1

    
    print("merged : " , str(merged))

    return merged              


def is_asc_( arr):
    direction_asc = True
    k = len(arr)
    n = len(arr[0])
    for i in range(k):
        if arr[i][0] > arr[i][n-1]:
            direction_asc = False
            break
    return direction_asc

    
arr = [[1, 3, 5, 7],[2, 4, 6, 8],[0, 9, 10, 11], [12,15,17,23]]
merge_arrays(arr)



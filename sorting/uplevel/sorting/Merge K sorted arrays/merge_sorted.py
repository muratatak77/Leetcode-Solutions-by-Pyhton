#
# Complete the mergeArrays function below.
#
def mergeArrays(arr):
    
    k = len(arr)
    n = len(arr[0])
    direction_asc = True
    
    for i in range(k):
        if arr[i][0] > arr[i][n-1]:
            direction_asc = False
            break
    
    sum = []
    for item in arr:
        sum += item
    
    if direction_asc:
        sum.sort()
    else:
        sum.sort(reverse = True)
    
    return sum


arr = [[1, 3, 5, 7],[2, 4, 6, 8],[0, 9, 10, 11]]
res = mergeArrays(arr)
print(res)


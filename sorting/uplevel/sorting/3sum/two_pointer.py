# Complete the function below.

# we can apply 2 pointers approach
# we can seperate first element first that it would be less than or equal zero. Other element would be any number.
# 
def findZeroSum(arr):
    # [10, 3, -4, 1, -6, 9]
    #1 <= n <= 2000
    n = len(arr)
    if n <= 1 or n >= 2000:
        return arr
    
    #we need to sort arr for this approach
    arr.sort()
    res = []
    # [-6, -4, 1, 3, 9, 10]
    #we need to find smaller or equal than 0 and no duplicate
    for i in range(len(arr)):
        if arr[i] > 0:
            break
        if i== 0 or arr[i] != arr[i-1]:
            twoSum(arr, i, res)

    return res
    
    
def twoSum(arr, i, res):
    lo = i+1
    hi = len(arr)-1
    
    while lo < hi:
        sum = arr[i] + arr[lo] + arr[hi]
        if sum == 0:
            res.append(str(arr[i])+","+str(arr[lo])+","+str(arr[hi]))
            lo += 1
            hi -= 1
            while lo < hi and arr[lo] == arr[lo-1]:
                lo += 1
        elif sum < 0:
            lo += 1
        else:
            hi -= 1

            
# def listToString(list_):  
#     res = []
#     for i in list_:
#         part = ', '.join(map(str, i))
#         res.append(part)
#     return res


arr = [10,3,-4,1,-6,9]
arr = [-41,-67,12,-25,46,-26,-24,27,-13,-4,17,-37,1,-6,-19,-44,-67,75,3,-10,10,-39,64,-15,49,-48,-20,26,50,78,-28,96,-10,88,10,-8,-28,-3,-54,-54,57,-36,4,15,-42,66,19,-58,-53,50,27,52,22,-42,-84,48,93,52,9,-6,-78,-86,28,-42,1,12,-83,38,-33,-42,-65,6,52,44,16,23,-36,43,38,-5,-23,6,24,-53,-61,-41,-39,-79,-65,60,-4,2]

res = findZeroSum(arr)
print(res)
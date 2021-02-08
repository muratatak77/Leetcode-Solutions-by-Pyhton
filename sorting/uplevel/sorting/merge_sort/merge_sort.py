#
# Complete the 'merge_sort' function below.
#
# The function accepts an integer array as parameter.
#

def merge_sort(arr):
    
    if len(arr) > 1:
     
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        # if left == right:
            # return arr
        
        merge_sort(left)
        merge_sort(right)
        
        #for 2 halves
        i = 0
        j = 0
        
        #for main iterater
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        #for remain params
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        
        return arr
    
    

arr = [1,2,1,2]
arr = [1,1]
res = merge_sort(arr)
print(res)
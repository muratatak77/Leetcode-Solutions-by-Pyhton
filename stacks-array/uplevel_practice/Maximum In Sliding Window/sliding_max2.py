# Complete the function below.

# This problem is a window sliding problem. We need a queue to store the max element throughout the subarray size

import collections

def max_in_sliding_window(arr, w):
    
    n = len(arr)
    
    if n > 1000000 or n < 1:
        return []
        
    if w > n or w < 1:
        return []
    
    
    q = collections.deque()
    result = []
    
    for i in range(n):
        
        # The queue must be a maximum is 3 items. 
        # That's why we need to compare the subarray size and current index. 
        # If we subtract the first element in the queue from the current index from and if the result equals the subarray size, 
        # we need "pop left" from the queue.
        if q and i - q[0] == w:
            q.popleft()
        
        # Every time the first item should be the max element in the subarray. 
        # If the next item grater than from the queue last element, we need to pop from the queue.
        while q and arr[q[-1]] < arr[i]:
            q.pop()
            
        q.append(i)
        
        #if the current index grater-equal than the subarray index size, we can add to the result array 
        if i >= w-1:
            result.append(arr[q[0]])
    
    return result
    

arr = [1, 3, -1, -3, 5, 3, 6, 7]
w = 3

print(max_in_sliding_window(arr,w))
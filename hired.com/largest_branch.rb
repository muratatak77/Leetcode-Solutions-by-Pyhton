#Determine larger branch in binary tree represented as an array | Question from another site

def solution(arr)
    # Type your solution here 
    return "" if arr.nil?
    n = arr.length
    return "" if n == 0
    left_sum , right_sum  = 0,0
    
    left = 1
    right = 2
    left_sum = get_tree_sum(arr, left)
    right_sum = get_tree_sum(arr, right)
    
    return "Left" if left_sum  > right_sum 
    return "Right" if left_sum < right_sum 
    return ""
        
end


def get_tree_sum(arr, i)
    return 0 if i > arr.length or arr[i] == -1
    left_child = 2*i+1
    right_child = 2*i+2
    sum = 0
    if i < arr.length
        sum = arr[i] + get_tree_sum(arr, left_child) + get_tree_sum(arr, right_child)
    end
    sum
end

arr = [3,6,2,9,-1,10]
res = solution(arr)
puts "res : #{res}"
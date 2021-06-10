=begin
  We can use 2 pointers approach . we can follow a way to create left and right params. While right item contunie in a loop, we can check between right and left indices.
  
  Input: [2, 5, 3, 10], target=30
  prod *= 2  > 2  
    result = [2]
  prod *= 5  > 10
    result = [2],[5]

  prod *= 10  > 30 

        [2, 5, 3, 10] 
        left  = 0, right = 2 

        we can divide first item and we can get new prod. Why we removed first item because we have new item 3. we should use first item for generate new list.
        
        prod /= arr[left]  > 30/2 = 15 

        and we need to increment left += 1
        
          we can use a queue data structure. 
          first we can add a temp_list = queue([3]) , queue([5,3])
          we can add result getting queue direct values.

        result = [2],[5],[3], [5,3]

=end

def find_subarrays(arr, target)
  result = []
  prod = 1
  left  = 0
  n = arr.length
  for right in (0..n-1) do
    prod *= arr[right]
    while prod >= target and left < n-1
      prod /= arr[left]
      left += 1
    end
    temp_list = []
    for i in right.downto(left) do
      temp_list << arr[i]
      result << temp_list.reverse
    end
  end
  result
end

arr = [2, 5, 3, 10]
target = 30
res= find_subarrays(arr,target)
puts("res  : #{res}")


=begin
  T(N) = for loop = O(N) , creating sub array O(N) in the worst case > O(N^2)
  S(N) =  O(N) for temp list
=end


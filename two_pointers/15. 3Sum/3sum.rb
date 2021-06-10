# @param {Integer[]} nums
# @return {Integer[][]}
# we can take help from two sum approach
# first
# 	we need sorting because we don't want to duplicate
# 	start a loop. we can look first item and we can define left and right value in our sorted nums.
#
#

def three_sum(nums)
  return [] if nums.nil?
  n = nums.length
  return [] if n < 3

  nums = nums.sort
  result = []

  for i in (0..n)

    #we don't need if we have greater than 0. Because we need our summaization will be 0. we can save a lot of time
    break if nums[i].to_i > 0

    # if in 0 we can contunie avoid out of index error or we don't want to duplicate , we want unique items
    if i == 0 or nums[i-1] != nums[i]
      search_pair(i, n, nums,result)
    end
  end

  return result
end


def search_pair(i,n, nums, result)
  puts "i : #{i}"
  left = i+1
  right = n-1

  while left < right
    sum = nums[i] + nums[left] + nums[right]
    if sum == 0
      result.append([nums[i], nums[left], nums[right]])
      left +=1
      right -= 1
      #after change left and right pointers , we can encounter same items so we need to check again previous items
      while left < right and nums[left-1] == nums[left]
        left += 1
      end
      while left < right and nums[right-1] == nums[right]
        right -= 1
      end
    elsif sum < 0
      left +=1
    elsif sum > 0
      right -= 1
    end
  end
end


nums = [-3, 0, 1, 2, -1, 1, -2]
# nums = [-1,0,1,2,-1,-4]
# nums = [-5, 2, -1, -2, 3]
# nums = []
# nums = [0]
# nums = [1]

res = three_sum(nums)
print("res : ", res)


=begin
		
	Time complexity #
			Sorting the array will take O(N * logN). 
			The sear_pair() function will take O(N). 

			As we are calling search_pair() for every number in the input array, this means that overall three_sum() will take O(N * logN + N^2)
	​​ ), which is asymptotically equivalent to O(N^2)O

	Space complexity
	Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.	

=end

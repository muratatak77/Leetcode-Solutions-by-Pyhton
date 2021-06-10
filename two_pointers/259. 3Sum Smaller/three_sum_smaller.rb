# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def three_sum_smaller(nums, target)
  nums = nums.sort
  n = nums.length
  return 0 if n == 0
  count = 0
  for i in (0..n-2)
  	count += search_pair(nums, target, i)
  end
  return count
end


def search_pair(nums, target, i)
	left = i + 1 
	right = nums.length - 1
	count = 0
	while left < right		
		sum = nums[i] + nums[left] + nums[right]
		if sum < target
			#we can get a diff right - left. If right is works for this process , between the right and left indices also works in a sorted arr.
			count += right - left  
			left += 1
		else
			right -= 1
		end
	end
	return count
end


nums = [-1, 0, 2, 3]
target = 3

res = three_sum_smaller(nums, target)
puts "res : #{res}"
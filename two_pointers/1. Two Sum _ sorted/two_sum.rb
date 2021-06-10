# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
	left, right = 0, nums.length-1
	while left < right
		current_sum = nums[left] + nums[right]
		if current_sum == target
			return [left, right]
		end
		puts "current_sum : #{current_sum}"

		if target > current_sum
			left += 1
		else
			right -= 1
		end
	end

	return [-1,-1]

end



nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

res = two_sum(nums, target)
puts "res : #{res}"
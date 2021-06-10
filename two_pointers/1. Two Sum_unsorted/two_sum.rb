# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    n = nums.length
    map = {}
    for i in (0..n-1)
    	diff = target - nums[i]
    	if map.include? diff
    		return [map[diff], i]
    	else
    		map[nums[i]] = i
    	end
    end
end


nums = [3,2,4]
target = 6

res = two_sum(nums, target)
puts "Res : #{res}"
def remove_element(nums, val)
	key = val
	next_index = 0
	for i in (0..nums.length-1)
		if nums[i] != key
			nums[next_index] = nums[i]
			next_index += 1
		end
	end
	return next_index
end


nums = [3,2,2,3]
val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2


res = remove_element(nums, val)
puts "res : #{res}"
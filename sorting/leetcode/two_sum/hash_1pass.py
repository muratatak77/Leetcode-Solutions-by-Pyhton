def sort_hash(nums, target):
	
	map = {}
	n = len(nums)

	for i in range(0,n):
		complement = target - nums[i]
		if complement in map:
			return [map.get(complement), i]
		else:
			map[nums[i]] = i


nums = [2, 7, 11, 15]

check = sort_hash(nums, 9)
print(check)

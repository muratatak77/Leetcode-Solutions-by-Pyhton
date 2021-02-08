def sort_hash(nums, target):
	
	map = {}
	n = len(nums)

	for i in range(0,n):
		map[nums[i]] = i

	print("map " + str(map))

	for i in range(0,n):

		complement = target - nums[i]
		index = map.get(complement)

		print("complement : " + str(complement))
		print("index : " + str(index))

		if (complement in map and index != i):
			return [i, index]


nums = [2, 7, 11, 15]

check = sort_hash(nums, 9)
print(check)

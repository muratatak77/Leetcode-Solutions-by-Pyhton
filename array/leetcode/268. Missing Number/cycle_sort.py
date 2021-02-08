def missingNumber(nums):

	n = len(nums)
	dest = 0

	for i in range(0,n):
		print(" i : ", i)
		while nums[i] != i:
			dest = nums[i]
			print("	dest : ", dest)
			if dest<n: # sanity check
				nums[i],nums[dest] = nums[dest],nums[i]
				print("		after swap : ", nums)
			else:
				break #deviant finding
			print("-----------")

	#final scan to find missing item
	print(".....FINAL SCAN TO FIND MISSING")
	for i in range(0,n):
		if nums[i] != i:
			print("We found missing :", i)
			return i

	return n


nums = [3,0,1]
res = missingNumber(nums)
print("res : ", res)

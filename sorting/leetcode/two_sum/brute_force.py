
def two_sum_brute_force(nums, target):
	n = len(nums)
	for i in range(0,n-1):
		for j in range(i+1,n-1):
			if (nums[i] + nums[j] == target):
				return [i,j]


nums = [2, 7, 11, 15]

check = two_sum_brute_force(nums, 19)
print(check)

check = two_sum_brute_force(nums, 9)
print(check)


			
		
	
'''
		We can apply two pointer approach for this question.
		if we don't have a match we update next item index with thr current index item in array-place
		
'''

def remove_element(nums, val):
	key = val
	next_index = 0

	for i in range(len(nums)):
		if nums[i] != key:
			nums[next_index] = nums[i]
			next_index += 1

	return next_index


nums = [3,2,2,3]
val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2


res = remove_element(nums, val)
print("res :" , res)
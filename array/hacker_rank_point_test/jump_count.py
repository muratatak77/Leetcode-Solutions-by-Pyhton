'''
	given an string of numbers or empty string.
	get jump count

	case 1
	# number_of_str = "3,1,0,2"
	start every time from index 0 = 3 

	after 3 position is there any number yes , jump ++ 
		what is the number of after 3 positions = 2
		can we go next more 2 poisition no . Because length of item is not enough

		we can go back 2 item. we have 1. jump ++   ok we go to the right we have 0
		when we get 0 we can return jump count

	
	case 2
	number_of_str = "1,2,0"
	we can start 1. and we can go forward 1 position. jumpcount ++ 
		we have 2 but we don't have either left or right side because of length of array is not enough to next or back moving.
		we can return -1

'''

def get_jump_count(number_of_str):
	
	if not number_of_str:
		return -1
	if len(number_of_str) == 0:
		return -1
	if number_of_str[0] == 0:
		return 1

	arr = number_of_str.split(",")
	for i in range(len(arr)):
		arr[i] = int(arr[i])

	print("arr : ", arr)
	n = len(arr)
	jump_count = 0
	current_item = arr[0]
	curr_idx = 0
	while True:
		print("curr_idx : ", curr_idx)
		print("current_item : ", current_item)

		if curr_idx + arr[curr_idx] + 1 <= n:
			current_item = arr[curr_idx + arr[curr_idx]]
			curr_idx = curr_idx + arr[curr_idx]
			jump_count += 1
		elif curr_idx - arr[curr_idx] > -1:
			current_item = arr[curr_idx - arr[curr_idx]]
			curr_idx = curr_idx - arr[curr_idx]
			jump_count += 1
		else:
			return -1

		if current_item == 0:
			return jump_count

		print("======================")

	return jump_count

number_of_str = "3,1,0,2"
# number_of_str = "1,2,0"
# number_of_str = "1,2,6,9,2,3,5"
res = get_jump_count(number_of_str)
print("res : " , res)






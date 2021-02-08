# Python program to find the smallest 
# window containing 
# all characters of a pattern 
from collections import defaultdict 

# Function to find smallest window 
# containing all distinct characters 
def findSubString(strr): 
	
	n = len(strr) 
	print("N : ", n)
	
	# Count all distinct characters. 
	dist_count = len(set([x for x in strr])) 

	print("dist_count : ", dist_count)
	
	curr_count = defaultdict(lambda: 0) 
	count = 0
	start = 0
	min_len = n 
	
	# Now follow the algorithm discussed in below 
	# post. We basically maintain a window of characters 
	# that contains all characters of given string. 
	for j in range(n): 
		print("-------------------- start j -----------------------")
		print("strr[j] : ", strr[j])
		curr_count[strr[j]] += 1
		print("curr_count: ", curr_count)
		
		# If any distinct character matched, 
		# then increment count 
		if curr_count[strr[j]] == 1: 
			count += 1
			print("count : ", count)
			
		# Try to minimize the window i.e., check if 
		# any character is occurring more no. of times 
		# than its occurrence in pattern, if yes 
		# then remove it from starting and also remove 
		# the useless characters.
		
		if count == dist_count: 
			print(">>>>>>>  start count == dist_count > count : ", count ," dist_count : ",dist_count)
			print("start : ", start)
			while curr_count[strr[start]] > 1: 
				print(" >>> start while : ", strr[start])
				print(" >>> 1 curr_count[strr[start]] : ", curr_count[strr[start]])
				if curr_count[strr[start]] > 1: 
					curr_count[strr[start]] -= 1
				print(" >>> 2 curr_count[strr[start]] : ", curr_count[strr[start]])
				start += 1
			
			print(" >>> 3 curr_count : ", curr_count)

			# Update window size 
			print(" j : " , j , " - start : " , start)
			len_window = j - start + 1
			print("len_window : ", len_window)

			print("min_len : ", min_len)
			if min_len > len_window: 
				min_len = len_window 
				start_index = start 
				print("min_len : ", min_len)
				print("start_index : ", start_index)

	# Return substring starting from start_index 
	# and length min_len """ 
	return str(strr[start_index: start_index + min_len]) 
								
# Driver code 
if __name__=='__main__': 
	res = findSubString("aabcbcdbca")
	print(res)


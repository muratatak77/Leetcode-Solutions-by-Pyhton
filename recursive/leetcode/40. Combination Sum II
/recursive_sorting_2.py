'''
	[2,5,2,1,2]
	
	sorting
	[1,2,2,2,5] 
	 
	1,2,2  - 5
		   root manager 

		1               1
      2   2
    5  

  []   2   2,5
	
	in the leaf workers : 

		1. slate == target . result append
		2. slate > target return 
		3. slate < target contunie

	 in the internal nodes ,, recursive ccase
	

	    root

	2   2,2  2,2,2

'''


def overall(candidates, target):
	result = []
	candidates.sort()
	n = len(candidates)

	def helper(s,i,slate):

		#bactracking case
		if sum(slate) == target:
			result.append(slate[:])
			return 
		elif sum(slate) > target:
			return

		#leaf workers , base case
		if i == n:
			return

		#recursive case , internal nodes
		count = 0
		for index in range(i,n):
			if s[index] != s[i]:
				break
			count += 1

		#exclude case
		# print("exclude case : ", slate)
		helper(s,i+count,slate)

		#include case
		for c in range(1,count+1):
			slate.append(s[i])
			# print("inclide case append slate : " , slate, " - i :", i, " - count : ", count)
			helper(s, i+count, slate)

		for c in range(1,count+1):
			# print("slate pop : ", slate)
			slate.pop()
			
	helper(candidates, 0, [])
	return result



candidates = [2,2,2,1]
target = 6


res = overall(candidates, target)
print("res : ", res)



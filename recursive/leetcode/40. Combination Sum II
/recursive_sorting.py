def overall(candidates, target):
	
	result = []
	n = len(candidates)
	candidates.sort()
	print(candidates)

	def helper(s,i, slate):

		#backtracking case
		sum_slate = sum(slate)
		if sum_slate == target:
			result.append(slate[:])
			return
		elif sum_slate > target:
			return

		#base case
		if i == n:
			return
		
		#recursive case : internal workers
		count=0
		for index in range(i,n):
			if s[index] != s[i]:
				break
			count += 1
	
		#exclude case
		helper(s,i+count,slate)

		#multiway include case
		for c in range(1,count+1):
			slate.append(s[i])
			helper(s, i+count, slate)

		for c in range(1,count+1):
			slate.pop()


	helper(candidates,0, [])
	return result

# candidates  = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
# candidates = [10,1,2,7,6,1,5]
# target = 8

candidates = [2,5,2,1,2]
target = 5

res = overall(candidates, target)
print("res : ", res)




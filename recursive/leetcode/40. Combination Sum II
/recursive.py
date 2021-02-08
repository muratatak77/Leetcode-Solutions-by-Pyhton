def overall(candidates, target):
	
	
	result = []
	n = len(candidates)
	candidates.sort()
	print(candidates)

	def helper(s,i,target,slate):
		#base case : leaf workers
		
		if  s[i] == target:
				result.append(slate[:])
				return

		if i == n:
			return

		for k in range(i,n):
		
			#recursive case : internal workers
			#exclude case
			helper(s,i+1,target,slate)

			#include case
			slate.append(s[i])
			helper(s,i+1,slate)
			slate.pop()


	helper(candidates,0,[])
	return result

# candidates  = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
candidates = [10,1,2,7,6,1,5]
target = 27

print(overall(candidates, target))




# https://leetcode.com/problems/combinations/solution/

def overall(n, k):
	
	result = []

	def helper(first = 1, slate = []):
		#if combination is done
		if len(slate) == k:
			result.append(slate[:])
		# add i into the current combination
		for i in range(first,n+1):
			#use next integers to complete the combination
			slate.append(i)
			helper(i+1,slate)
			slate.pop()

	helper()
	return result

n = 4
k = 2
print(overall(n,k))


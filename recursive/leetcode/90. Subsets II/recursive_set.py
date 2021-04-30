def overall(nums):
	result = []
	n = len(nums)
	hset = set()

	def helper(s,i,slate):
		#base case : leaf worker nodes
		print(hset)
		# 
		if i == n:
			if str(slate[:]) not in hset:
				result.append(slate[:])	
				hset.add(str(slate[:]))
			return
		else:			
			#exclude case
			helper(s,i+1,slate)
			# hset.add(str(slate[:]))

			#include case
			slate.append(s[i])
			helper(s,i+1,slate)
			# hset.add(str(slate[:]))
			slate.pop()

	helper(nums,0,[])
	return result

nums = [1,2,2]
nums = [4,4,4,1,4]
print(overall(nums))
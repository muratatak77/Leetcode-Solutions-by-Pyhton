def overall(nums):
	
	n = len(nums)
	hset = set()
	result = []

	def helper(s,i,slate):
		#base case : leaf workers
		if i == n:
			result.append(slate[:])
			return
		else:
		#recursive case : internal node workers
			for pick in range(i,n):
				if str(slate[:]) in hset:
					continue

				s[pick], s[i] = s[i], s[pick]
				slate.append(s[i])
				helper(s,i+1, slate)
				s[pick], s[i] = s[i], s[pick]
				hset.add(str(slate[:]))
				slate.pop()


	helper(nums,0,[])
	return result

 
nums = [1,1,2]
# nums = [1,2,3]
print(overall(nums))





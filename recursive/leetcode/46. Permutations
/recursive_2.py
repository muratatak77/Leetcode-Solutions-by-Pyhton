'''
return all permutations
we need recursive appoarch in a tree
we have sub problem definition and partial solution
when we reach fully partial solution we will add global result

additionaly , every number item has n times possibility permutations we need iterator 
	inside the iteration we need swap reevant item 
'''


def overall(nums):
	result = []

	def helper(s,i,slate):
		#base case , leaf workers
		if i == len(s):
			result.append(slate[:])
		else:
			for pick in range(i,len(s)):

				s[pick],s[i] = s[i], s[pick] # we need to swap for all permutations in original string like 1,2,3 > 1,3,2
				slate.append(s[i])
				helper(s,i+1, slate)
				slate.pop() # we need pop  return back from subordinates to the manager
				s[pick],s[i] = s[i], s[pick]
			

	helper(nums, 0, [])
	return result

nums = [1,2,3]
res = overall(nums)
print("res : ", res)

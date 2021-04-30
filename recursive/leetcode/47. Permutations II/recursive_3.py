# we can apply sub definition and partial solution tree solution
# we need to a set to avoid repeating

def overall(s):
	result = []
	hset = set()
	n = len(s)

	def helper(s,i,slate):
		#base case, leaf node
		if i == n:
			result.append(slate[:])
			return
		else:

			for pick in range(i, n):

				if str(slate[:]) in hset:
					continue

				s[pick],s[i] = s[i], s[pick]
				slate.append(s[i])
				helper(s, i+1, slate)
				s[pick],s[i] = s[i], s[pick]
				hset.add(slate[:])
				slate.pop()

	helper(s,0,[])
	return result



nums = [1,1,2]
res = overall(nums)
print("res : ", res)

'''
Time complexity : O(N!.N)
space : O(N!.N)
'''

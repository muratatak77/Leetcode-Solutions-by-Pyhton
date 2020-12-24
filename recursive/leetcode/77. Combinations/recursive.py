def overall(n, k):

	result = []
	s = []
	# for i in range(1,n+1):
		# s.append(i)

	def helper(n,i,slate):
		#base case : lead node
		if len(slate) == k:
			result.append(slate[:])
			return
		
		if i == n+1:
			return

		#recursive case : internal nodes
		#exlude side
		helper(n,i+1,slate)

		#include side 
		slate.append(i)
		helper(n,i+1,slate)
		slate.pop()

	helper(n,1,[])
	return result

n = 4
k = 2
print(overall(n,k))


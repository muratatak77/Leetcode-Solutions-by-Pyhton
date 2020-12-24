# https://leetcode.com/problems/permutations/solution/

def overall(s):

	result = []
	n = len(s)
	def helper(first = 0):
		if  first == n:
			result.append(s[:])
		else:
			for i in range(first,n):
				s[first],s[i] = s[i],s[first]
				helper(first+1)
				s[first],s[i] = s[i],s[first]

	helper()
		
	return result


nums = [1,2,3]
print(overall(nums))
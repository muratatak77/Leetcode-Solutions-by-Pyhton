def overall(s):
	result = []
	def helper(s, i):
		#base case: leaf workers
		if  i == len(s):
			result.append(''.join(s)) #mutable version, fresh string creating out of original slate, O(n) 
		else:
			if s[i].isdigit():
				helper(s, i+1)
			else:
				s[i] = s[i].upper()
				helper(s, i+1)

				s[i] = s[i].lower()
				helper(s, i+1)

	helper(list(s), 0)
	return result

s = "a1b2"
res = overall(s)
print(res)

#aux space is better for mutable version. Because we don't create new fresh string in every node.
#space = 
#	input O(n)
#	output = O(2^n x n)
#  			n = length of string
#  			2^n = number of all case variations

#	aux = O(n) much better rather than the immutable version

#Time : O(2^n x n)
# leaf workers : O(2^n x n)
# internal node workers : O(2^n)
# 
# 
# space comp. immutable : O(n^2)
# space comp. mutable : O(n)
# just aux space much better

'''
we need overall and  helper method. helper method is for backtracking. 
we can apply backtrakcing approach. for every each digit makes a combinations other digit.
we need a hash map to lookup that a digit  includes which letters.
	
	helper include a index or starter I can say i

'''
def overall(digits):
	result = []
	hmap = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

	def helper(digits,i,slate):
		#base case, leaf nodes
		if i == len(digits):
			if len(slate)>0:
				result.append("".join(slate)) # slate copy 
				return

		#recursive case, leaf nodes
		else:
			for letter in hmap[digits[i]]:
				slate.append(letter)
				helper(digits,i+1,slate)
				slate.pop()

	helper(digits,0,[])
	return result


digits = "23"
res = overall(digits)
print("res : ", res)

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# time comp  : O(3^N x 4^M)
# space : : O(3^N x 4^M)
# 
# 
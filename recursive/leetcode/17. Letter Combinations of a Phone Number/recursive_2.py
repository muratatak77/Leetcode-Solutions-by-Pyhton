'''
we need overall and  helper method. helper method is for backtracking. 
we can apply backtrakcing approach. for every each digit makes a combinations other digit.
we need a hash map to lookup that a digit  includes which letters.
	
	like : '23'
	we can start to iterate first digit is 2. 2 is corresponding [a,b,c]
	and other digit is 3 : [d,e,f]

	for every 2 digit chars we can compare combine every next digit chars.

				
	slate = []	 		a 					b 					c
		
	slate = [a]		d 	e 	f 			d 	e  f   >> recursive case 

	slate = [ad]   ad   ae  af   >> base case, leaf node

	



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

	def helper(i, slate):
		#base case, leaf node
		if i == len(digits):
			result.append("".join(slate[:]))
			return
		else:
			#recursive case
			for letter in hmap[digits[i]]:
				slate.append(letter)
				helper(i+1, slate)
				slate.pop()

	helper(0,[])
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
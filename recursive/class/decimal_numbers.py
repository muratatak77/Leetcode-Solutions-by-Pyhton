result = []
def overall(n):
	return  helper(n,0,"")

def helper(n,i,slate):

	#s,i  = sub problem defination
	#slate = partial solution
	#base case, leaf level
	if i == n:
		return result

	result.append(slate)
	helper(n,i+1, n)
	

n = 99
res = overall(n)
print(res)



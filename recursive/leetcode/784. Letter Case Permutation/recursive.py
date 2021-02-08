result = []
def overall(s):
	return  helper(s,0,"")

def helper(s,i,slate):

	#s,i  = sub problem defination
	#slate = partial solution
	#base case, leaf level
	if i == len(s):
		result.append(slate)
		return

	#recursive case, internal node
	else:
		if s[i].isdigit():
			helper(s,i+1, slate+s[i])
		else:
			helper(s,i+1, slate+s[i].lower())
			helper(s,i+1, slate+s[i].upper())

	return result

s = "a1b2"
res = overall(s)
print(res)



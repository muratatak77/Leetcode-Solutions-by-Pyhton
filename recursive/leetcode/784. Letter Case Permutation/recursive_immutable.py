
#
#
##we have a general template 
#This is a filling the blanks problem , preserving original order, 
#
#1 - partial solution = slate = every worker has a job that is to fill most left blank finally this slate will be fill all chars
#2 - sub problem definition = s,i = it needs to delegate filling the blank
#    and whetever go, stop sub problem definition. 
#    
#    what is the next job for next subordinate.
#
#overall function : 
#  subproblem size is the entire string and the partial solution is empty

def overall(s):
	result = []

	def helper(s,i, slate):
		#base case : leaf worker
		#if sub problem definition is empty or partial solution is complete combinatorial object (Perm. / Comb.)
		if i == len(s):
			# master copy from original string # immutable version, we can't change string we need to add 
			result.append(slate) 
			return
		else:
		#recursive case : internal Node
			if s[i].isdigit():
				helper(s,i+1,slate+s[i])
			else:
				helper(s,i+1,slate+s[i].lower()) # string concatenation immutable version. we create a new string we can't change original string
				helper(s,i+1,slate+s[i].upper())
	
	helper(s,0,"")
	return result


s = "a1b2"
res = overall(s)
print(res)



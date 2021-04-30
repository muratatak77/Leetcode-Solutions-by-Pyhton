def overall(s):

	result = []

	def helper(s,i,slate):
		print("after helper   :  i : ", i , ", slate : ", slate )
		if  i == len(s):
			result.append(slate[:])
			print("return after helper   :  i : ", i , ", slate : ", slate )
			print("===========================")
			return
		else:
			print("	before i : ", i)			
			for pick in range(i,len(s)):

				print("		inside i         : ", i , "     , pick :", pick)
				s[pick],s[i] = s[i],s[pick]
				print("		1 - swap s :" , s)
				slate.append(s[i])
				print("		before helper  :  i : ", i , ", slate : ", slate )
				helper(s,i+1,slate)
				slate.pop()
				print("		slate pop :" , slate, "  - i : ", i, " -  s : ", s, " - pick : ", pick)
				s[pick],s[i] = s[i],s[pick]
				print("		2 - swap s :" , s, " - slate : ", slate, " - pick : ", pick)
				print("--------------")


	helper(s,0,[])			
	return result


nums = [1,2,3]
print(overall(nums))
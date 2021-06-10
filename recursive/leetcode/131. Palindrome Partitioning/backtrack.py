'''
we can apply partial solution and sub definition approach
we need to walk trough for every part char with together a substring input

		    aab
      a      aa       aab
    a   ab    b   
  b  

result [a,a,b] 
result [aa,b]

 - we need a is palindrom function

'''

def overall(s):
	result = []

	def ispalindrome(slate):
		return slate == slate[::-1]

	def helper(s,i,slate):
		print("start helper i :", i , " - slate : ", slate)
		#backtracing case
		# if len(slate) > 0 and not ispalindrome(slate[-1]):
			# print("   is not palindrom : ", slate[-1])
			# return 

		#base case
		if i == len(s):
			print( " 				result append : " , slate[:])
			result.append(slate[:])
			return

		#recursive case
		for pick in range(i,len(s)):
			#append s[i..pick]
			print("recursice case - i :" , i, " - pick :", pick)
			print("slate append : ", s[i:pick+1])
			if ispalindrome(s[i:pick+1]):
				slate.append(s[i:pick+1])
				print("  call helper : slate : ", slate, " i : ", i)
				helper(s,pick+1,slate)
				print("     slate pop     ")
				slate.pop()
				print("     after pop slate :  ", slate)
			print("-------------------------------")

	helper(s,0,[])
	return result


s = "aab"
res = overall(s)
print("res : ", res)


'''
	T(N)  = O(2^N. N )   N is the length of string, this is worst case time complexity when all the possible substring are palindrome

	N = 3 Total nodes =will be 8. 2^N

	S(N) = O(N)

'''
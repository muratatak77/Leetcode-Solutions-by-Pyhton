class Solution:
	def myAtoi(self, s: str) -> int:
		print("Inital S:",s)

		# 1.Read in and ignore any leading whitespace.
		#check if there are spaces in the head of string
		while s and s[0] == ' ':
			s = s[1:]

		print("after clean first space S:",s)

		#edge case
		#if there is no string we can return 0
		if not s:
			return 0
		
		#Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
		newstring = s
		for i , j in enumerate(s):
			print("	i : ", i,  " - j :", j)
			#i == 0 we need to check first char, becase would be - or + and we can ignore first char
			if i == 0:
				continue
			elif j == ' ' or j =='.' or j not in '1234567890':
				newstring = s[:i]
				print("		generated newstring : ", newstring)
				break
		 
		print("	2. newstring : ", newstring)
	
		if len(newstring) > 1 and newstring[1] not in '1234567890':
			return 0

		if s[0] not in '-+ 1234567890':
			return 0


		#if our initial input would be +-12 , in this point, we get the just + char. we need to check what are gonna happen if we convert int 
		try:
			int(newstring)
		except ValueError:
			return 0 

		if int(newstring) < -2147483648:
			return -2147483648
		
		if int(newstring) > 2147483647:
			return 2147483647
			
			
		return int(newstring)


s = " 42"
s = "4193 with words"
s = "-91283472332"
s = "+-12"
s = "words and 987"

res = Solution().myAtoi(s)
print("res : ", res)
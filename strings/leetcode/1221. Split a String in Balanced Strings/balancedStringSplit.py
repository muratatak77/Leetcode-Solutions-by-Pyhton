class Solution:
	def balancedStringSplit(self, s: str) -> int:
		stack=[s[0]]
		c=0
		
		for i in range(1,len(s)):
			print("stack : ", stack)
			if(stack==[]):
				c=c+1
				stack.append(s[i])
				print("		Append stack : ", stack, " - c :", c)
			
			else:
				if(stack[-1]!=s[i]):
					stack.pop(-1)
				else:
					stack.append(s[i])
		
		return(c+1)


s = "RLRRLLRLRL"
s = "RLRRLLRLRL"
# s = "RLLLLRRRLR"
res = Solution().balancedStringSplit(s)
print("res : ", res)
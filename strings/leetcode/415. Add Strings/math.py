class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		res = []

		carry = 0
		p1 = len(num1) - 1
		p2 = len(num2) - 1
		while p1 >= 0 or p2 >= 0:
			
			if p1 >= 0:
				#Set x1 to be equal to a digit from string nums1 at index p1
				x1 = ord(num1[p1]) - ord('0')
			else: 
				x1 = 0
			print("	x1 : ", x1)
			if p2 >= 0:
				x2 = ord(num2[p2]) - ord('0')
			else:
				x2 = 0
			print("	x2 : ", x2)

			value = (x1 + x2 + carry) % 10
			print("		value : ", value)

			carry = (x1 + x2 + carry) // 10
			print("		carry : ", carry)

			res.append(value)
			p1 -= 1
			p2 -= 1
			print("----------------------")
		
		if carry:
			res.append(carry)

		return ''.join(str(x) for x in res[::-1])



num1 = '1789'
num2 = '15'
res = Solution().addStrings(num1,num2)
print("res : ", res)

'''
	T(N) = O(Max(N1,N2)) N1 and N2 is strings. We got finally max(n1,n2)
	S(N) = O(Max(N1,N2)) because length of the string is at most max(N1,N2)
'''
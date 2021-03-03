class Solution:
	def addBinary(self, a, b) -> str:
		
		# we need to fill by 0, if we have space
		# thats way we need max size of binary string 
		n = max(len(a), len(b))
		a = a.zfill(n)
		b = b.zfill(n)

		carry = 0
		answer = []
		for i in range(n-1,-1,-1):

			#if we have 1 we can increment carry +1
			if a[i] == '1':
				carry += 1
			if b[i] == '1':
				carry += 1

			if carry % 2 == 1:
				answer.append('1')
			else:
				answer.append('0')

			carry //= 2

		
		if carry == 1:
			answer.append('1')
		answer.reverse()

		return ''.join(answer)


a = "11"
b = "1"

a = "111"
b = "101"
res = Solution().addBinary(a, b)
print("res :", res)

'''
	T(N) = O(Max(N,M)) 
			N = size of a , M = size of b. what is the largest size of any binary string.
	S(N) = O(Max(N,M))
'''
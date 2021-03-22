'''
	We can apply some math operations.
	like  :
		
 		
 		Our formula : 
 			x ^ {a + b} = x ^ a * x ^ b

		we can say :

		2^4 == 2^2 * 2^2

		actually same thing so we can seperate n items. Everytime we can divide 2 along the iterate n > 0 times.
		We don't need n times iterate. 

		2^4 = 2.2.2.2


		but we need to check n % 2 == 1 
		in this case 

			2^3 = 2.2.2   divided 2 remain is will be 1. 

			in this case we can multiply a global ans. 
				ans = ans * x

'''
class Solution:
	def myPow(self, x: float, n: int) -> float:

		if n == 0:
			return 1
		
		if n == 1:
			return x

		if n < 0:
			x = 1/x
			n = -n

		ans = 1
		while n>0:
			if n%2 == 1:
				ans = ans * x
			x = x*x
			n //= 2

		return ans



x = 2
n = 7

# x = 2.10000
# n = 3

# x = 2.00000
# n = -2


res = Solution().myPow(x, n)
print("res :", res)

'''
	T(N) = O(Logn) For each bit ob n's binary represantation
	S(N) = O(1)
'''
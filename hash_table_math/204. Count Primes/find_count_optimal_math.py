'''
	if we find non prime numbers until the n, after we will be find prime numbers optimal way.

	Step 1:
		get non prime numbers until the n

		get sqrt from n:
			Explanation : https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-prime-number-to-determine-if-it-is-pr

			1- If a number n is not prime, it can be factored into two factors a and b
				n = a*b
				Now a and b can't be both grater than the squaare root of n, since then the product a*b would be grater than sqrt(n)*sqrt(n) = n.
				So in any factorization of n, at least one of the factors must be smaller than the square root of n, and if we can't find
				any factors less than or equal to the square root, n must be a prime.
			
		we can keep an extra array to follow 0 to n like array.
		
		n = 5
		ary = [0,0,0,0,0]

		first 0 and 1 will be 1.
		arr = [1,1,0,0,0]

		and we can sqrt of 7

		we can apply an iterative  to the sqrt(n)
		i and j start   every time 2

		if (i*j) < n 
			means i and j are not prime numbers.
			arr[i*j] will not be prime numbers.

		

'''
import math

class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n < 3:
			return 0
		
		arr = [0] * n
		arr[0] = 1
		arr[1] = 1
		
		print("ARRAY initial : ", arr)

		sqrt = int(math.sqrt(n))
		print("sqrt : ", sqrt)

		for i in range(2, sqrt+1):
			print("   i :", i)
			j = 2
			while (i*j) < n:
				print("		(i*j) : ", (i*j))
				arr[i*j] = 1
				j += 1
			print("		J : ", j)
		print("---------------------")

		print("arr finished : ", arr)

				
		return len([num for num in arr if num == 0])


n = 10
res = Solution().countPrimes(n)
print("res : ", res)
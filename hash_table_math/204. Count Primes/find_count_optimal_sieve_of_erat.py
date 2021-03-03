'''
Sieve Of eratosthenes

  - Assume all prime from 2 to n
  - Generate and eliminate composite numbers
  - Count remaning primes


  lets start 2


	      False
  i  j
  2 | 2*2 = 4 generate 4 and 6,8,810,12 ..| n
  3 | 9,12,15..  
  4 | we already eliminate 4 first check
  5 | 25,60 ....

	we will check i is less than and equal the n. Because we are eliminating non primes 
	checking by square number. larger than n we don't care.

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
		
		primes = [1] * n

		i = 2
		while i*i < len(primes):
			if primes[i]:
				j = i
				while j*i < len(primes):
					primes[j*i] = 0
					j += 1
			i+=1

		prime_count = 0
		for i in range(2,len(primes)):
			if primes[i]:
				prime_count += 1

		return prime_count

n = 10
res = Solution().countPrimes(n)
print("res : ", res)
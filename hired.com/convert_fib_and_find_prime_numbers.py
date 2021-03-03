def findPrimeNumbers(n):

	#first step - find fibonacci number start 1 to the until the n 
	if n <= 0:
		return 0

	fibo = [0]*(n+1)
	fibo[1] = 1

	for i in range(2,n+1):
		fibo[i] = fibo[i-1] + fibo[i-2]

	print("fibo : ", fibo)

	#second step - find prime numbers
	#like  = 5 
	#5 % 2 != 0  
	#5 % 3 != 0
	#5 % 4 != 0
	# so 5 is a prime numbers.
	
	primes = []
	for num in fibo:

		if num > 1:
			if num == 2:
				primes.append(2)
				continue

			for i in range(2,num):
				if num % i == 0:
					break
			else:
				primes.append(num)

	return primes

n = 50
res = findPrimeNumbers(n)
print("res : ", res)

'''

'''
# Python 3 program for checking of
# Narcissistic number

# function to count digits
def countDigit(n) :
	print(" n : ", n)
	if (n == 0) :
		return 0
	print("		countDigit(n // 10) : ", (n // 10))

	return (1 + countDigit(n // 10) )

	

# Returns true if n is Narcissistic number
def check(n) :
	
	# Count the number of digits
	l = countDigit(n)

	print(" L : ", l)

	dup = n; sm = 0



	# Calculates the sum of digits
	# raised to power
	while (dup) :
		print("			dup : ", dup)
		print("			dup % 10 : ", dup % 10)
		sm = sm + pow(dup % 10, l)
		print("sm : ", sm)
		dup = dup // 10
	
	return (n == sm)
	

# Driver code
n = 1634
if (check(n)) :
	print( "yes")
else :
	print( "no")
	
	

# This code is contributed by Nikita Tiwari.

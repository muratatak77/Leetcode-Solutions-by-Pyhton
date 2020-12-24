'''
	football 
	each play can lead 2,3 or 7 points.
	
	if we are given some score of p find out 2,3 and 7 
	
	how many diff perm 
	
	p = 7
	
	perm count = 4 
	
	
	7
	
	2+3+2
	
	3+2+2
	
	2+2+3
	
	---------
	
	
	
			2                       3                  7
	 2      3       7        2      3    7            (7) 
   3   7   2   3           2   3    x    x
  (7)  x   (7) x          (7)  x 
  
	
'''  

def combinationSum(numbers, target):

	if target == 0:
		return 1  # base case

	count = 0

	for number in numbers:
		if number <= target:
			count += combinationSum(numbers, target - number)

	return count



points = [7,3,2]
target = 29 

# points = []
# target = 4

res = combinationSum(points, target)
print("res : ", res)
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

def overall(nums, target):
	
	if len(nums) > 5:
		return 0

	hset = set()
	nums.sort()
	n = len(nums)
	count = 0
	result =[]

	def helper(num,remain,slate):

		nonlocal count
		# print("main num : ", num)
		# print("main remain : ", remain)
		# print("main slate : ", slate)
		# print("main hset : ", hset)
		# print("main count : ", count)
		# print("=====================")

		if remain == 0:
			if not str(slate[:]) in hset:
				count += 1
				result.append(slate[:])
				# print("		BINGO : ", count, " - slate : ", slate)
			return
		elif remain < 0:
			return

		else:
			for num2 in nums:
				
				if str(slate[:]) in hset:
					# print("		we have slate in hset : ", slate)
					continue

				if num2 <= target:
					slate.append(num2)
					helper(num2,remain - num2, slate)
					hset.add(str(slate[:]))
					slate.pop()


	for num in nums:
		helper(num,target,[])

	# print("RESULT : ", result)
	return count


points = [7,3,2]
target = 10

# points = [1,2,3]
# target = 4

res = overall(points, target)
print("res : ", res)
#
# Complete the merger_first_into_second function below.
#
def merger_first_into_second(arr1, arr2):
	#
	# Write your code here.
	#

	p1 = len(arr1)-1
	p2 = len(arr2) - p1 - 2
	p = len(arr2) - 1

	# print("p1 : ", p1)
	# print("p2 : ", p2)
	# print("p : ", p)
	
	while p1 >= 0 and p2 >= 0:
		
		if arr2[p2] < arr1[p1]:
			arr2[p] = arr1[p1]
			p1 -= 1
		else:
			arr2[p] = arr2[p2]
			p2 -= 1

		p -= 1

	arr2[:p1+1] = arr1[:p1+1]

	return arr2

			
			
arr1 = [1,3,5]
arr2 = [2,4,6,0,0,0]


arr1 = [1,1,1,1,1,1]
arr2 = [1,1,1,1,1,2,0,0,0,0,0,0]


res =  merger_first_into_second(arr1, arr2)
print(res)
'''
we can apply sub definition and partial solution recursive approach 
we will have root manager and this root manager will delegate sub ordinates, These sub ordinates will delegate other subordinates in a tree.
finally when we reach leaf nodes , we will be add  result global array
I will work trough exclude and include  for each number

				_ _ _ 
	
		{}_ _					{1} _ _

	{} _ 	 		{2} _

{}		{3}		{2}		{2,3}


'''

def overall(nums):

	result = []

	def helper(s,i, slate):
		# base case , leaf workers 
		if i == len(s):
			result.append(slate[:]) # copy / clone add
		else:

			#recurvise case , internal nodes
			# exclude side 
			helper(s, i+1, slate)

			#include case
			slate.append(s[i])
			helper(s, i+1, slate)
			slate.pop()

	helper(nums,0,[])
	return result


nums = [1,2,3]
res = overall(nums)
print("res : ", res)


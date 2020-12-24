from collections import defaultdict

def diagonalMerge(nums):
	
	hmap = defaultdict(list)
	
	for i in range(len(nums)):
		print("start i : ", i , " >>>>>>>>>>>> ")
		for j in range(len(nums[i])):
			print(" i : ", i, " / j : ", j)
			hmap[i+j].append(nums[i][j])
			print("   Added hmap . key = ", i+j, ".append(", nums[i][j] ,")")
	
	res = []
	for k in hmap.keys():
		for v in reversed(hmap[k]):
			res.append(v)

	return res
	
nums = [[1,2,3],[4,5,6],[7,8,9]]
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
nums = [[5,6,3,10],[9],[1,19],[9,9,2]]

res = diagonalMerge(nums)
print("res :", res)

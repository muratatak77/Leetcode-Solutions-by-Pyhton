from collections import defaultdict
from collections import deque

def diagonalMerge(nums):
	
	d = defaultdict(deque)

	for r_idx, row in enumerate(nums):
		for c_idx, col in enumerate(row):
			d[r_idx+c_idx].appendleft(col)

	res = []
	for v in d.values():
		for e in v:
			res.append(e)
			
	return res


nums = [[1,2,3],[4,5,6],[7,8,9]]
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
nums = [[5,6,3,10],[9],[1,19],[9,9,2]]

res = diagonalMerge(nums)
print("res :", res)

'''
	DFS - recursion approaching

			1
		2     
	4		5

	1+2+4 = 
	1+2+5 = 
	...

	BFS is not suitable for this question. We don't need keep evel by level traversal

'''

class TreeNode():

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		

def dfs(node, remain):

	if not node:
		return False

	remain -= node.val

	#base case : leaf nodes
	if not node.left and  not node.right  and remain == 0:
		return True

	#recursive case : internal nodes
	return dfs(node.left, remain) or dfs(node.right, remain)


node = TreeNode(5)
node.left = TreeNode(4)
node.left.left = TreeNode(11)
node.left.left.right = TreeNode(2)
node.left.left.left = TreeNode(7)
node.right = TreeNode(8)

sum = 22
res = dfs(node, sum)
print("res :", res)


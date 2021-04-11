class TreeNode():
	"""docstring for TreeNode"""
	def __init__(self, val):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None

def pathSum(root, sum):
	if not root:
		return []
	result = []

	def dfs(root, target, slate):
		
		#base case, leaf workers
		if not root.left and not root.right:
			if target == root.val:
				slate.append(root.val)
				result.append(slate[:])
				slate.pop()

		#recursice case, internal nodes
		slate.append(root.val)
		if root.left:
			dfs(root.left, target - root.val, slate)
		if root.right:
			dfs(root.right, target - root.val, slate)
		slate.pop()
		print("slate : ", slate)


	dfs(root, sum, [])
	return result

node = TreeNode(5)
node.left = TreeNode(4)
node.left.left = TreeNode(11)
node.left.left.left = TreeNode(7)
node.left.left.right = TreeNode(2)

node.right = TreeNode(8)
node.right.left = TreeNode(13)
node.right.right = TreeNode(4)
node.right.right.right = TreeNode(1)
node.right.right.left = TreeNode(5)

sum = 22
result = pathSum(node, sum)
print(result)


'''
Time compl :  N = scan every each node  and append to the global bax : log N. = T(N LogN)
Space compl : O(NLogn)
'''
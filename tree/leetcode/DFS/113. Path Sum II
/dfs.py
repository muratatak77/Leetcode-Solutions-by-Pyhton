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


	def dfs(node, target, slate):
		#base case : leaf worker 
		if not node.left and not node.right:
			if target == node.val:
				slate.append(node.val)
				result.append(slate[:])
				slate.pop()
		
		#recursive case : internal node
		slate.append(node.val)
		if node.left:
			dfs(node.left, target - node.val, slate)
		if node.right:
			dfs(node.right, target - node.val, slate)
		slate.pop()

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
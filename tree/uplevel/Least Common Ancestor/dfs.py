#doesnt work every case
class TreeNode():
	"""docstring for TreeNode"""
	def __init__(self, val):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None


def leastCommonAncestor(root, p, q):
	
	if not root:
		return None

	def dfs(node):
		print("node : ", node.__dict__)
		#base case : leaf workers
		if not node.left  and not node.right:
			if node.val == p or node.val == q:
				return True
			else:
				return False

		#recursive  case :
		bl , br = None, None
		if node.left:
			bl = dfs(node.left)
			print("bl : ", bl)
			if (node.val == p or node.val == q):
				return True

		if node.right:
			br = dfs(node.right)
			print("br : ", br)
			if (node.val == p or node.val == q):
				return True

		if bl and br:
			return node

		return br or bl

	return dfs(root)
		


node = TreeNode(1)
node.left =  TreeNode(2)
node.left.left = TreeNode(4)

node.left.right = TreeNode(5)

node.left.left.left = TreeNode(8)
node.left.left.right = TreeNode(9)

node.left.right.left = TreeNode(10)
node.left.right.right = TreeNode(11)


p = 9
q = 10
res = leastCommonAncestor(node, p, q)
print(res.__dict__)







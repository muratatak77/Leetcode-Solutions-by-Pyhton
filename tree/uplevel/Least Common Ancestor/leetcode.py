#doesnt work every case

class TreeNode():
	"""docstring for TreeNode"""
	def __init__(self, val):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None


class Solution:

	def __init__(self):
		# Variable to store LCA node.
		self.ans = None

	def lowestCommonAncestor(self, root, p, q):

		if not root:
			return

		def dfs(node):

			if not node:
				return False

			#left recursive
			left = dfs(node.left)
			print("left : ", left)
			#rigt recursive
			right = dfs(node.right)
			print("right : ", right)

			# if the current node is one of p or q
			mid = node == p or node == q
			print(mid)

			#if any two or three flags left, right or mid becomes True
			if mid + left + right >= 2:
				self.ans = node

			#return True if either of the three bool values is True
			return mid or left or right


		dfs(root)
		return self.ans




node = TreeNode(1)
node.left =  TreeNode(2)
node.left.left = TreeNode(4)

node.left.right = TreeNode(5)

node.left.left.left = TreeNode(8)
node.left.left.right = TreeNode(9)

node.left.right.left = TreeNode(10)
node.left.right.right = TreeNode(11)


p = node.left.left
q = node.left.right

res = Solution().lowestCommonAncestor(node, p, q)
print(res.__dict__)





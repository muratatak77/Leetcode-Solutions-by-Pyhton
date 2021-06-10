class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		

class Solution(object):
	def __init__(self):
		self.ans = None
			
	def lowestCommonAncestor(self, root, p, q):

		def helper(curr_node):
			
			if not curr_node:
				return False

			left  = helper(curr_node.left)
			right  = helper(curr_node.right)

			mid = curr_node == p or curr_node == q

			if mid + left + right >= 2:
				self.ans = curr_node

			return mid or left or right

		helper(root)
		return self.ans
	


node = TreeNode(1)
node.left = TreeNode(2)

node.left.left = TreeNode(4) 
node.left.right = TreeNode(5) 

node.left.left.left = TreeNode(8) 
node.left.left.right = TreeNode(9) 

node.left.right.left = TreeNode(10) 
node.left.right.right = TreeNode(11) 

p = node.left.left.right
q = node.left.right.right

res = Solution().lowestCommonAncestor(node, p, q)
print("res :", res.val)



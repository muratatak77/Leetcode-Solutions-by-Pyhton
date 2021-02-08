class TreeNode():
	"""docstring for TreeNode"""
	def __init__(self, val):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None

class Solution:
	def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
		
		if not root or not root.left:
			return root
		
		true_root = self.upsideDownBinaryTree(root.left)
		print("true_root val : ", true_root.val)

		# print("root val :",root.val)
		print("root : ", root.val)
		print("root.left : ", root.left.val)
		print("root.right : ", root.right.val)

		root.left.left=root.right
		root.left.right=root
		root.left=None
		root.right=None
		print("return true_root : ", true_root.val)
		print("================")
		return true_root

def printNode(root):
	if root:
		print(root.val)
		printNode(root.left)
		printNode(root.right)

node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)

# node.left.left.left = TreeNode(7)
# node.left.left.right = TreeNode(2)

node.right = TreeNode(3)
# node.right.left = TreeNode(13)
# node.right.right = TreeNode(4)
# node.right.right.right = TreeNode(1)
# node.right.right.left = TreeNode(5)

res = Solution().upsideDownBinaryTree(node)
print("result : ", res)

printNode(res)

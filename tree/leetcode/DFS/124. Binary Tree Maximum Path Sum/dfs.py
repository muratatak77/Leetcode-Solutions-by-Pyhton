class TreeNode():
	"""docstring for TreeNode"""
	def __init__(self, val):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None


class Solution:

	def maxPathSum(self, root: TreeNode) -> int:

		def helper(node):
			nonlocal globalSum

			if not node:
				return 0

			left = helper(node.left)
			right = helper(node.right)

			# print("globalSum : ", globalSum)

			sumUsableByParent = max(node.val, node.val + left, node.val + right)  # 3 paths
			print("sumUsableByParent : ", sumUsableByParent)
			print("node.val + left + right : " , node.val + left + right, " - left : ", left , " - right : ", right , " - node.val : ", node.val)

			globalSum = max(globalSum, sumUsableByParent, node.val + left + right)  # 4 paths

			print("globalSum : ", globalSum, " - sumUsableByParent : ", sumUsableByParent , " - node.val : ", node.val, " - left :", left , " - right :" , right)
			print("======== ======= ======= ======= ======")
			return sumUsableByParent

		globalSum = float('-inf')
		helper(root)
		return globalSum



node = TreeNode(-10)
node.left = TreeNode(9)
# node.left.left = TreeNode(11)
# node.left.right = TreeNode(3)
# node.left.left.left = TreeNode(7)
# node.left.left.right = TreeNode(2)

node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
# node.right.right.right = TreeNode(1)
# node.right.right.left = TreeNode(5)

result = Solution().maxPathSum(node)
print(result)

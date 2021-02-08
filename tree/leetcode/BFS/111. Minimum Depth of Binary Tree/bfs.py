class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

from collections import deque
class Solution(object):
	def minDepth(self, root):

		if not root:
			return 0

		q = deque([root])
		level = 0

		while q:
			level += 1
			for _ in range(len(q)):
				node = q.popleft()

				if node.left:
					q.append(node.left)

				if node.right:
					q.append(node.right)
				
				if node.left is None and node.right is None:
					return level

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

res = Solution().minDepth(tree)
print("res : ", res)


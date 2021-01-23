from collections import deque
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isUnivalTree(self, root: TreeNode) -> bool:
		if not root:
			return False
		
		q = deque([root])
		unival = root.val
		while q:
			for _ in range(len(q)):
				node = q.popleft()
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
				if node.val != unival:
					return False
		return True


root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)

res = Solution().isUnivalTree(root)
print("res : ", res)



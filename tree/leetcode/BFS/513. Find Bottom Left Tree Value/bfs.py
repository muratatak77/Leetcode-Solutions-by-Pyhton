'''
	We can apply BFS - level by level order traversal. 
	We need a deque in BFS approach
	In every level first node is our left most node.
	We can keep a first_val param, we can set null value for every level startting. 
	And if this first val is None we can set node val. 

'''
# Definition for a binary tree node.
from collections import deque
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	def findBottomLeftValue(self, root: TreeNode) -> int:
		if not root:
			return 0

		q = deque([root])
		while q:
			first_val = None
			for _ in range(len(q)):
				node = q.popleft()
				if first_val is None:
					first_val = node.val
				if node.left is not None:
					q.append(node.left)
				if node.right is not None:
					q.append(node.right)
		return first_val


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)

root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.right = TreeNode(7)


res = Solution().findBottomLeftValue(root)
print("res : ", res)

'''
	T(N) = O(N) N is root numbers
	S(N) = O(N) Q visit for every node
'''

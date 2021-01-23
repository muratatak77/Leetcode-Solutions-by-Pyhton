from collections import deque
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
		
		if p is None and q is None:
			return True

		if (p is None and q is not None) or (p is not None and q is None):
			return False

		def check(p, q):
			# if both are None
			if not p and not q:
				return True
			# one of p and q is None
			if not q or not p:
				return False
			if p.val != q.val:
				return False
			return True

		deq = deque([(p,q)])
		while deq:
			for _ in range(len(deq)):
				p, q = deq.popleft()
				if not check(p,q):
					return False
					
				if p:
					deq.append((p.left, q.left))
					deq.append((p.right, q.right))

		return True


p = TreeNode(1)
# p.left = TreeNode(None)
# p.right = TreeNode(2)

q = TreeNode(1)
# q.left = TreeNode(2)
q.right = TreeNode(3)

res = Solution().isSameTree(p,q)
print("res : ", res)
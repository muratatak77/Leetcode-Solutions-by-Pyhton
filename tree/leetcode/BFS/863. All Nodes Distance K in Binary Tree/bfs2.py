from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def distanceK(self, root, target, K):
		visited = set()
		res = []
		parent = {}
		self.findParent(root, parent)
		self.helper(target, K, visited, parent, res)
		return res
		
	def findParent(self, node, parent):
		if not node:
			return 
		if node.left:
			parent[node.left] = node
		if node.right:
			parent[node.right] = node
		self.findParent(node.left, parent)
		self.findParent(node.right, parent)
		
	def helper(self, node, k, visited, parent, res):


		print("node : ", node)

		if node in visited:
			return
		if k == 0:
			res.append(node.val)
			return
		visited.add(node)
		if node.left:
			self.helper(node.left, k-1, visited, parent, res)
		if node.right:
			self.helper(node.right, k-1, visited, parent, res)    
		if node in parent:
			self.helper(parent[node], k-1, visited, parent, res)



node  = TreeNode(3)
node.left = TreeNode(5)
node.left.left  = TreeNode(6)
node.left.right  = TreeNode(2)
node.left.right.left  = TreeNode(7)
node.left.right.right  = TreeNode(4)

node.right = TreeNode(1)
node.right.left = TreeNode(0)
node.right.right = TreeNode(8)

target = node.left
K = 2
res = Solution().distanceK(node, target, K)
print("res :", res)  
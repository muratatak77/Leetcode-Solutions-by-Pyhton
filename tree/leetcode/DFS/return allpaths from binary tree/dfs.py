# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def allPathsFromBT(self, root):
		
		if not root:
			return []

		result = []

		def dfs(node, slate):

			#base case: lead nodes
			slate.append(node.val)
			if not node.left and not node.right:
				#we should add copy of mater slate. 
				#copy of slate = slate[:]
				#we need a copy of slate.
				#otherwise we can add reference of master slave. 
				#Eventually , we will be bunch of empty list.
				result.append(slate[:])
				#we can not return anything because it  will be effects recursive case

			#recursive case: internal nodes
			if node.left:
				dfs(node.left, slate)
			if node.right:
				dfs(node.right, slate)

			#we need to pop from our slate because of we added all path 
			#and we need extract one item from slate.
			slate.pop()
			
		dfs(root, [])
		return result


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4) 
node.left.right = TreeNode(5) 

res = Solution().allPathsFromBT(node)
print("res : ", res)



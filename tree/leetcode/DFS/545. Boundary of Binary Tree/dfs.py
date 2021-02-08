'''
	
				   1
		  2					3
	  4	    5			 6		
		  7	  8	  	   9	10


	We can apply 3 parts solution for this problem.
	First part : 
		leftboundry = []
		we can get and keep an array just left most nodes in the Tree expect last node.
		Last node is a leaf node. We will get in the final step all leaves nodes.
		leftboundry = [1,2]

	Second part:
		
		rightboundry = []
		we can get and keep an array just right most nodes in the Tree expect last right most node.
		last node is a leaf node. We will get in the final step all leaves nodes.
		And we need to reverse array data structer. 
		rightboundry = [3,6]

	Thirt part:
		
		We can get just leaves node. 
		We can use DFS approach to get leaves node easly.
		Because we need just leaves nodes. Top-Down approach works in this case.
		leaves = [4,7,8,9,10]

	Final :

		return leftboundry + leaves + right_boundry


'''

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution(object):
	def boundaryOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""

		if root is None:
			return []

		if root.left is None and root.right is None:
			return [root.val]

		leftboundry = [root.val]

		if root.left is not None:
			curr = root.left
			while curr is not None:
				leftboundry.append(curr.val)
				if curr.left is not None:
					curr = curr.left
				else:
					curr = curr.right
			leftboundry.pop() #	Last node is a leaf node. We will get in the final step all leaves nodes.


		rightboundry = []

		if root.right is not None:
			curr = root.right
			while curr is not None:
				rightboundry.append(curr.val)
				if curr.right:
					curr = curr.right
				else:
					curr = curr.left
			rightboundry.pop() # Last node is a leaf node. We will get in the final step all leaves nodes.

		rightboundry.reverse()

		leaves = []
		def dfs(node):
			#leaf case
			if node.left is None and node.right is None:
				leaves.append(node.val)

			#recursive case
			if node.left is not None:
				dfs(node.left)
			if node.right is not None:
				dfs(node.right)
		dfs(root)
		
		return leftboundry + leaves + rightboundry


node = TreeNode(1)
node.right = TreeNode(2)

node.right.left = TreeNode(3) 
node.right.right = TreeNode(4) 

result = Solution().boundaryOfBinaryTree(node)
print(result)




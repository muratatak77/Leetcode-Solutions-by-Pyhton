'''
	We can apply Top- Down DFS approacing.
	
	First each node check left and right node. 

		1
	2		3
4		5

	we can separate to the 3 parts while doing the solution

	when we reach leaf node 4 , we can do it left and right :

		in process case  :
			we can say current node will be old left and old right child

			old_left = node.left
			node.left = right sibling of node
			node.right = parent

			that's why we need every recursive case parent and right_sibling params

		in leaf case : 

			our root will be 4

		in recussive case :
			
			dfs(node, parent, rightsibling)

	


'''

class TreeNode():
	"""docstring for TreeNode"""
	def __init__(self, val):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None

class Solution:
	def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
		if root is None:
			return None
		globalroot = [None]
		def dfs(node, parent, rightsibling):
			
			#Process
			old_left = node.left
			old_right = node.right
			node.right = parent
			node.left = rightsibling

			if node:
				print("node : " , node.val)
				if node.right:
					print("node right: " , node.right.val)
				if node.left:
					print("node left: " , node.left.val)

			if old_left:
				print("old_left : " , old_left.val)
			if old_right:
				print("old_right : " , old_right.val)

			print("==========")

			#leaf node
			if old_left is None and old_right is None:
				globalroot[0] = node


			#recursive case
			if old_left is not None:
				dfs(old_left, node, old_right)

		dfs(root, None, None)
		return globalroot[0]
			

	
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


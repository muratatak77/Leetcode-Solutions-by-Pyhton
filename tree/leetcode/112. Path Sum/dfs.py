class TreeNode():

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		

def overall(root, sum):

	if not root:
		return  False
	flag = [False]


	def dfs(node, target):
		print("node : ", node.val, " - target : ", target)
		#base case : leaf workers
		if not node.left and not node.right:
			print("target : ", target)
			if target == node.val:
				flag[0] = True
				return

		#recursive case : internal node
		if node.left:
			dfs(node.left, target - node.val)
		if node.right:
			dfs(node.right, target - node.val)

	dfs(root, sum)
	return flag[0]



node = TreeNode(5)
node.left = TreeNode(4)
node.left.left = TreeNode(11)
node.left.left.right = TreeNode(2)
node.left.left.left = TreeNode(7)
node.right = TreeNode(8)

sum = 22
print(overall(node, sum))


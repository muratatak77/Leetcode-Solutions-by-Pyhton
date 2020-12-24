'''
DFS iterater 
WE can use a stack in DFS iterator appoarch
DFS - Preorder
Top > Down and Left > Right

'''

class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def dfs(root, total):
	if not root:
		return False

	stack = [(root, total - root.val)]
	while stack:
		node , curr_sum = stack.pop()
		if not node.left and not node.right and curr_sum == 0:
			return True
		if node.left:
			stack.append((node.left, curr_sum - node.left.val))
		if node.right:
			stack.append((node.right, curr_sum - node.right.val))

	return False


node = TreeNode(5)
node.left = TreeNode(4)
node.left.left = TreeNode(11)
node.left.left.right = TreeNode(2)
node.left.left.left = TreeNode(7)
node.right = TreeNode(8)

sum = 22
print(dfs(node, sum))


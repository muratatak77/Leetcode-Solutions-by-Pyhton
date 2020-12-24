class TreeNode():

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		

def postorderTraversal(root):
	if not root:
		return []
		
	result = []
	stack = [root]

	while stack:
		node = stack.pop()
		result.append(node.val)
		if node.left:
			stack.append(node.left)
		if node.right:
			stack.append(node.right)

	return result[::-1]

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)

# node.left.left = TreeNode(None)
# node.left.right = TreeNode(None)

node.left.left = TreeNode(4) 
node.left.right = TreeNode(5) 

result = postorderTraversal(node)
print(result)

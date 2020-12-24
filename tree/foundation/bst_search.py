class TreeNode:
	"""docstring for TreeNode"""
	def __init__(self, key):
		super(TreeNode, self).__init__()
		self.key = key
		self.left = None
		self.right = None

def search(root, key):
	curr = root
	while curr is not None:
		if key == curr.key:
			return curr
		elif key < curr.key:
			curr = curr.left
		else:
			curr = curr.right
	return None

# A utility function to do inorder tree traversal 
def inorder(root): 
    if root: 
        print(vars(root))
        inorder(root.left) 
        inorder(root.right) 


node = TreeNode(44)
node.left = TreeNode(17)
node.right = TreeNode(88)

node.left.left = TreeNode(8)
node.left.right = TreeNode(32)

node.right.left = TreeNode(65) 
node.right.right = TreeNode(97) 

result = search(node, 88)
# print(result.__dict__)
# print(vars(result))
print(inorder(result))





		
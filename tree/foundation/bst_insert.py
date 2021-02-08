class TreeNode:
	def __init__(self, key):
		super(TreeNode, self).__init__()
		self.key = key
		self.left = None
		self.right = None

def insert(root, key):

	newnode = TreeNode(key)
	if root is None:
		return newnode

	prev = None
	curr = root
	while curr is not None:
		if key == curr.key:
			print("Key already exists!")
			return root
		elif key < curr.key:
			prev = curr
			curr = curr.left
		else:
			prev = curr
			curr = curr.right

	if key < prev.key:
		prev.left = newnode
	else:
		prev.right = newnode

	return root



# A utility function to do inorder tree traversal 
def print_nodes(root): 
    if root: 
        print(vars(root))
        print_nodes(root.left) 
        print_nodes(root.right) 



node = TreeNode(44)
node.left = TreeNode(17)
node.right = TreeNode(88)

node.left.left = TreeNode(8)
node.left.right = TreeNode(32)

node.right.left = TreeNode(65) 
node.right.right = TreeNode(97) 

result = insert(node, 54)
# result = insert(node, 65)
# print(result.__dict__)
# print(vars(result))
print(print_nodes(result))





		
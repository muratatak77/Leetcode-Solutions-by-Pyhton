class TreeNode():
	def __init__(self, val=None, left_ptr=None, right_ptr=None):
		self.val = val
		self.left_ptr = left_ptr
		self.right_ptr = right_ptr

def updown(root):

	if not root:
		return root

	#base case
	if not root.left_ptr and not root.right_ptr:
		print("return root : ", root.__dict__)
		return root

	#recursive case
	# if root.left_ptr:
	
	left = updown(root.left_ptr)
	print("result recursive left : ", left.__dict__)

	new_root = TreeNode(left.val)
	print("new_root : ", new_root.__dict__)

	print("1 root : ", root.__dict__)
	# print("root.right_ptr : ", root.right_ptr.__dict__)

	root.left_ptr.left_ptr = root.right_ptr
	root.left_ptr.right_ptr = root

	# new_root.left_ptr = root.right_ptr
	# new_root.right_ptr = root

	# print("after ass root : ", root.__dict__)
	# print("root.left_ptr.left_ptr : ", root.left_ptr.left_ptr.__dict__)
	# print("root.left_ptr.right_ptr : ", root.left_ptr.right_ptr.__dict__)
	root.left_ptr = None
	root.right_ptr = None
	
	print("root 3 : ", root.__dict__)
	print("=====================")
	return new_root


def print_preorder(root):
	if not root:
		return None

	print_preorder(root.left_ptr)
	print_preorder(root.right_ptr)
	print(root.val)

node = TreeNode(1)
node.left_ptr =  TreeNode(2)
node.right_ptr = TreeNode(3)
node.left_ptr.left_ptr =  TreeNode(4)
node.left_ptr.left_ptr =  TreeNode()


res = updown(node)
print(res.__dict__)

print_preorder(res)

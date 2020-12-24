class TreeNode():
	def __init__(self, val=None, left_ptr=None, right_ptr=None):
		self.val = val
		self.left_ptr = left_ptr
		self.right_ptr = right_ptr

def updown(root):

		def helper(node, parent, parentRightChild):
			if not node:
				return parent
			
			leftChild, rightChild = node.left_ptr, node.right_ptr
			
			node.right_ptr = parent  
			node.left_ptr = parentRightChild
			
			return helper(leftChild, node, rightChild)

		ans = helper(root, None, None)
		return ans


def print_preorder(root):
	if not root:
		return None

	print(root.val)
	print_preorder(root.left_ptr)
	print_preorder(root.right_ptr)

node = TreeNode(1)
node.left_ptr =  TreeNode(2)
node.right_ptr = TreeNode(3)
node.left_ptr.left_ptr =  TreeNode(4)
node.left_ptr.right_ptr =  TreeNode(5)


res = updown(node)
print("res :" , res.__dict__)

print_preorder(res)

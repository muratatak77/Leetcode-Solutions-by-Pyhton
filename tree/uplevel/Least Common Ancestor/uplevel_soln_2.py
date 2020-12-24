#doesnt work in every case
class TreeNode(object):
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right



def lca(root, p,q):
	
	if not root:
		return

	print("process root : ", root.data)
	print("===============")

	if root in (p,q):
		return root.data

	left = lca(root.left, p, q)
	print("left : ", left)
	right = lca(root.right, p, q)
	print("right : ", right)

	if left and right:
		return root.data

	return left or right


node = TreeNode(1)
node.left =  TreeNode(2)
node.left.left = TreeNode(4)

node.left.right = TreeNode(5)

node.left.left.left = TreeNode(8)
node.left.left.right = TreeNode(9)

node.left.right.left = TreeNode(10)
node.left.right.right = TreeNode(11)

# 2 2 2
# 1 2
p = node.left.left.right
q = node.left.right.right

res = lca(node, p, q)
print(res)
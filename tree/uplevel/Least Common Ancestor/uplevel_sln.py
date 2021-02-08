#doesnt work in every case
class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def lca(root, a, b):
	
	if not root.left and not root.right:
		return root.val

	if not root:
		return None

	def dfs(node):
		
		nonlocal answer
		
		#base case : leaf workers
		if not node:
			return False
		
		#recursive  case :
	
		left = dfs(node.left)
		print("left : ", left)
		right = dfs(node.right)
		print("right : ", right)

		mid = node == a or node == b
		
		if mid + left + right >= 2:
			answer = node.val
	
		return mid or left or right
	
	answer = None
	dfs(root)
	return answer
   


# node = TreeNode(1)
# node.left =  TreeNode(2)
# node.left.left = TreeNode(4)

# node.left.right = TreeNode(5)

# node.left.left.left = TreeNode(8)
# node.left.left.right = TreeNode(9)

# node.left.right.left = TreeNode(10)
# node.left.right.right = TreeNode(11)


# 1 1 1

node =  TreeNode(1)
node.left = TreeNode(2)

# 2 2 2
# 1 2
p = node.left.left
q = node.left.left

res = lca(node, p, q)
print(res)

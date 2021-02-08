from collections import deque
class TreeNode():

	def __init__(self, val):
		# super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None

def bfs(root):

	if not root:
		return []

	q = deque([root])

	while len(q) != 0:

		numnodes = len(q)
		printed = False
		
		for _ in range(numnodes):
			node = q.popleft()

			if not printed:
				print(node.val)
				printed = True

			if node.left is not None:
				q.append(node.left)
			if node.right is not None:
				q.append(node.right)


node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)

# node.left.left = TreeNode(None)
# node.left.right = TreeNode(None)

node.right.left = TreeNode(15) 
node.right.right = TreeNode(7) 

bfs(node)

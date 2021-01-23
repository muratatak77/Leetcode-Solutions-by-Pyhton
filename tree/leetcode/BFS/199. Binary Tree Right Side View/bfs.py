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
	result = []
	q = deque([root])
	while len(q) != 0:
		numnodes = len(q)
		temp = []
		for _ in range(numnodes):
			node = q.popleft()
			temp.append(node.val)
			if node.left is not None:
				q.append(node.left)
			if node.right is not None:
				q.append(node.right)
		result.append(temp[-1])	
	return result


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)

node.left.right = TreeNode(5) 

node.right.right = TreeNode(4) 

result = bfs(node)
print(result)
# print(result.__dict__)
# print(vars(result))


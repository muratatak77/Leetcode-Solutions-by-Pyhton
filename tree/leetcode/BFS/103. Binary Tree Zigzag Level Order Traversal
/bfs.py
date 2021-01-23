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
	rtol = False

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

		if rtol:
			temp.reverse()
		rtol = not rtol
		
		result.append(temp)
	
	# result.reverse()
	return result

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)

node.right.left = TreeNode(15) 
node.right.right = TreeNode(7) 

result = bfs(node)
print(result)
# print(result.__dict__)
# print(vars(result))


from collections import deque

class TreeNode():

	def __init__(self, val):
		self.val = val
		self.children = []

def bfs(root):
	if not root:
		return []
	result = []
	q = deque([root])
	while q:
		temp = []
		for _ in range(len(q)):
			node = q.popleft()
			temp.append(node.val)
			# q.extend(node.children) #same  with the for iterator below
			for child in node.children:
				q.append(child)
		result.append(temp)
	return result



# children = [3,5,6]
node = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2)
node4 = TreeNode(4)

node.children.append(node3)
node.children.append(node2)
node.children.append(node4)

node5 = TreeNode(5)
node6 = TreeNode(6)

node3.children.append(node5)
node3.children.append(node6)

result = bfs(node)
print(result)
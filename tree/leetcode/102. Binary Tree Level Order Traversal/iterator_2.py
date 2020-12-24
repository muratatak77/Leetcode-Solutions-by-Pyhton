'''
level traversal order is the other saying BFS (Breadth First Search)
We scan through the tree level by level, following the order of height, from top to bottom.
	We need apply a Queue strusture (FIFO). We can add whole Node to a queue. And after we can pull by one by node from queue and we can add the global result array.
'''

from collections import deque

class TreeNode(object):

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

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
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
		result.append(temp)

	return result


node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.left.left = TreeNode(15)
node.left.right = TreeNode(12)



result = bfs(node)
print(result)


'''
Time comp : O(N) each node is processed exatly one
Space : O(N) to keep the output structure which contains N node values

'''

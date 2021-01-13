'''
 We can use BFS. bacause BFS scans the level traversal order.
 we need a queue (FIFO)
 We can add to a temp array nodes from a root.
 final we can add global result array from temp last array.
'''

from collections import deque

class TreeNode():
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
		result.append(temp[-1])

	return result



t1 = TreeNode(1)
t2 = TreeNode(2)
# t3 = TreeNode(3)
# t4 = TreeNode(4)
# t5 = TreeNode(5)

t1.left = t2
# t1.right = t3
# t2.right = t5
# t3.right = t4

result = bfs(t1)
print(result)
# print(result.__dict__)
# print(vars(result))


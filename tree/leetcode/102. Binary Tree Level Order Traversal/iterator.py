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
	print("list q : ", list(q))

	while len(q) != 0:
		numnodes = len(q)
		temp = []

		print("len(q) : ", len(q))

		for _ in range(numnodes):
			node = q.popleft()
			print("after pop left node in q " , node.__dict__)

			temp.append(node.val)
			print("temp append node val : ", node.val)

			if node.left is not None:
				q.append(node.left)
				print("Q append node left : " , node.left.__dict__)
			if node.right is not None:
				q.append(node.right)
				print("Q append node right : " , node.right.__dict__)

			print("after append Q >>> ", list(q))

		result.append(temp)
		print("Append result : ", temp)
		print("=======================")

	return result
		

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)

# node.left.left = TreeNode(None)
# node.left.right = TreeNode(None)

node.right.left = TreeNode(15) 
node.right.right = TreeNode(7) 

result = bfs(node)
print(result)

# print(result.__dict__)
# print(vars(result))


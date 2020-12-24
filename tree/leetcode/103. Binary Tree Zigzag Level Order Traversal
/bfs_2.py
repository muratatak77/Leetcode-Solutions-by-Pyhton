from collections import deque
'''
 Level traversal order is BFS appoarc = Breadth First Search
 we can scan BFS , top down and left to right. But after scan one level we need to keep a boolean decision left to right : ltor.
 first ltor is false but second should be true. When this booelan decision is True , we can append to the global result as a reverse() temp

 We need a queue (FIFO) for BFS. first in first out. WE need get every time first element from Q
'''
class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def bfs(root):
	if not root:
		return []

	result = []
	q = deque([root])
	rtol = False

	while q:
		temp = []
		for _ in range(len(q)):
			
			node = q.popleft()
			temp.append(node.val)
			
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)

		if rtol:
			temp.reverse()
		rtol = not rtol

		result.append(temp)

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


'''
Time comp : O(N) N is number of nodes in the tree
Space : O(N) 
'''


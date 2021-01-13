'''
	level order traversal = BFS
	We can apply BFS , Breadth First Search 
	scan level by level and bottom to top 
	We use a queue (FIFO) first items that go in should be the first to come out
	In n-ary tree we have to define children elements in TreeNode
'''

from collections import deque

class TreeNode(object):
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

			for child in node.children:
				q.append(child)

		result.append(temp)

	return result


t1 = TreeNode(1)
t3 = TreeNode(3)
t2 = TreeNode(2)
t4 = TreeNode(4)

t1.children.append(t3)
t1.children.append(t2)
t1.children.append(t4)


t5 = TreeNode(5)
t6 = TreeNode(6)

t3.children.append(t5)
t3.children.append(t6)

result = bfs(t1)
print(result)

'''
Time complexity :  O(N) , where n is number of nodes. 
					Each node getting added to the queue , pop from the q, and added to the result once.
Space complexity: O(N) , Queue to keep track of nodes we still need to visit the children of.
						 Q contain all the element  at a single level
'''
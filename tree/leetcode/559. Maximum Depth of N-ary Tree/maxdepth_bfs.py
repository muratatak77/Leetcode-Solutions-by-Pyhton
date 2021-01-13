'''
	We can apply BFS structure. Level by level iterator.
	every level is a depth. 
	Depth ;

		1		L0 - D0

	2		3 	L1 - D1

2	4	7       L2 - D2

'''

from collections import deque

# Definition for a Node.
class Node:
	def __init__(self, val=None, children=[]):
		self.val = val
		self.children = children

class Solution:
	def maxDepth(self, root: 'Node') -> int:

		if not root:
			return 0

		level = 0
		q = deque([root])

		while q:
			level += 1
			for i in range(len(q)):
				node = q.popleft()
				for child in node.children:
					q.append(child)

		return level

# root = [1,null,3,2,4,null,5,6]

root = Node(1)
node3 = Node(3)
root.children = [node3, Node(2), Node(1)]
node3.children = [Node(5), Node(6)]


res = Solution().maxDepth(root)
print("res : ", res)

'''
	T(N) = O(N) visit each node exatly once
	S(N) = O(N) queue would be store N times in the worst case.
				Best case : in the completly balanced tree would be log(N)

				

'''
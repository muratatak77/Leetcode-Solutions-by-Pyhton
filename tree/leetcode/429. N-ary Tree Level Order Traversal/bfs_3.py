''' 
	BFS - Level order traversal
	We need a queue (FIFO) data structure to keep items level by level
	We have N-Ary tree , we need to get children of Tree
'''

from typing import List
from collections import deque

class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		self.val = val
		self.children = []


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

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




root = TreeNode(1)
t3 = TreeNode(3)
root.children = [t3,TreeNode(2), TreeNode(4)]
t3.children = [TreeNode(5), TreeNode(6)]

res = Solution().levelOrder(root)
print("res : ", res)


'''
	T(N) = O(N) every level iterate just once 
	S(N) = O(N) 
'''
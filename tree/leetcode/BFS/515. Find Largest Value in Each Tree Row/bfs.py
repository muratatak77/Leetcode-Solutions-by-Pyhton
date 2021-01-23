'''
	BFS - level by level iterate 
	we can keep a total number to store each level total and number of nodes 
	and after the each lenght of Q iterative, we can add to result as : total/number of nodes
'''

from collections import deque

class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	def largestValues(self, root):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""
		if not root:
			return []

		result = []
		q = deque([root]) # 3

		while q:
			temp = []
			for _ in range(len(q)):
				node = q.popleft() # 3
				temp.append(node.val) # 3
				if node.left:
					q.append(node.left) # 9
				if node.right:
					q.append(node.right) # 20
			result.append(max(temp))

		return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


res = Solution().largestValues(root)
print("res :", res)

'''
	T(N) = O(N) each node in just 1 iterative 
	S(N) = O(N) The size of Q
'''


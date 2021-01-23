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
	def averageOfLevels(self, root):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""
		if not root:
			return []

		result = []
		q = deque([root]) # 3

		while q:
			total = 0.0
			temp = []
			numnodes = len(q)
			for _ in range(numnodes):
				node = q.popleft() # 3
				temp.append(node.val) # 3
				if node.left:
					q.append(node.left) # 9
				if node.right:
					q.append(node.right) # 20
				total += node.val

			result.append(total/numnodes)

		return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


res = Solution().averageOfLevels(root)
print("res :", res)

'''
	T(N) = O(N) each node in just 1 iterative 
	S(N) = O(M) The size of Q or temp can grow upto atmost the max number of nodes 
				at any level in the given binary tree.
				M refers the max number of nodes at any level in the input tree


	From leetcode : 

	Time complexity : O(n). The whole tree is traversed atmost once. Here, nn refers to the number of nodes in the given binary tree.

	Space complexity : O(m). The size of queuequeue or temptemp can grow upto atmost the maximum number of nodes at any level in the given binary tree. Here, mm refers to the maximum mumber of nodes at any level in the input tree.
'''


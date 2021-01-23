from collections import deque
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def maxLevelSum(self, root: TreeNode) -> int:

		if not root:
			return 0

		q = deque([root])

		level = 0
		minlevel = 0
		maxsum = float("-inf")

		while q:
			
			level += 1
			total = 0

			for _ in range(len(q)):

				node  = q.popleft()

				if node.left:
					q.append(node.left)

				if node.right:
					q.append(node.right)

				total += node.val

				print("Total : ", total)
				print("maxsum : ", maxsum)
				print("minlevel : ", minlevel)
				print("=-----------------")
				
			if total > maxsum:
				print("CHANGED")
				maxsum = total
				minlevel = level


		return minlevel

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)

root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)


# root = TreeNode(989)
# root.right = TreeNode(10250)

# root.right.left = TreeNode(98693)
# root.right.right = TreeNode(-89388)
# root.right.right.right = TreeNode(-32127)


res = Solution().maxLevelSum(root)
print("res : ", res)

'''
	T(N) = O(N)
	S(N) = O()
'''

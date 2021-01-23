import collections

class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	def distanceK(self, root, target, K):
		def dfs(node, par = None):
			if node:
				node.par = par
				dfs(node.left, node)
				dfs(node.right, node)

		dfs(root)

		# print("root : ", root.left)
		# print("root : ", root.left.left.__dict__)
		# print()

		queue = collections.deque([(target, 0)])
		print("queue :", queue)
		seen = {target}
		# print("seen :", seen)

		while queue:
			print("queue ::::", queue)
			print("queue[0][1] : ", queue[0][1])
			if queue[0][1] == K:
				print("Q : ", queue)
				return [node.val for node, d in queue]

			node, d = queue.popleft()
			print("node  ", node.val)
			print("d  ", d)

			for nei in (node.left, node.right, node.par):

				print("nei : ", nei)
				if nei:
					print("nei val : ", nei.val)

				if nei and nei not in seen:
					seen.add(nei)
					if nei:
						print("     add seen : ",nei.val)
					queue.append((nei, d+1))
					if nei:
						print("     append queue : ",nei.val, " -  d: ", d+1)

				print("===========================================")


		return []






node  = TreeNode(3)
node.left = TreeNode(5)
node.left.left  = TreeNode(6)
node.left.right  = TreeNode(2)
node.left.right.left  = TreeNode(7)
node.left.right.right  = TreeNode(4)

node.right = TreeNode(1)
node.right.left = TreeNode(0)
node.right.right = TreeNode(8)

target = node.left
K = 2
res = Solution().distanceK(node, target, K)
print("res :", res)            
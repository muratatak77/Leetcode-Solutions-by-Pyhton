from collections import deque
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def verticalTraversal(self, root):
	
			node_list = []

			def BFS(root):
				print(root)
				queue = deque([(root, 0, 0)])
				while queue:
					node, row, column = queue.popleft()
					if node is not None:
						node_list.append((column, row, node.val))
						queue.append((node.left, row + 1, column - 1))
						queue.append((node.right, row + 1, column + 1))

			# step 1). construct the global node list, with the coordinates
			BFS(root)

			# step 2). sort the global node list, according to the coordinates
			print("node_list : ", node_list)
			node_list.sort()
			print("node_list after sort : ", node_list)

			# step 3). retrieve the sorted results partitioned by the column index
			ret = dict([])
			for column, row, value in node_list:
				if column in ret:
					ret[column].append(value)
				else:
					ret[column] = [value]

			return ret.values()



node  = TreeNode(10)
node.left = TreeNode(4)
node.left.left  = TreeNode(11)
node.left.right  = TreeNode(8)

node.right = TreeNode(3)
node.right.left = TreeNode(5)
node.right.right = TreeNode(13)

res = Solution().verticalTraversal(node)
print("res :", res)
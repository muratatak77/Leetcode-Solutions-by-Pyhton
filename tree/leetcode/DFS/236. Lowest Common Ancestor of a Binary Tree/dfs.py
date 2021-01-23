# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):

	def __init__(self):
		self.ans = None
		
	def lowestCommonAncestor(self, root, p, q):

		def helper(cur_node):

			#base case , lead nodes
			if not cur_node:
				return False
			
			#recursive case , lead nodes

			print("Call helper left cur_node " , cur_node.val)
			left = helper(cur_node.left)
			print("Call helper right cur_node " , cur_node.val)
			right = helper(cur_node.right)

			mid = cur_node == p or cur_node == q
			print("   mid : ", mid)
			print("   left : ", left)
			print("   right : ", right)
			print("   		mid + left + right : ",  mid + left + right)

			if mid + left + right >= 2:
				print("			*******   Found it ans. node val : ", cur_node.val)
				self.ans = cur_node
			
			return mid or left or right

		helper(root)
		return self.ans


node = TreeNode(1)
node.left = TreeNode(2)

node.left.left = TreeNode(4) 
node.left.right = TreeNode(5) 

node.left.left.left = TreeNode(8) 
node.left.left.right = TreeNode(9) 

node.left.right.left = TreeNode(10) 
node.left.right.right = TreeNode(11) 

p = node.left.left.right
q = node.left.right.right

res = Solution().lowestCommonAncestor(node, p, q)
print("res :", res.val)


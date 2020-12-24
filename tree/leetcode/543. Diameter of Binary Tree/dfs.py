# global globaldia
class TreeNode():

	def __init__(self, val):
		# super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None


class Diameter():
		
	def computeDia(self, root):
		
		self.globaldia = 0

		def dfs(node):
			#base case : leaf worker
			print("process node : ", node.__dict__)
			# if node is None:
				# return 0
			if node.left is None and node.right is None:
				return 0

			#recursive case: internal node
			mydia = 0
			if node.left:
				lh = dfs(node.left)
				mydia += lh + 1
				print("mydia l : ", mydia)

			if node.right:
				rh = dfs(node.right)
				mydia += rh + 1
				print("mydia r: " , mydia)

			print("return : max(lh,rh)+1. LH : " , lh, " - RH : ", rh ,  " + 1")
			self.globaldia = max(self.globaldia, mydia)
			print("globaldia >>  ", self.globaldia )
			max_lh = max(lh,rh)+1
			print("max_lh : " , max_lh)
			print("==========================")

			return max_lh
		
		dfs(root)
		return self.globaldia




node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)

node.left.left = TreeNode(4) 
node.left.right = TreeNode(5) 

result = Diameter().computeDia(node)
print(result)
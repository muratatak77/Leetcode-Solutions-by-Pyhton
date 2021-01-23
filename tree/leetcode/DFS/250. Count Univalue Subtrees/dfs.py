# global globaldia
class TreeNode():

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Univalue():
		
	def countUnivalSubTree(self, root):
		
		self.globalcount = 0

		def dfs(node):
			#base case : leaf worker
			if node.left is None and node.right is None:
				self.globalcount += 1 #everytime leaf workers is univalue
				return True

			#recursive case: internal node
			amIunival = True
			if node.left:
				print("check Node Left: " , node.__dict__,  " Node Left Val :  ", node.left.val)
				bl = dfs(node.left)
				print("BL : ", bl)
				print("self.globalcount : ", self.globalcount)
				if bl is False or (node.val != node.left.val):
					amIunival = False

			if node.right:
				print("check Node Right : " , node.__dict__ ,  " Node Right Val :  ", node.right.val)
				br = dfs(node.right)
				print("BR : ", br)
				print("self.globalcount : ", self.globalcount)
				if br is False or (node.val != node.right.val):
					amIunival = False

			if amIunival:
				self.globalcount += 1

			return amIunival
		
		dfs(root)
		return self.globalcount

# node = TreeNode(1)
# node.left = TreeNode(1)

node = TreeNode(5)
node.left = TreeNode(1)
node.right = TreeNode(5)

node.left.left = TreeNode(5) 
node.left.right = TreeNode(5) 

node.right.right = TreeNode(5)

result = Univalue().countUnivalSubTree(node)
print(result)
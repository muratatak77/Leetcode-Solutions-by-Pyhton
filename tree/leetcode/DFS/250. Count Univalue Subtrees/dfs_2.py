
# global globalcount
'''
 we need 2 level solution
 global solution ;
 node solution
'''
class TreeNode():

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Univalue():

	def countUnivalSubTree(self, root):

		if not root:
			return 0
		
		self.globalcount = 0

		def dfs(root):
			amIUnival = True
			#base case , leaf workers 
			#we need to check left or right
			if not root.left or not root.right:
				self.globalcount += 1
				return True

			
			#recursive case, internal node
			#each node needs whether I am unival or not.
			#if current level is unival we need to add global count increment

			if root.left:
				isleftUni = dfs(root.left)
				if isleftUni is False or node.val != node.left.val:
					amIUnival = False

			if root.right:
				isRightUni = dfs(root.right)
				if isRightUni is False or node.val != node.right.val:
					amIUnival = False

			if amIUnival:
				self.globalcount += 1

			return amIUnival

		dfs(root)
		return self.globalcount


		
# node.left = TreeNode(1)

node = TreeNode(5)
node.left = TreeNode(1)
node.right = TreeNode(5)

node.left.left = TreeNode(5) 
node.left.right = TreeNode(5) 
# 
node.right.right = TreeNode(5)

result = Univalue().countUnivalSubTree(node)
print(result)

'''
T(N) = O(N) scan every each
S(N) = O(H) height of tree. so O(N)
'''
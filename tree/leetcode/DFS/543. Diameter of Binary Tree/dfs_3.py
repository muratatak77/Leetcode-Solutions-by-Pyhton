# global globaldia
'''
	DFS - down to up approach 
	Because we need compute the height left and right subtree hence we need a heigh of information from down from child to parent. 

 	we need to compute in this question. 
 		Every node has to compute itself height and pass to parent
 		compute the global solution from left height and right height

'''
class TreeNode():

	def __init__(self, val):
		# super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None


class Diameter():

	def computeDia(self, root):

		self.globaldia = 0

		def dfs(root):
			
			#base case , leaf workers
			if not root.left and not root.right:
				return 0

			#recursive case
			mydia = 0 # every node has to compute itself height
			if root.left:
				lh = dfs(root.left)
				mydia += lh +1 # left part height computing

			if root.right:
				rh = dfs(root.right)
				mydia += rh +1 # right part height of computing

			#we need to compute globaldiameter 
			self.globaldia = max(self.globaldia,mydia) # global height

			return max(lh,rh)+1 #own height

		dfs(root)
		
		return self.globaldia



node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)

node.left.left = TreeNode(4) 
node.left.right = TreeNode(5) 

result = Diameter().computeDia(node)
print(result)



'''
O(T) = O(N). We visit every node once
Space = O(H) height of tree : O(N) the size of our implicit call stack during our depth-first search

'''
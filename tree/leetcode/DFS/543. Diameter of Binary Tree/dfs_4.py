# global globaldia
'''

	If we apply up down we will not be able to get the answer. Top Down goes individual path. 

	DFS - Bottom > Up approach 

	Because we need compute the height left and right subtree 
	hence we need a heigh of information from down from child to parent. 
	
	we will max aggrigate from bottom to up in a left and right tree

	Each recursive case will return height of relavent tree
	And dfs function will retirn the max depth/height of subtree at node

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

		def dfs(node):
			#base case , leaf nodes
			#we should return 0, becuase we start compute from here
			if not node.left and not node.right:
				return 0

			#recursive case
			mydia = 0
			if node.left:
				lh = dfs(node.left)
				print("lh : ", lh)
				mydia += 1 + lh 

			if node.right:
				rh = dfs(node.right)
				mydia += 1 + rh

			self.globaldia = max(self.globaldia, mydia)
			print("RETURN :  max(lh,rh)+1. LH : ",lh, " - RH :", rh, " MAX : ",  max(lh,rh)+1)
			return max(lh,rh)+1


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
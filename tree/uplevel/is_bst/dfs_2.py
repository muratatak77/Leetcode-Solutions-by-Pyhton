import sys
class TreeNode():
   def __init__(self, val=None, left_ptr=None, right_ptr=None):
	   self.val = val
	   self.left_ptr = left_ptr
	   self.right_ptr = right_ptr

# complete the function below

def isBST(root):
	#edge cases 
	if not root: #none
		return True

	
	def dfs(node, min = -sys.maxsize - 1 , max = sys.maxsize):
		#base case : leaf workers
		if not node:
			return True
		print("process node : ", node.val , " min  : " , min ,  " - max : ", max)

		if node.val > max or node.val < min:
			return False
			
		#recursive case : leaf workers  
		if not dfs(node.left_ptr, min, node.val):
			return False

		return dfs(node.right_ptr, node.val, max)

	
	return dfs(root)


node = TreeNode(300)
node.left_ptr =  TreeNode(200)
node.right_ptr = TreeNode(400)
node.left_ptr.left_ptr = TreeNode(200)
node.left_ptr.right_ptr = TreeNode(250)

res = isBST(node)
print(res)
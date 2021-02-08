# global globaldia
class TreeNode():

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def bstFromPreorder(preorder):

	hmap = {}
	inorder = sorted(preorder)
	for i in range(len(inorder)):
		hmap[inorder[i]] = i

	def helper(P, startP, endP, I, startI, endI):

		#base case: leaf workers
		if startP > endP: #size 0
			return None

		if startP == endP: #size 1
			return TreeNode(P[startP])

		#recursive case : internal node
		root_node = TreeNode(P[startP]) #we know first element root node in preorder
		root_index = hmap[P[startP]] #we need root index to find subtrees in preorder
		numleft = root_index - startI #in inorder

		root_node.left = helper(P, startP+1, startP+numleft, I, startI, root_index-1)
		root_node.right = helper(P, startP+numleft+1, endP, I, root_index+1, endI)
		return root_node


	return helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1 )



def printNode(root):

	if not root:
		return
		
	print(root.val)
	printNode(root.left)
	printNode(root.right)


preorder = [8,5,1,7,10,12]
ans = bstFromPreorder(preorder)
printNode(ans)

print(ans.__dict__)

# global globaldia
class TreeNode():

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def buildTree(preorder, inorder):
	
	hmap = {}

	for i in range(len(inorder)):
		hmap[inorder[i]] = i #key is array element , value is index
		
	print("hmap : ", hmap)

	def helper(P, startP, endP, I, startI, endI):
		#base case
		if startP > endP: #size 0
			return None

		if startP == endP: #size 1
			return TreeNode(P[startP])

		#recursive case
		root_node = TreeNode(P[startP])
		root_index = hmap[P[startP]]  # we able to know just the root index in pre-order > P[startP]. We can't know any subtrees
		num_left = root_index - startI #we can learn leftsubtree bound in just Inorder 
		numright = endI - root_index  #we can learn rightsubtree bound in just Inorder
		root_node.left = helper(P, startP+1, startP+num_left, I, startI, root_index-1 )
		root_node.right = helper(P, numright, endP, I, root_index+1 ,endI )
		return root_node

	return helper(preorder,0,len(preorder)-1, inorder,0,len(inorder)-1)


def printNode(root):

	if not root:
		return
		
	print(root.val)
	printNode(root.left)
	printNode(root.right)

		
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

ans = buildTree(preorder,inorder)
print(ans.__dict__)

printNode(ans)

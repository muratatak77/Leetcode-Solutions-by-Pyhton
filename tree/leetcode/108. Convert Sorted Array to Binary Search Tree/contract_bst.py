class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None

def sortedArrayToBST(nums):

	#divide and conquer approach
	def helper(A, start, end):
		#base case
		if start > end:
			return None

		if start == end:
			return TreeNode(A[start])

		#recursive case
		mid = start + ((end-start)//2)

		root = TreeNode(A[mid])
		root.left = helper(A, start, mid-1)
		root.right = helper(A, mid+1, end)
		return root

	return helper(nums,0,len(nums)-1)

def printNode(root):

	if not root:
		return
		
	print(root.val)
	printNode(root.left)
	printNode(root.right)


nums = [-10,-3,0,5,9]
ans = sortedArrayToBST(nums)
printNode(ans)



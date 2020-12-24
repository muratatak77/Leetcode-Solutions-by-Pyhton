'''
	--------------------------------------------------------

	[-10,-3, 0, 5, 9]

	     0
	-10      5 
	    -3      9

	balanced tree meaning : the depths of the two subtrees of every node never differ by more than 1.
	middle element should be root in balanced bst.
	we can use divide and conquer approach . we can start middle element.and left sub tree should be less than middle element 
	right sub tree should be grater than middle element in the array.

	----------------------------

	DFS recursion 
	preorder traversal : always choose left middle node as a root
	node > left > right
	
	root
	root.left
	root.right

'''

class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	"""docstring for Solution"""
	def sortedArrayToBST(self, nums):

		def helper(start, end):
			#base case, leaf node
			if start > end:
				return None

			if start == end:
				return TreeNode(nums[start])

			#recursive case, internal nodes
			mid = start + (end-start)//2
			root = TreeNode(nums[mid])
			root.left = helper(start, mid-1)
			root.right = helper(mid+1, end)
			return root

		return helper(0,len(nums)-1)

def preOrderPrint(root):
	if not root:
		return None
	print(root.val)
	preOrderPrint(root.left)
	preOrderPrint(root.right)

nums = [-10,-3,0,5,9]
ans = Solution().sortedArrayToBST(nums)
preOrderPrint(ans)


'''
T(N) = O(N) . evach node creates a TreeNode that is constant amount of work. 

S(N) =  implicit call stack : O(LogN) - Height of tree
		explicit = O(N)

'''
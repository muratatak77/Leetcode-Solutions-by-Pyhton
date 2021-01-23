'''
DFS iterater 
WE can use a stack in DFS iterator appoarch
DFS - Preorder
Top > Down and Left > Right

'''

class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def dfs(root, curr_sum):

	if not root:
		return False

	#base case
	curr_sum -= root.val
	# print("curr_sum : ", curr_sum)
	# print("root.left : ", root.left)
	# print("root.left : ", root.right)
	if not root.left and not root.right and curr_sum == 0:
		return True

	#recursive case
	left = root.left
	right = root.right
	return dfs(left, curr_sum) or dfs(right, curr_sum)
	

node = TreeNode(5)
node.left = TreeNode(4)
node.left.left = TreeNode(11)
node.left.left.right = TreeNode(2)
node.left.left.left = TreeNode(7)

node.right = TreeNode(8)

sum = 22
print(dfs(node, sum))


'''
Time : O(T) = O(N) 
Space  :  Avarage case  O(H)  Height of the tree
		: Worst case O(N)
		Tree is balanced O(logN)

'''

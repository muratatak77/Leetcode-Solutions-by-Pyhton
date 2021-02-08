'''	
	DFS - Top Down Approach
	We can return just node in leaf level 
	We can keep a temp left and right in the recursive case
		and we can match for each recursive case

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        

        if not root:
        	return None

        def dfs(node):

        	#base case
        	if not node.left and not node.right:
        		return node

        	#recursive case
        	oldleft = node.left
        	oldright = node.right
        	node.left = oldright
        	node.right = oldleft
        	if node.left:
        		dfs(node.left)
        	if node.right:
        		dfs(node.right)

        dfs(node)
        return node



def print_tree(node):
	if not node:
		return
	print(" LEFT : ", node.val)
	print_tree(node.left)
	print_tree(node.right)

node = TreeNode(4)
node.left = TreeNode(2)
node.right = TreeNode(7)

node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right.left = TreeNode(6)
node.right.right = TreeNode(9)

res = Solution().invertTree(node)
print("res :", res)

print_tree(res)

'''
	T(N) = O(N)
	S(N) = O(N) height of tree in the worst case but O(N) covers

'''
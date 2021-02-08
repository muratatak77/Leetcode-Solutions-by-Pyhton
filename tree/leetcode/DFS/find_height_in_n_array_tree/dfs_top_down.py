'''	


'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []

class Solution:
    def findHeight(self, root: TreeNode) -> TreeNode:

    	if root is None:
    		return 0

    	height = [0]

    	def dfs(node, edges_upto_parent):

    		edges_upto_me = 1 + edges_upto_parent
    		print("edges_upto_parent : ", edges_upto_parent , " - edges_upto_me : ", edges_upto_me)
    		print("node val : ", node.val)
    		height[0] = max(height[0], edges_upto_me)

    		for child in node.children:
    			# print("edges_upto_parent : ", edges_upto_parent)
    			dfs(child, edges_upto_me)
    		print("-----------------------")

    	dfs(root, -1)
    	return height[0]

# children = [3,5,6]
node = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2)
node4 = TreeNode(4)

node.children.append(node2)
node.children.append(node3)
node.children.append(node4)

node5 = TreeNode(5)
node6 = TreeNode(6)

node3.children.append(node5)
node3.children.append(node6)

res = Solution().findHeight(node)
print("res : ", res)
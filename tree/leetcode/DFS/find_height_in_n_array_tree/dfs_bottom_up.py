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

    	def dfs(node):
            #base case
            if len(node.children) == 0:
                # in the leaf node we can return 0
                # and we gonna compute bottom to up
                return 0

            height = 0
            for child in node.children:
                height = max(height, 1+dfs(child)) 
                
            return height 			

    	return dfs(root)

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
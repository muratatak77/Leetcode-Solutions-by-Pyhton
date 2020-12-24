
import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower, upper):
            
            if not node:
                return True
            
            
            val = node.val
            print("val : ", val, "  - lower : ", lower, " - upper : ", upper)
            
            if val <= lower or val >= upper:
                return False
        
            if not helper(node.left, lower, val):
                return False
            
            if not helper(node.right, val, upper):
                return False
            

            return True
    
        return helper(root,  -sys.maxsize - 1,  sys.maxsize)

                    
node  = TreeNode(10)
node.left = TreeNode(4)
node.left.left  = TreeNode(3)
node.left.right  = TreeNode(8)

# node.right = TreeNode(3)
# node.right.left = TreeNode(5)
# node.right.right = TreeNode(13)

res = Solution().isValidBST(node)
print("res :", res)            
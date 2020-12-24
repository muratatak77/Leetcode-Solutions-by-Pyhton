# global globaldia
class TreeNode():

    def __init__(self, val):
        # super(TreeNode, self).__init__()
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            
            L = depth(node.left)
            R = depth(node.right)
            
            self.ans = max(self.ans, L+R+1)
            print("ans : ", self.ans, " - L : ", L  ," - R : ", R)

            return max(L, R) + 1

        depth(root)
        return self.ans - 1 




node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)

node.left.left = TreeNode(4) 
node.left.right = TreeNode(5) 

result = Solution().diameterOfBinaryTree(node)
print(result)

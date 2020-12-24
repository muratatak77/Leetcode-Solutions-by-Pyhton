class TreeNode():
   def __init__(self, val):
       self.val = val
       self.left = None
       self.right = None


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node 
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node        
                last = node
                # right
                helper(node.right)
        
        if not root:
            return None
        
        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        print("first : ", first.__dict__)
        return first


node = TreeNode(4)
node.left_ptr =  TreeNode(2)
node.right_ptr = TreeNode(5)
node.left_ptr.left_ptr = TreeNode(1)
node.left_ptr.right_ptr = TreeNode(3)

res = Solution().treeToDoublyList(node)
print(res.__dict__)
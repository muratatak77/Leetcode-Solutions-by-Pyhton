'''
    I can apply a DFS recursion approach. 
    I can count from top to down. 
    in the leaf node I wll check left and right node, 
        if we don't have right and left node
            we can add global result our temp slate 

    in the recursion part  : 
        we need add '->' part to the our temp slate
        and recursion call
    
'''

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        result = []
        
        def dfs(node, slate):
        
            slate += str(node.val)
            if not node.left and not node.right:
                result.append(slate[:])
                
            slate += '->'
            if node.left:
                dfs(node.left, slate)
            if node.right:
                dfs(node.right, slate)
        
        dfs(root, "")
        return result

            
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4) 
node.left.right = TreeNode(5) 

res = Solution().binaryTreePaths(node)
print("res : ", res)

'''
    T(N) = O(N) , we visit each node exactly once 
    O(N) = O(N) 
                O(N) > worst case > like completly unbalanced tree
                O(LogN) > best case  > but if we have balanced tree 
'''


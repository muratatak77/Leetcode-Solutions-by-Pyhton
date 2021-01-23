'''
    
    P = preoder =   root          preorder(L)        preorder(R)  
                 
                  startP            numleft           numright   endP

    

    I = inorder =   inorder(L)       root             inorder(R)
                     numleft                            numright

                     startI        rootindex              endI


    everytime preorder traversal start root. But we have a problem how to find inorder root in inorder traversal. 
    hence , we can generate a hash map. this hmap record key - value. Key : inorder elem and value is index in inorder
    
    in constract tree we can apply divide and conquer approach

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        hmap = {}
        for i in range(len(inorder)):
            hmap[inorder[i]] = i
        
        def helper(P,startP,endP,I,startI,endI):
            
            if  startP>endP:
                return None
            
            if startP == endP:
                return TreeNode(P[startP])
            
            root = TreeNode(P[startP])
            rootindex = hmap[P[startP]]
            numleft = rootindex - startI

            root.left = helper(P, startP+1, startP + numleft, I, startI, rootindex-1)
            root.right = helper(P,startP+numleft+1, endP,I,  rootindex+1, endI)
            return root
    
        return helper(preorder, 0,len(preorder)-1, inorder, 0, len(inorder)-1)
        
'''
    T(N) : O(N) : every line takes constant amount of time. Hashtable lookp, create TreeNode etc. 
    S(N) ; impilicit call stack : O(N) (There is no balanced tree.)
           explicit : O(n) >> hash table + O(n) >> output tree  = O(n)

'''''
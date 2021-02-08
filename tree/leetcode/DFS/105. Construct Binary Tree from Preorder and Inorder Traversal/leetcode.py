# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left = 0, in_right = len(inorder)):
            print("Call start in_left : ", in_left, " - in_right : ", in_right)

            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                print("")
                print("          in_left == in_right. return None. in_left : ", in_left , " - in_right : ", in_right)
                return None
            
            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            print("")
            print("      Created TreeNode. val : ", root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]
            print("    index from idx_map : ", index)

            # recursion 
            pre_idx += 1
            print("pre_idx : ", pre_idx)
            # build left subtree
            print("  -------------------- Call root.left in_left : ", in_left ,  " in_right : ", index)
            root.left = helper(in_left, index)

            # build right subtree
            print("  -------------------- Call root.right in_left : ", index + 1 ,  " in_right : ", in_right)
            root.right = helper(index + 1, in_right)
            print("====================== =================== =================")
            return root
        
        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        print("idx_map : ", idx_map)
        return helper()


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

ans = Solution().buildTree(preorder,inorder)
print(ans.__dict__)


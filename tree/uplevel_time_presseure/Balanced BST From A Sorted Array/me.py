# complete this function

'''
    For your reference:
    
    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

def build_balanced_bst(a):
    
    if not a:
        return None
    
    #divide - and conquer approach
    
    def helper(a, start, end):
        if start > end:
            return None
        
        if start == end:
            return TreeNode(a[start])
    
        mid = start + ((end-start) // 2)
        root = TreeNode(a[mid])
        root.left_ptr = helper(a, start, mid-1 )
        root.right_ptr = helper(a, mid+1, end)
        
        return root
    
    return helper(a, 0, len(a)-1)

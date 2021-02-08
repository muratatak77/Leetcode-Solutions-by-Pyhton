'''
    For your reference:
    
    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

def kth_smallest_element(root, k):

    new_list = []
    
    inorder(root,new_list)
    
    return new_list[k-1]

def inorder(root, new_list):
    
    if root==None:
        return
    
    inorder(root.left_ptr,new_list)
    new_list.append(root.val)
    inorder(root.right_ptr,new_list)
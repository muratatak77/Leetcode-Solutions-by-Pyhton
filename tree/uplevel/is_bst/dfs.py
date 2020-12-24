
class TreeNode():
   def __init__(self, val=None, left_ptr=None, right_ptr=None):
       self.val = val
       self.left_ptr = left_ptr
       self.right_ptr = right_ptr

# complete the function below

def isBST(root):
    #edge cases 
    if not root: #none
        return True
    
    # if not root.left_ptr or not root.right_ptr: #just has 1 node
        # return True
    
    result = [True]
    
    def dfs(node):
        #base case : leaf workers
        if not node.left_ptr and not node.right_ptr:
            print("bitti node : ", node.val)
            return True
            
        is_right = True
        #recursive case : internal workers
        if node.left_ptr:
            l = dfs(node.left_ptr)
            print("node.val : " ,  node.val , " >=  node.left_ptr.val :  " , node.left_ptr.val)
            if l is False or node.val <= node.left_ptr.val:
                is_right = False
        
        if node.right_ptr:
            r = dfs(node.right_ptr)
            # print("node.val >= node.right_ptr.val ", node.val >= node.right_ptr.val)
            print("node.val : " ,  node.val , " >=  node.right_ptr.val :  " , node.right_ptr.val)
            if r is False or node.val >= node.right_ptr.val:
                is_right = False
                
        result[0] = is_right
        return is_right
    
    dfs(root)
    return result[0]
    

# 300 200 400 100 400


# 4
# 100 200 300 400
# 0
# 3
# 0 1 L
# 1 2 R
# 2 3 L


5
300 200 400 100 400
0
4
0 1 L
0 2 R
1 3 L
1 4 R
# # <parentNodeIndex><space><childNodeIndex><space><leftOrRightFlag>

# node = TreeNode(300)
# node.left_ptr = TreeNode(100)
# node.left_ptr.right_ptr = TreeNode(200)
# node.left_ptr.right_ptr.left_ptr = TreeNode(400)
# node.right_ptr.right_ptr = TreeNode(400)
# 
node = TreeNode(300)
node.left_ptr =  TreeNode(200)
node.right_ptr = TreeNode(400)
node.left_ptr.left_ptr = TreeNode(100)
node.left_ptr.right_ptr = TreeNode(400)




res = isBST(node)
print(res)


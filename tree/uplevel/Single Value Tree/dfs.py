
class TreeNode():
   def __init__(self, val=None, left_ptr=None, right_ptr=None):
       self.val = val
       self.left_ptr = left_ptr
       self.right_ptr = right_ptr

# complete the function below

def findSingleValueTrees(root):
    
    if root is None:
        return 0
    
    if root.left_ptr is None and root.right_ptr is None:
        return 1
			
    global_count = [0]
    
    #bsf doesnt work because we need get the information from below subtreess
    #we need seperate solution that global and local. Global solution : I am a manager and I need whether I am unival or not
    #localsolution : every node need I am unival or not and increment to global count 
    def dfs(node):
        
        #base case : leaf workers 
        if not node.left_ptr and not node.right_ptr:
            global_count[0] += 1
            return True
        
        #recursive case : internal node
        am_i_unival = True
        
        if node.left_ptr:
            bl = dfs(node.left_ptr)
            if (bl is False) or (node.val != node.left_ptr.val):
                am_i_unival = False
            
        if node.right_ptr:
            br = dfs(node.right_ptr)
            if (br is False) or (node.val != node.right_ptr.val):
                am_i_unival = False
            
        if am_i_unival:
            global_count[0] += 1
        
        return am_i_unival
    
    dfs(root)
    return global_count[0]


	# node = TreeNode(5)
	# node.left_ptr = TreeNode(5)
	# node.right_ptr = TreeNode(5)
	# node.left_ptr.left_ptr = TreeNode(5) 
	# node.left_ptr.right_ptr = TreeNode(5) 
	# node.right_ptr.right_ptr = TreeNode(5)


node = TreeNode(12)
node.left_ptr = TreeNode(2)

result = findSingleValueTrees(node)
print(result)
			
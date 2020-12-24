
class TreeNode():
   def __init__(self, val=None, left_ptr=None, right_ptr=None):
	   self.val = val
	   self.left_ptr = left_ptr
	   self.right_ptr = right_ptr

# complete the function below


# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def BTtoLL(root):
	
	#dfs - inorder traversal = Left  + Root + Right
	#      4 
	#    2    5  
	#  1   3
	
	if not root:
		return
	
	def helper(node):
		
		nonlocal head, tail
		
		if node:
			#left call
			helper(node.left_ptr)
			
			#root process
			if tail:
				#link the previous node (tail) with the current one (node)
				tail.right = node  # 1 > 2 > 3 > 4 > 5
				node.left = tail # 1 < 2 < 3 < 4 < 5
			else:
				#keep the left most node as a head
				head = node # 1
			#set last element to the tail
			tail = node # 3, 4, 5
			
			#right call
			helper(node.right_ptr)
			
  
	head, tail = None, None 
	helper(root)
	tail.right_ptr = head
	head.left_ptr = tail
	return head
	 



	 
node = TreeNode(4)
node.left_ptr =  TreeNode(2)
node.right_ptr = TreeNode(5)
node.left_ptr.left_ptr = TreeNode(1)
node.left_ptr.right_ptr = TreeNode(3)

res = BTtoLL(node)
print(res.__dict__)

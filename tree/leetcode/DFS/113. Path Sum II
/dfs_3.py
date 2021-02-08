from typing import List
class TreeNode():
	"""docstring for TreeNode"""
	def __init__(self, val):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        def dfs(node, target, slate):
            
            target -= node.val
            slate.append(node.val)
            #base case : leaf nodes
            if not node.left and not node.right and target == 0:
                result.append(slate[:])
            
            #recursive case : internal node    
            if node.left:
                dfs(node.left, target, slate)
                
            if node.right:
                dfs(node.right, target, slate)
                
            # we need extract last element each end of the recursive
            slate.pop()
        
        dfs(root, sum, [])
        return result 

       

node = TreeNode(5)
node.left = TreeNode(4)
node.left.left = TreeNode(11)
node.left.left.left = TreeNode(7)
node.left.left.right = TreeNode(2)

node.right = TreeNode(8)
node.right.left = TreeNode(13)
node.right.right = TreeNode(4)
node.right.right.right = TreeNode(1)
node.right.right.left = TreeNode(5)

sum = 22
result = Solution().pathSum(node, sum)
print(result)


'''
Time compl :  N = scan every each node  and append to the global bax : log N. = T(N LogN)
Space compl : O(NLogn)
'''
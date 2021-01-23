'''
   1
    \
     3
    / \
   2   4
        \
         5
	
	we need a matching current node is equal current parent node val.

	like 
		node = 3 
		node.val == node.parent.val + 1 
			3 	 == 	2
			is not matching
		
		node = 4
			4 = 3+1 
			is match

 --- 
	We can apply DFS - top bottom approach. BFS is not suiatable for this question.
	we can keep a globalans first
	and we can apply dfs top - down 

	if we have matching we can increment global ans

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:

    	if not root:
    		return 0

    	globalans = [0]

    	def dfs(node, parent_val, lengthsofar):
    		
    		if node.val == parent_val +1:
    			lengthsofar += 1 
    		else:
    			lengthsofar = 1 # we need new sequence

    		if lengthsofar > globalans[0]:
    			globalans[0] = lengthsofar

    		#base case : leaf node
    		#we don;t have any process
    		
    		#recursice case
    		if node.left:
    			dfs(node.left, node.val, lengthsofar)

    		if node.right:
    			dfs(node.right, node.val, lengthsofar)


    	dfs(root, float("inf"), 0 )
    	return globalans[0]



node = TreeNode(1)
node.right = TreeNode(3)
node.right.left = TreeNode(2)
node.right.right = TreeNode(4)
node.right.right.right = TreeNode(5)

res = Solution().longestConsecutive(node)
print("res : ", res)




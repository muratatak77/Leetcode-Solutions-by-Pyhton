'''
	Question : 
		102. Binary Tree Level Order Traversal

		Share
		Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

		For example:
		Given binary tree [3,9,20,null,null,15,7],

		    3
		   / \
		  9  20
		    /  \
		   15   7

		return its level order traversal as:
		[
		  [3],
		  [9,20],
		  [15,7]
		] 

	Solution 

		
			We need to iterative level by level for this question. 
			First level = 3 
			second level 9 - 20 

			that's why we can use BFS (Breadth-first Search) iterative method.

			in BFS we need a Queue ( FIFO ) data structure.

			We can add root initial to the Q.

			And until the Q is empty we can iterate for every level items. 
			we can add a temp array after each loop we can add global result array.

'''


# Definition for a binary tree node.

from typing import List
from collections import deque
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        q = deque([root])
        result = []
        while q:
        	#needed refresh temp tree in every q loop
        	temp = []
        	for i in range(len(q)):
        		node = q.popleft()
        		temp.append(node.val)
        		if node.left:
        			q.append(node.left)
        		if node.right:
        			q.append(node.right)
        	result.append(temp)

       	return result



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

res = Solution().levelOrder(root)
print("res : ", res)








        
        

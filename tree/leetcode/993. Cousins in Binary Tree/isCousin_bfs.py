'''
	We can apply level by level iterator > BFS
	First we can check parent's of node.
		If we have match case like node.left.val or node.right.val
			we can check parent is common or not.
			if they have same parent we need to return False
			if they have not the same parent we can return True
'''

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
    	q = deque([root])
    	while q:
    		px, py = None, None
    		for _ in range(len(q)):
    			node = q.popleft()

    			if node.left:
    				q.append(node.left)
    				if node.left.val == x:
    					px = node.val
    				if node.left.val == y:
    					py = node.val

    			if node.right:
    				q.append(node.right)
    				if node.right.val == x:
    					px = node.val
    				if node.right.val == y:
    					py = node.val

    			if (px and py) and (px != py):
    				return True
    	return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

x= 5
y = 4

res = Solution().isCousins(root,x,y)
print("res : ", res)

'''
	O(N) = Each node iterate once in the worst case
	S(N) = Queue store all item once 
'''
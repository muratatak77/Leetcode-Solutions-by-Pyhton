'''
	We can apply level by level traversal so it is BFS
	We need a queue in BFS approach
	We don't care about node values , we just care about level information or tree column id. 
	In a complete binary tree : 
		every level , expect possibly the last, is complettly filled
		All nodes in the last level are as far left as possible.

'''
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        q = deque([(root, 1)])
        expected_id = 1
        col_id = 1
        while q:
        	for _ in range(len(q)):
        		(node, col_id) = q.popleft()
        		if col_id == expected_id:
        			expected_id += 1
        		else:
        			return False

        		if node.left:
        			q.append((node.left, 2*col_id))
        		if node.right:
        			q.append((node.right, 2*col_id+1))
        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)


res = Solution().isCompleteTree(root)
print("res : ", res)

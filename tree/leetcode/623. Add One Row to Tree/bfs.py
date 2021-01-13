'''
	we can use BFS - level by level iterator.
	we need a create left and right node.
	after create these nodes we can set : 
		
		newleft = current_node.left
		newright = current_node.right
		
		and we need to set :

		current_node.left = newleft
		current_node.right = newright

'''


from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
        	return root

        q = deque([root])
        if d == 1:
        	newnode = TreeNode(v)
        	newnode.left = root
        	root = newnode
        	return root

        level = 0 
        while q:
        	level += 1
        	for x in range(len(q)):
        		node = q.popleft()
        		if node.left:
        			q.append(node.left)
        		if node.right:
        			q.append(node.right)

        		if level == d-1:
        			newleft = TreeNode(v)
        			newright = TreeNode(v)
        			newleft.left = node.left
        			newright.right = node.right
        			node.left = newleft
        			node.right = newright
        			break

        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)

v = 1
d = 2 
res = Solution().addOneRow(root,v,d)
print("res : ", res)

'''
	T(N) = O(N)
	S(N) = O(N)
'''
# Definition for a binary tree node.
# look at the stack.png
#   we can use a stack for keep root to left most node.
#   but our most node has a right node , we call again our helper funnction and we can start to fill our stack.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.index = -1
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """

        top_most_node = self.stack.pop()

        if top_most_node.right:
            self._leftmost_inorder(top_most_node.right)

        return top_most_node.val


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# 

node = TreeNode(7)
node.left = TreeNode(3)
node.right = TreeNode(15)
node.right.left = TreeNode(9)
node.right.right = TreeNode(20)

iterator = BSTIterator(node)

print(iterator.next())    # return 3
print(iterator.next())    # return 7
print(iterator.hasNext()) # return true
print(iterator.next())    # return 9
print(iterator.hasNext()) # return true
print(iterator.next())    # return 15
print(iterator.hasNext()) # return true
print(iterator.next())    # return 20
print(iterator.hasNext()) # return false


'''
    T(N) 
    next : we have 2 process. first one is stack pop works in O(1). second call helper function works worst case O(N)
    hasnext : O(1)

    S(N) = O(N) dfs traversal visit all nodes and append stack.

    
'''


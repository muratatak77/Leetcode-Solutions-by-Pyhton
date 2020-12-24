# Definition for a binary tree node.
# 
# BST : most small element being in the most left place
# we can scan the root DFS - inorder. because inorder iterator start left most node.  O(N)
# and we can store these nodes in an array. O(N)
# When we next call we can get by the index O(1) from an array.
# has next we can check the current item index less than array lenght. O(1)
# 
# 
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
        self.sorted_array = []
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.sorted_array.append(root.val)
        self._inorder(root.right)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        self.index += 1
        return self.sorted_array[self.index]


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.index+1 < len(self.sorted_array)


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


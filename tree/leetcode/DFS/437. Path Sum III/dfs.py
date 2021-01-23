'''

    We can apply Top Down - DFS recursive approach.
    We can keep a array as a slate for keep following total and we can iterate than we try to match for a suffix sum.

'''

from collections import defaultdict

class TreeNode():
    """docstring for TreeNode"""
    def __init__(self, val):
        super(TreeNode, self).__init__()
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, _sum):

        if not root:
            return 0

        globalans = [0]

        def dfs(node, target, slate):
            
            slate.append(node.val)
            suffixsum = 0
            for i in range(len(slate)-1,-1,-1):
                suffixsum += slate[i]
                if suffixsum == target:
                    globalans[0] += 1

            #base case
            #we don't need do anything
            
            #recursive case
            if node.left:
                dfs(node.left, target, slate)
            if node.right:
                dfs(node.right, target, slate)

            slate.pop()
        

        dfs(root, _sum, [])
        return globalans[0]


node = TreeNode(10)
node.left = TreeNode(5)
node.left.left = TreeNode(3)
node.left.left.left = TreeNode(3)
node.left.left.right = TreeNode(-2)

node.left.right = TreeNode(2)
node.left.right.right = TreeNode(1)

node.right = TreeNode(-3)
node.right.right = TreeNode(11)

_sum = 8

res = Solution().pathSum(node, _sum)
print("res : ", res)


''' 
    T(N) = O(N) visit for each node once
    S(N) = O(N) slate 
'''
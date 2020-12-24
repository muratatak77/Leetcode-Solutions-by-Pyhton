'''
we can apply prefix  sum algorith in this question

    arr : 1,3,4,6,-7-1

    target = 7

    #situation 1
    curr_sum == target
        count += 1
    
    #situation 2
    count += h[curr_sum - target]

    
    hmap = {1:1, 4:1, 8:1, 14:1, 7:1, 6:1 }
    count = 2


    in tree 

        additional :
         preorder
         root > left > right
         h[curr_sum] -= 1

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

        def preorder(node, curr_sum):
            print("curr_sum : ", curr_sum)
            nonlocal count
            if not node:
                return
            #sum curr sum with the current node val
            curr_sum += node.val

            #sitation 1
            if curr_sum == k:
                count += 1

            #situation 2
            count += h[curr_sum - k]
            h[curr_sum] += 1            
            print("h : ", h)

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            h[curr_sum] -= 1

        h = defaultdict(int)
        count,k = 0, _sum
        preorder(root, 0)
        return count



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
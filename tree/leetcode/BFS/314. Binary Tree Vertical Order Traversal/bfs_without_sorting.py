# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import defaultdict
from collections import deque
from typing import List
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])
        min_col = max_col = 0

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_col = min(min_col, column)
                max_col = max(max_col, column)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        result = []

        for i in range(min_col, max_col+1):
            result.append(columnTable[i])

        return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

res = Solution().verticalOrder(root)
print("res : ", res)

'''
    T(N) = O(N) N is number of nodes
    S(N) = O(N) defaultdict spend time O(N). Worst case , each node has a uniqu column index.
'''

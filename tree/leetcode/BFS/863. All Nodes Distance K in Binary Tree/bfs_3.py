
import collections



'''

	- we need to find  parent each tree
	- we need to count distance for every subtree

	    3
	  /   \
	 5     1
	/ \
   6   2
      / \
     7   4


	node - parent 
	 5        3
	 6        5
	 2        5
	 7        2
	 4        2

	q(node : 5 , d : 0)
	q(node : 6 , d : 1)
	q(node : 2 , d : 1)

	q(node : 7 , d : 2)
	q(node : 4 , d : 2)

	q(node : 3 , d : 1)
	q(node : 1 , d : 2)

	
	return result that we have in q : 7,4,1	

	seen : {5,6,2,3,7,4,1}


'''

class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		# self.parent = None


class Solution(object):
	def distanceK(self, root, target, K):

		def dfs(node, parent = None):
			if node:
				node.parent = parent
				dfs(node.left, node)
				dfs(node.right, node)

		dfs(root)

		q =  collections.deque([(target, 0)])
		seen = {target}

		while q:
			if q[0][1] == K:
				return [node.val for node, d in q]
			node, d = q.popleft()
			for nei in (node.left, node.right, node.parent):
				if nei and nei not in seen:
					seen.add(nei)
					q.append((nei, d+1))

		return []




node  = TreeNode(3)
node.left = TreeNode(5)
node.left.left  = TreeNode(6)
node.left.right  = TreeNode(2)
node.left.right.left  = TreeNode(7)
node.left.right.right  = TreeNode(4)

node.right = TreeNode(1)
node.right.left = TreeNode(0)
node.right.right = TreeNode(8)

target = node.left
K = 2
res = Solution().distanceK(node, target, K)
print("res :", res)     


'''
Complexity Analysis

	Time Complexity: O(N), where N is the number of nodes in the given tree.

	Space Complexity: O(N).

'''       
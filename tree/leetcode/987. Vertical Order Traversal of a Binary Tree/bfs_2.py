'''

	we can use BFS order traversal approach for this problem. 
	BFS : We need a Queue to iterate FIFO method

	 - we can think tree can be a table. 2 dimensional table that we can keep a array : col, row, node.val

	     10 
	    /  \
	   4    8

	for 10 : this is a root. 
	for root  >  col : 0,   row : 0,  val : 10
	for left  >  col : -1,  row : 1,  val : 4
	for right >  col : 1,   row : 1,  val : 8

	node_list = [(0,0,10),(-1,1,4), (1,1,8)]

	- we need to sort. starting most left column 
	
	- we need a hmap for last result array.

		hmap[column] = val
		hmap[-1] = [4,...]
		hmap[0]= [10]
		hmap[1]= [8...]   ... > other coming in right subtree

	- finally we can return hmap.values()

'''
from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def verticalTraversal(self, root):

		node_list = []
		def bfs(root):

			q = deque([(0,0,root)])
			while q:
				col, row, node = q.popleft()
				if node:
					node_list.append((col,row,node.val))
					q.append((col-1,row+1,node.left))
					q.append((col+1,row+1,node.right))

			node_list.sort() # we need to start most left (negative columns)
			print("node_list: ", node_list ) 

			hmap = dict([])
			for column, row, value in node_list:
				if column in hmap:
					hmap[column].append(value)
				else:
					hmap[column] = [value]

			return hmap.values()

		return bfs(root)


node  = TreeNode(10)
node.left = TreeNode(4)
node.left.left  = TreeNode(11)
node.left.right  = TreeNode(8)

node.right = TreeNode(3)
node.right.left = TreeNode(5)
node.right.right = TreeNode(13)

res = Solution().verticalTraversal(node)
print("res :", res)
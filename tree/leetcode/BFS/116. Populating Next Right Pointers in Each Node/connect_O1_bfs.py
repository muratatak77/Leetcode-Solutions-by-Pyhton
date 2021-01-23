
# Definition for a binary tree node.
class Node:
	def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
		self.val = val
		self.left = left
		self.right = right
		self.next = next

class Solution:
	def connect(self, root: 'Node') -> 'Node':
		if not root:
			return None
		leftmost = root

		while leftmost.left:
			#like linkedlist we are using head
			head = leftmost
			while head:

				#connection 1
				head.left.next = head.right

				#connection 2
				##head is not the right child. Head is in the left child side.
				if head.next:
					head.right.next = head.next.left

				#progress continue pass to right side
				head = head.next 

			#move onto next level
			leftmost = leftmost.left


		return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.right = Node(5)

res = Solution().connect(root)
print("res : ", res)

'''
	O(N) = Each node iterate once in the worst case
	S(N) = Queue store all item once 
'''
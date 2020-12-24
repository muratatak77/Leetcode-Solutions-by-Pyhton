class Node(object):

	def __init__(self,data):
		self.data = data
		self.next = None
		self.child = None

class LinkedList(object):

	def printList(self, node):
		temp = node
		while temp:
			print(temp.data, end=" ")
			temp = temp.next
		print()

	def flattenList(self, node):
		tail = self.getTail(node)
		while node:
			if node.child:
				tail.next = node.child
				tail = self.getTail(node.child)
			node = node.next
		return node

	def getTail(self, node):
		while node and node.next:
			node = node.next
		return node

ll = LinkedList()

node = Node(1)
node2 = node.next = Node(2)
node5 = node2.child = Node(5)
node2.child.next = Node(6)

node5.child = Node(10)
node.next.next = Node(3)

node4 = node.next.next.next = Node(4)
node7 = node4.child = Node(7)
node8 = node4.child.next = Node(8)
node4.child.next.next = Node(9)
node7.child = Node(11)
node8.child = Node(12)
node8.child.next = Node(13)

ll.printList(node)
ll.flattenList(node)
ll.printList(node)






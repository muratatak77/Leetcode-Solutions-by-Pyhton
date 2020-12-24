class Node(object):

	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList(object):
	#Function to initialize head
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next

	def hasCycle(self, node):
		fast = node
		slow = node
		length = 0
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if slow == fast:
				length = 1
				slow = slow.next
				while slow != fast:
					slow = slow.next
					length += 1
				return length
		return 0


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.head.next.next.next.next = llist.head

countCycle = llist.hasCycle(llist.head)
print ("Cycle Detected Length : " , countCycle)

# if not hasCycle:
	# llist.printList()
		
		
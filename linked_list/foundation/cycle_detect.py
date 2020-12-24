
#what exactly cycle in ll. 
#where we use cycle detectipn alg. in real world : circular dependency , 
#side effects of cylcle detection : infite loop
#we can data lose if we have cycle detection
#
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
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True
		return False


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.head.next.next.next.next = llist.head

hasCycle = llist.hasCycle(llist.head)
if hasCycle:
	print ("Cycle Detected")
else:
	print ("No Cycle")

if not hasCycle:
	llist.printList()
		
		
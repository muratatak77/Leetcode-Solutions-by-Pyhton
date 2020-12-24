
#
# Complete the 'cloneLinkedList' function below.
#
# The function accepts INTEGER_SINGLY_LINKED_LIST List as parameter.
#

#
# For your reference:
#
class SinglyLinkedListNode:
	def __init__(self, node_data):
		self.data = node_data
		self.next = None
		self.randomPointer = None

	def printList(self, head, stype): 
		node = head 
		while node: 
			if not stype:
				stype = "Default" 
			print(stype, node.data)
			node = node.next
		print("==================")


def printList(head, stype): 
	node = head 
	while node: 
		if not stype:
			stype = "Default" 
		print(stype, node.data)
		node = node.next
	print("==================")


def cloneLinkedList(List):


	if not List:
		return List
	
	#First, we need to clone from original list.
	#when we create new node we can connect from the original node
	#original : A>B>C 
	#after cloned :   A > A` > B > B` > C > C`
	curr = List
	while curr:
		new_node = SinglyLinkedListNode(curr.data)
		new_node.next = curr.next
		curr.next = new_node
		curr = new_node.next

	# second pass. 
	# we need to connect random pointers using by original list
	# if A > C  has random pointer , we can access A` > C`
	# we need to go to head of original list , because we gonna walk trough using by both list
	curr = List

	while curr:
		if curr.randomPointer:
			curr.next.randomPointer = curr.randomPointer.next
		else:
			curr.next.randomPointer = None

		curr = curr.next.next


	#3rd process , we need to back original SinglyLinkedListNode and cloned list. We can break access each other
	ptr_old = List # we gonna keep A>B>C
	ptr_new = List.next # we gonna keep  A'>B'>C'
	res = List.next
	while ptr_old:
		ptr_old.next = ptr_old.next.next
		ptr_new.next = ptr_new.next.next
		ptr_old = ptr_old.next
		prt_new = ptr_new.next
	return res
	

ll = SinglyLinkedListNode("A")
ll.next = SinglyLinkedListNode("B")
ll.next.next = SinglyLinkedListNode("C")

ll.randomPointer = ll.next.next
ll.next.randomPointer = ll

# ll.next.set_randomPointer(ll)
# ll.set_randomPointer(ll.next.next)

res = cloneLinkedList(ll)

printList(res, "res")

# ll.next.next.next = LinkedListNode(4)
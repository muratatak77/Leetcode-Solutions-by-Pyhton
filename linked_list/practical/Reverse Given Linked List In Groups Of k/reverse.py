
class LinkedListNode:
	def __init__(self, node_value):
		self.val = node_value
		self.next = None


def printList(head, stype): 
	node = head 
	while node: 
		if not stype:
			stype = "Default" 
		print(stype, node.val)
		node = node.next
		break

	
def reverseLinkedList(head, k):
	
	# Reverse k nodes of the given linked list.
	# This function assumes that the list contains 
	# atleast k nodes.
	new_head, ptr = None, head
	while k:
		
		# Keep track of the next node to process in the
		# original list
		next_node = ptr.next
		print("next_node : " , printList(next_node, "next_node"))
		# Insert the node pointed to by "ptr"
		# at the beginning of the reversed list
		ptr.next = new_head
		print("ptr.next : " , printList(ptr.next, "ptr.next"))

		new_head = ptr
		print("new_head : " , printList(new_head, "new_head"))
		
		# Move on to the next node
		ptr = next_node
		print("ptr : " , printList(ptr, "ptr"))
		# Decrement the count of nodes to be reversed by 1
		k -= 1
		
		print("new_head : " , printList(new_head, "new_head"))
		print("========================================")


	# Return the head of the reversed list
	return new_head
			

def reverseKGroup(head, k):
	
	count = 0
	ptr = head
	
	# First, see if there are atleast k nodes
	# left in the linked list.
	while count < k and ptr:
		ptr = ptr.next
		count += 1
	
	# If we have k nodes, then we reverse them
	if count == k: 
		
		# Reverse the first k nodes of the list and
		# get the reversed list's head.
		reversedHead = reverseLinkedList(head, k)
		
		# Now recurse on the remaining linked list. Since
		# our recursion returns the head of the overall processed
		# list, we use that and the "original" head of the "k" nodes
		# to re-wire the connections.
		head.next = reverseKGroup(ptr, k)
		return reversedHead
	return head



ll = LinkedListNode(1)
ll.next = LinkedListNode(2)
ll.next.next = LinkedListNode(3)
# ll.next.next.next = LinkedListNode(4)

k = 3

res = reverseKGroup(ll, k)
print(res)
# printList(res)


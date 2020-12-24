
#
# Complete the 'sortLinkedList' function below.
#
# The function accepts INTEGER_SINGLY_LINKED_LIST's head pointer as parameter and 
# returns the head pointer of INTEGER_SINGLY_LINKED_LIST.
#

#
# Definition for SinglyLinkedListNode
#

class SinglyLinkedListNode:
  def __init__(self, node_data):
	  self.data = node_data
	  self.next = None

def printList(head, stype): 
	node = head 
	while node: 
		if not stype:
			stype = "Default" 
		print(stype, node.data)
		node = node.next
	print("-------------------")


def sortLinkedList(head):
	# Write your code here

	if (head is None) or (head.next is None):
		return head

	mid = getMid(head)
	left = sortLinkedList(head)
	right = sortLinkedList(mid)
	return merge(left, right)
	

def merge(list1, list2):
	
	dummyhead = SinglyLinkedListNode(None)
	tail = dummyhead
	
	while list1 and list2:
		if list1.data < list2.data:
			tail.next = list1
			list1 = list1.next
			tail = tail.next
		else:
			tail.next = list2
			list2 = list2.next
			tail = tail.next
	
	if list1 is None:
		tail.next = list2
	else:
		tail.next = list1
	
	return dummyhead.next

def getMid(head):
	if head is None:
		return head

	midPrev = None
	while head and head.next:
		if midPrev:
			midPrev = midPrev.next
		else:
			midPrev = head
		head = head.next.next
	mid = midPrev.next
	midPrev.next = None
	return mid


ll = SinglyLinkedListNode(10)
ll.next = SinglyLinkedListNode(1)
ll.next.next = SinglyLinkedListNode(60)
ll.next.next.next = SinglyLinkedListNode(30)
ll.next.next.next.next = SinglyLinkedListNode(5)


res = sortLinkedList(ll)
printList(res, "res")




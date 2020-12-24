class LinkNode():

	def __init__(self, value):
		self.value = value
		self.next = None


def print_list(node, type):
	curr = node
	while curr:
		print(type, curr.value)
		curr = curr.next
	print("========================")

def reversed_linked_list(curr):

	prev = ""
	next = ""

	while curr:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next

	return prev


def zip_given_linked_list(head):

	print_list(head, "head")
	slow = head
	fast = head.next

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	# 1>2>3>  4>5>6
	print_list(head, "head2")

	list1 = head
	list2 = slow.next

	slow.next = None

	print_list(list1, "list1")
	print_list(list2, "list2")


	# reversed linked list
	list2 = reversed_linked_list(list2)
	print_list(list2, "reversed_linked_list")

	# zip 
	# 1>2>3    
	# 6>5>4
	while list2 :
		next1 = list1.next 
		next2 = list2.next
		list1.next = list2
		list2.next = next1
		list1 = next1
		list2 = next2

	return head


ll = LinkNode(1)
ll.next = LinkNode(2)
ll.next.next = LinkNode(3)
ll.next.next.next = LinkNode(4)
ll.next.next.next.next = LinkNode(5)
ll.next.next.next.next.next = LinkNode(6)

res = zip_given_linked_list(ll)
print_list(res, "res")


		
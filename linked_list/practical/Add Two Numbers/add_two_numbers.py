class SinglyLinkedListNode:
	def __init__(self, data):
		self.data = data
		self.next = None


def printList(head, stype): 
	node = head 
	while node: 
		if not stype:
			stype = "Default" 
		print(stype, node.data)
		node = node.next
	print("-------------------")

def addTwoNumbers(l_a, l_b):
	result = l_b
	# Write your code here
	# printList(l_a, "l_a")
	# printList(l_b, "l_b")

	if not l_b and l_a:
		return None
					
	# we can do regular summaziation process for linked list respectively
	# we can store lb sum results, hence we can finally lb
	# we need walk trough both la and lb linked lists
	# we need sum and carryforward params
	sum, carryforward = 0,0
	
	# if we get one of linkedlists null we can finish the while iterator
	while True:
		sum = l_a.data + l_b.data + carryforward # regular sum
		l_b.data = sum%10 #if sum is 14 we need just 4
		carryforward = sum//10 # if sum 14 we need just 1
		if l_a.next == None or l_b.next == None:
			break
		l_a = l_a.next
		l_b = l_b.next
	
	printList(l_a, "l_a")
	printList(l_b, "l_b")

	# if we have still remain node in l_a list, we can add l_a next to l_b next
	if l_a.next != None and l_b.next == None:
		l_b.next = l_a.next
	

	# if we have carryforward and l_b.next have still node we need to iterator remainng sum and carryforward
	while (carryforward > 0) and (l_b is not None) and (l_b.next != None):
		l_b = l_b.next
		sum = l_b.data + carryforward
		l_b.data = sum%10
		carryforward = sum//10
	
	# still have carryforward we need new node
	if carryforward > 0:
		node = SinglyLinkedListNode(carryforward)
		l_b.next = node
	
	return result
		

ll = SinglyLinkedListNode(9)
ll.next = SinglyLinkedListNode(9)
ll.next.next = SinglyLinkedListNode(9)
ll.next.next.next = SinglyLinkedListNode(9)


ll2 = SinglyLinkedListNode(9)
ll2.next = SinglyLinkedListNode(9)
ll2.next.next = SinglyLinkedListNode(9)
ll2.next.next.next = SinglyLinkedListNode(9)

res = addTwoNumbers(ll, ll2)

printList(res, "res")

# Complete the function below.

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None


def printList(head): 
    node = head 
    while node: 
        print(node.val) 
        node = node.next


def find_count(head):
    count = 0
    node = head
    while node:
        count += 1
        node = node.next
    return count
    
def swap_nodes(head, k):
    
    # if k < 1:
    #     return head
    
    n = find_count(head)

    print("n : ", n)
    
    if not n:
        return head
        
    if n > 100000 or n < 1:
       return head
    
    if n < k:
        return head
    
    # if k and n same node
    if (2*k-1) == n:
       return head
    
    #we need find kth element of  start beginning of linkedlist
    x = head
    x_prev = LinkedListNode(None)
    for i in range(k-1):
        x_prev = x
        x = x.next
    
    # we need find kth element of end of linkedlist
    y = head
    y_prev = LinkedListNode(None)
    for i in range(n-k):
        y_prev = y
        y = y.next
        
     # 1>2>3>4>5>6>7
     # k = 2
     # 1>6   5>2  
    if x_prev:
        x_prev.next = y
    if y_prev:
        y_prev.next = x
        
    # 2>7  6>3
    temp = x.next
    x.next = y.next
    y.next = temp
    
    #changed head pointers 
    if k == 1:
        head = y
    if k == n:
        head = x
    
    return head


ll = LinkedListNode(1)
ll.next = LinkedListNode(2)
ll.next.next = LinkedListNode(3)
ll.next.next.next = LinkedListNode(4)

k = 2

res = swap_nodes(ll, k)
printList(res)


    
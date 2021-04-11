'''
    We can generate a LRU Cache system using by DoubleLinkedList and Hashmap
    The problem can be solved with a hashmap that keeps track of the keys and its values in the double linked list
    Put , get will be take O(1) time. 
    
    like 
    Initial we can generate HEAD and TAIL

    HEAD  >  TAIL
          <

    and we will create like this sttunctre with nodes.

    HEAD  >  NODE - key1 , value1 -  >   NODE - key2 , value2  > TAIL 
          <                          <                         <
'''


class DoubleLinkedList(object):
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

class LRUCache(object):
    """docstring for LRUCache"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head, self.tail = DoubleLinkedList(), DoubleLinkedList()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):

        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):

        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key):

        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.val

    def put(self, key, val):
        
        node = self.cache.get(key)

        if not node:
            newnode = DoubleLinkedList()
            newnode.key = key
            newnode.val = val

            self.cache[key] = newnode
            self._add_node(newnode)
            self.size += 1

            if self.size > self.capacity:
                #pop tail
                tail = self._pop_tail()
                del cache[tail.key]
                self.size -= 1

        else:

            node.val = val
            self._move_to_head(node)

        

lru = LRUCache(2)
lru.put(1, 1) #cache is {1=1}
lru.put(2, 2)
l1 = lru.get(1)
print(l1)

l2 = lru.get(2)
print(l2)


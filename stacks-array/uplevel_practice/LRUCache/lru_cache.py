# Complete the function below.

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache():
    
    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        
        # One particularity about the double linked list implemented here is 
        # that there are pseudo head and pseudo tail to mark the boundary, 
        # so that we don't need to check the null node during the update.

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node):
        #remove the existing node from the Dlinked list
        # head > node > node2
        # we will remove node
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
        
    def _add_node(self, node):
        #always add the new node right after head
        #node3
        #head >  <   node3 > <   node2 >< tail

        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_head(self, node):
        #move certain node in between to the head
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        #pop the current tail
        
        res = self.tail.prev
        self._remove_node(res)
        return res
        
    def get(self, key):
        
        #check cache
        node = self.cache.get(key, None)
        if not node:
            return -1
            
        #move the accessed node to the head
        self._move_to_head(node)
        return node.value
    
    def put(self, key, value):

        node = self.cache.get(key)

        if not node:
            print("No node, we'll create. key : ", key , " - value:", value)
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1
            
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)

    
def implement_LRU_cache(capacity, query_type, key, value):
    
    lru = LRUCache(capacity)
    res = []

    for i in range(len(query_type)):

        k = key[i]
        v = value[i]
        t = query_type[i]
        if t == 1:
            lru.put(k, v)
        elif t == 0:
            res.append(lru.get(k))

    return res



capacity    = 2
query_type  = [1,  1,  0,  1,   0,  1, 0]
key     = [5, 10, 5, 15, 10, 5, 5]
value   = [11, 22, 1, 33, 1, 55, 1]
ans = implement_LRU_cache(capacity, query_type, key, value)
print(ans)




"""
The problem can be solved with a hashmap that keeps track of the keys and its values in the double linked list. 
Put, get and remove operations work in O(1)

head >  Key,Value >   Key,Value   >  Key,Value >  tail
	 < 			  <

"""

class DLinkedNode(object):

	def __init__(self):
		self.key = 0
		self.value = 0
		self.prev = None
		self.next = None


class LRUCache(object):

	def __init__(self, capacity):
		self.cache = {}
		self.size  = 0
		self.capacity = capacity
		self.head, self.tail = DLinkedNode, DLinkedNode

		# One particularity about the dlinklist implemented here us that there are pseudo head and pseudo tail  to mark the boundary
		# ,so that we don't need to check the null node during the update.
		self.head.next = self.tail
		self.tail.prev = self.head

	def get(self, key):
		node = self.cache.get(key, None)
		if not node:
			return -1

		#move to accessed node to the head
		self._move_to_head(node)
		return node.value

	def put(self, key, value):
		
		node = self.cache.get(key)


		if not node:
			#append new node
			newNode = DLinkedNode()
			newNode.key = key
			newNode.value = value
			self.cache[key] = newNode
			self._add_node(newNode)
			self.size += 1

			if self.size > self.capacity:
				#pop the tail
				tail = self._pop_tail()
				del self.cache[tail.key]
				self.size -= 1
		else:
			#update exists node
			node.value = value
			self._move_to_head(node)
		
	def _add_node(self, node):
		#always add the new node right after head
		node.prev = self.head
		node.next = self.head.next

		self.head.next.prev = node
		self.head.next = node

	def _pop_tail(self):
		#pop the current tail
		res = self.tail.prev
		self.__remove_node(res)
		return res 

	def __remove_node(self, node):
		prev = node.prev
		new = node.next
		prev.next = new
		new.prev = prev
	
	def _move_to_head(self, node):
		self.__remove_node(node)
		self._add_node(node)
		#move certain node in between to the head.
		

lRUCache = LRUCache(2)
p1 = lRUCache.put(1, 1); # cache is {1=1}
p2 = lRUCache.put(2, 2); # cache is {1=1, 2=2}
p3 = lRUCache.get(1);    # return 1
p4 = lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
p5 = lRUCache.get(2);    # returns -1 (not found)
p6 = lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
p7 = lRUCache.get(1);    # return -1 (not found)
p8 = lRUCache.get(3);    # return 3
p9 = lRUCache.get(4);    # return 4

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)

		

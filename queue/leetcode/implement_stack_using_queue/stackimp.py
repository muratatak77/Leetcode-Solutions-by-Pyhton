from collections import deque

class MyStack(object):
	
	""" 
		in this question, we implement a stack by using a queue. We have just one stack and one queue.
		problem is we use a queue that it works FIFO. But we want the LIFO cycle, and we need to change FIFO to LIFO.
	"""

	def __init__(self):
		self.queue = deque()
		self.size = 0

	#in the worst case O(n).
	def push(self,x):
		self.queue.append(x)
		for i in range(self.size):
			self.queue.append(self.queue.popleft())
		self.size += 1

	#O(1)
	def pop(self):
		if self.size == 0:
			return None
		self.size -= 1
		return self.queue.popleft()
		
	#O(1)
	def top(self):
		if self.size == 0:
			return None
		return self.queue[0]

	#O(1)
	def empty(self):
		return self.size == 0


stack = MyStack();
p1 = stack.push(1);
print("p1 : ", stack.queue)

p2 = stack.push(2);  
print("p2 : ", stack.queue)

p3 = stack.push(3);  
print("p3 : ", stack.queue)

top = stack.top();   # returns 2
print("top : ", top)

pop = stack.pop();   # returns 2
print("pop : ", pop)

print("p4 : ", stack.queue)
stack.empty(); # returns false
from collections import deque

class MyQueue(object):
    def __init__():
        enqueue_stack = deque()
        dequeue_stack = deque()
        self.size = 0

    # s1 = 1,2,3
    # s2 = 
    
    def push(self, val):
        self.enqueue_stack.append(val)
        self.size += 1

    def pop(self):

        if self.size == 0:
            return None
        
        self.size -= 1

        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack.pop()

        while len(self.enqueue_stack) != 0:
            item = self.enqueue_stack.pop()
            self.dequeue_stack.append(item)

        return self.dequeue_stack.pop()

    def peek(self):

        if self.size == 0:
            return None

        if len(self.dequeue_stack) > 0:
            d_size = len(dequeue_stack)-1
            return self.dequeue_stack[d_size]

        while len(self.enqueue_stack) != 0:
            item = self.enqueue_stack.pop()
            self.dequeue_stack.append(item)

        return self.dequeue_stack[len(dequeue_stack)-1]
    
    def empty(self):
        
        return self.size == 0
        

# Explanation

# ["MyQueue","push","pop","empty"]

myQueue = MyQueue();
myQueue.push(1);

pop1 = myQueue.pop(); # return 1
print("pop1: ", pop1 )
print()


isempty = myQueue.empty(); # return False
print("isempty : " , isempty)



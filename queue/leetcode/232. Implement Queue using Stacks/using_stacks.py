from collections import deque

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enqueu_stack = deque()
        self.dequeu_stack = deque()
        self.size = 0


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.enqueu_stack.append(x)
        self.size += 1
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.size == 0:
            return None

        self.size -= 1

        if len(self.dequeu_stack) > 0:
            return self.dequeu_stack.pop()

        while len(self.enqueu_stack) != 0:
            self.dequeu_stack.append(self.enqueu_stack.pop())

        return self.dequeu_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.size == 0:
            return None
        if len(self.dequeu_stack) > 0:
            return self.dequeu_stack[len(self.dequeu_stack)-1]

        #Need to transfer enqueue_stack into dequeue_stack
        while len(self.enqueu_stack) != 0:
            self.dequeu_stack.append(self.enqueu_stack.pop())
        
        return self.dequeu_stack[len(self.dequeu_stack)-1]            

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
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



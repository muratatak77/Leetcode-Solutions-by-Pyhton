from collections import deque

class MyQueue():

    def __init__(self):
        self.stack = deque() 

    def enqueu(self, x):
        if not self.stack:
            self.stack.append(x)
        else:
            item = self.stack.pop()
            self.enqueu(x)
            self.stack.append(item)

    def dequeu(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.top()

    def empty(self):
        return not self.stack


myQueue = MyQueue();
myQueue.enqueu(1);
myQueue.enqueu(2);
myQueue.enqueu(3);
myQueue.enqueu(4);

pop1 = myQueue.dequeu(); # return 1
print("pop1: ", pop1 )

myQueue.enqueu(5);


isempty = myQueue.empty(); # return False
print("isempty : " , isempty)

print(myQueue.stack)

pop2 = myQueue.dequeu(); # return 1
print("pop2: ", pop2 )





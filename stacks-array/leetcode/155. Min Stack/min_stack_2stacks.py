class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack  = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
p1 = minStack.push(-2);
p2 = minStack.push(0);
p3 = minStack.push(-3);
p4 = minStack.getMin(); # return -3
p5 = minStack.pop();
p6 = minStack.top();    # return 0
p7 = minStack.getMin(); # return -2

print(p4)
print(p5)
print(p6)
print(p7)
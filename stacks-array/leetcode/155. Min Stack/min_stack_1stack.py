class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack  = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #we can define doudle elements in one stack item. (x,x) second element will be always min element.
        #first element will be current element. When we need min element we should get second item. 
        if not self.stack:
            self.stack.append((x,x))
            return
        current_min = self.stack[-1][1]
        self.stack.append((x, min(x,current_min)))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


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
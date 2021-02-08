from collections import deque
class QueuewithMaxAPI(object):
    """docstring for QueuewithMaxAPI"""
    def __init__(self):
        self.maxq, self.myq = deque(), deque()

    def push(self, val):
        self.myq.append(val)
        while self.maxq and self.maxq[-1] < val:
            self.maxq.pop()
        self.maxq.append(val)

    def pop(self):
        val = self.myq.popleft()
        if val == self.maxq[0]:
            self.maxq.popleft()
        return val

    def getMax(self):
        return self.maxq[0]

    def empty(self):
        return len(self.myq) != 0



q = QueuewithMaxAPI()
q.push(6)
q.push(2)
q.push(3)
q.push(5)

print(q.maxq)

p1 = q.pop()
print(p1)

print(q.maxq)

p2 = q.getMax()
print("p2 : ", p2)
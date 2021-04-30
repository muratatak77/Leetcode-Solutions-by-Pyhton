'''
    We can use a Queue - FIFO datya structure. 
    We can add coming input number to the Q.
    And we can keep a total that is calling totalsofar.

        if grater than avarage number from the lenght  of q 
            we can popleft from q and we can substract from rhe totalsofar

    we can return avarega

'''
from collections import deque
import math

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.totalsofar = 0
       
    def next(self, val: int) -> float:

        self.totalsofar += val
        self.q.append(val)
        if len(self.q) > self.size:
            self.totalsofar -= self.q.popleft()

        return self.totalsofar / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)

param_1 = obj.next(1)
print(">>param_1 : ", param_1)
print("==============================")

param_2 = obj.next(10)
print(">>param_2 : ", param_2)
print("==============================")

param_3 = obj.next(3)
print("param_3 : ", param_3)
print("==============================")

param_4 = obj.next(5)
print("param_4 : ", param_4)
print("==============================")

param_5 = obj.next(5)
print("param_5 : ", param_5)
print("==============================")


''''
	T(N) = O(1)
	S(N) = O(size)
'''
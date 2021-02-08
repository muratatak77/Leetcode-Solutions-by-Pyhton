'''
	We can use Queue - FIFO data structure
	We can keep a total as a totalsofar.
	first we can add val to the totalsofar
	we can append to the q val
	if our q size grater than given a size we can substract from the totalsofar by using q popleft.

	q []
	
	1 
	[1]
	
	10 push q : [1][10]

	3 push q : [1][10][3] 

	5 push  [1][10][3][5]. size is override,  we can do q.popleft() extract from q left. : [10][3][5]


'''
from collections import deque
import math

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.totalsofar = 0
        self.q = deque()
       
    def next(self, val: int) -> float:
    	print("Q initial: ", self.q, " VAL : ", val)

    	self.totalsofar += val
    	print("		self.totalsofar : ", self.totalsofar)
    	self.q.append(val)
    	print("			Q initial: ", self.q)
    	print("			len(self.q): ", len(self.q))

    	if len(self.q) > self.size:
    		self.totalsofar -= self.q.popleft()
    		print("			self.q.popleft() : ", self.q)

    	# return math.ceil(self.totalsofar / self.size)
    	print("		LAST self.totalsofar : ", self.totalsofar)
    	return self.totalsofar // len(self.q)

       	 


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
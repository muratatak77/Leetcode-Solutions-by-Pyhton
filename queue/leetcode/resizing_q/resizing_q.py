class MyCircularQueue:

    
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.array = [-1] * k #initialize an array (empty queue) of size k
        self.capacity = k
        self.size = 0 #number of elements in the queue

        #Head and Tail point to the index of the first & last elements in queue
        self.head = -1
        self.tail = -1
 
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size == 0: 
            self.array[0] = value
            self.head = 0
            self.tail = 0
            self.size = 1
        else:
            if self.size == self.capacity: #is full
                self.resize(2*self.capacity)
            self.tail = (self.tail+1) % self.capacity
            self.array[self.tail] = value
            self.size += 1 
            #Tail moved to the right and value inserted at its new index
        return True


    def resize(self, newcapacity):
        newarray = [-1]*newcapacity
        nextindex = 0
        #copy elements from old array into new array
        while  self.head != self.tail:
            newarray[nextindex] = self.array[self.head]
            print("head : ", self.head , " tail : ", self.tail)
            nextindex += 1
            self.head = (self.head + 1 ) % self.capacity   #we moved head in the current queue
            print("newarray : ",newarray)
            print(" >> head : ", self.head , " tail : ", self.tail)
        
        if self.head == self.tail:
            newarray[nextindex] = self.array[self.head]
            self.head = (self.head + 1 ) % self.capacity   #we moved head in the current queue
            nextindex += 1

        self.array = newarray
        self.head = 0
        self.tail = nextindex - 1
        self.capacity = newcapacity 

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        
        if self.size == 0:
            return False
        if self.size == 1:
            self.array[self.head] = -1
            self.head = -1
            self.tail = -1
            self.size = 0
        else:
            self.array[self.head] = -1
            self.head = (self.head+1) % self.capacity
            self.size -= 1


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.size == 0:
            return -1
        else:
            return self.array[self.head]


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """

        if self.size == 0:
            return -1
        else:
            return self.array[self.tail]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity




circularQueue = MyCircularQueue(7); # set the size to be 3
print(circularQueue.array)

circularQueue.enQueue("E");  # return true
circularQueue.enQueue("F");  # return true
circularQueue.enQueue("G");  # return true
circularQueue.enQueue("H");  # return false, the queue is full
circularQueue.enQueue("I");  # return false, the queue is full
circularQueue.enQueue("J");  # return false, the queue is full
circularQueue.enQueue("K");  # return false, the queue is full

print(circularQueue.array)

# rear = circularQueue.Rear();  # return 3
# print("rear :", rear)

isFull = circularQueue.isFull();  # return true
print("isFull : ", isFull)

# circularQueue.deQueue();  # return true
# print("after  deQueue: ", circularQueue.array)

circularQueue.enQueue("L");  # return true
print("after  enQueue 4 : ", circularQueue.array)

# rear = circularQueue.Rear();  # return 4
# print("rear : ", rear)

print("Final : ", circularQueue.array)

 

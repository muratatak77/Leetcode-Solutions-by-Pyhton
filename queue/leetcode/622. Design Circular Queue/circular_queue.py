class MyCircularQueue:

    #Based on the description of the problem, data structer that meets all the requirements would be a ring where the head and the tail are adjacent to each other.
    #We don't have a ring data structer in any programming language. Similar data structure we called Array which is a collection of elements continuously in one dimensional space.
    
    #in this case, to build a circular queue, we could form a virtual ring structure with the Array
    # given a fixed array, any of the elements could be considered as a head in a queue. As long as we know the lenght of the queue , 
    # we than can instantly locate its tail, based on the getting tail index and getting mod capacity
    
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
            if self.size == self.capacity:
                return False
            self.tail = (self.tail+1) % self.capacity
            self.array[self.tail] = value
            self.size += 1 
            #Tail moved to the right and value inserted at its new index
        return True

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




circularQueue = MyCircularQueue(3); # set the size to be 3
print(circularQueue.array)

circularQueue.enQueue(1);  # return true
circularQueue.enQueue(2);  # return true
circularQueue.enQueue(3);  # return true
circularQueue.enQueue(4);  # return false, the queue is full
print(circularQueue.array)

rear = circularQueue.Rear();  # return 3
print("rear :", rear)

isFull = circularQueue.isFull();  # return true
print("isFull : ", isFull)

circularQueue.deQueue();  # return true
print("after  deQueue: ", circularQueue.array)

circularQueue.enQueue(4);  # return true
print("after  enQueue 4 : ", circularQueue.array)

rear = circularQueue.Rear();  # return 4
print("rear : ", rear)

print("Final : ", circularQueue.array)

'''
    we can generate for every nums object a hash map  that it will keep non zero items.
    in dotProduct we can match 2 hashmap. If the same key has in 2 hash map, we can multiply.
    like 

    nonzeros1 :  {0: 1, 3: 2, 4: 3}
    nonzeros2 :  {1: 3, 3: 4}
    
    we have just {3: 2} , {3: 4} same key. 
    we can multiply 2*4 = 8
'''

from typing import List
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i,n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

        print("nonzeros : ", self.nonzeros)

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        
        for i,n  in self.nonzeros.items():
            print("i : ", i , " - n :", n)
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]

        print("result : ",result)
        return result
        

# Your SparseVector object will be instantiated and called as such:
nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)

print("ans : ", ans)


'''
    T(N) = O(N)  N is length of array , O(M) M is number of nonzero elements
    S(N) = O(M) for creating hash map, as we able store the element that non-zero.
'''
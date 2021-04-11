from typing import List
class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
    	result = 0

    	# for num1,num2 in zip(self.array,vec.array):
    	for i in range (len(self.array)):
    		num1 =  self.array[i]
    		num2 = vec.array[i]
    		if num1 != 0 and num2 != 0:
    			result += num1 * num2

    	return result

# Your SparseVector object will be instantiated and called as such:
nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)

print("ans : ", ans)


'''
	T(N) = O(N)
	S(N) = O(1)
'''
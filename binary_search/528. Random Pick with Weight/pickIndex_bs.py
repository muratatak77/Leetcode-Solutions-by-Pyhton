import random
from typing import List
class Solution:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

        print("prefix_sum : ", self.prefix_sums)
        print("total_sum : ", self.total_sum)
        print("--------------------------")

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        #lets us imagine that there are is a line in the space.
        #always large number would occupy a broader range on the line compared to a small number.
        #For exp : for th enumber 9 shuould be eaxtly nine times as the range for the number 1
        target = self.total_sum * random.random()

        # we can apply BS to find in array.
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high-low) // 2 #we follow this way because we need to prevent out of bound int numbers
            if target > self.prefix_sums[mid]:
                low = mid +1
            else:
                high = mid
        return low



# Your Solution object will be instantiated and called as such:
w = [1,2,3,4,5,6]
obj = Solution(w)
param_1 = obj.pickIndex()
print("param_1 : ", param_1)
param_2 = obj.pickIndex()
print("param_2 : ", param_2)



'''
    T(N) = Construction will be O(N)
        pickIndex will be O(logN), we did binary search

    S(N) = Construction will be O(N) , pickIndex method will be O(1) we don't use any extra space in pikckIndex method.

'''
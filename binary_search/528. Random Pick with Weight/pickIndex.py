'''
	We need to unerstand first how to get weight in a array.
	like = [1,2,3]
		index 0 = 1 / 1+2+3 = 1/6   should be just 1 option
		index 1 = 2 / 1+2+3 = 2/6 	should be just 2 option
		index 2 = 3 / 1+2+3 = 3/6	should be just 3 option

	How to get randomly pick and probability of an index being chosen should depend on its % contrubution to overall weight.
		- We can generate a random number  using a random method.
		- we need a sum to find weight to seperate some parts in weight array

		like :
		wt = [1,2,3]

		cumulative sum or prefix sum will be : [1,3,6]

		we can accross : 
			index 0   1  2
			wt = [1 , 2, 3]

			ps = [1,  3, 6]

			means : 
			0----1-------3------------6

			if we genarete a bucket will be: 
				0,1    1,3		3,6

			like if we have random number 2.04 will be index 1 because 1,3 bucket include 2.04
			if target < prefix sum 
				return index

		
'''
import random
from typing import List
class Solution:

	def __init__(self, w: List[int]):
		"""
		:type w: List[int]
		"""
		self.prefix_sum = []
		psum = 0
		for wt in w:
			psum += wt
			self.prefix_sum.append(psum)
		
		self.total_sum = psum

	def pickIndex(self) -> int:
		"""
		:rtype: int
		"""
		target = self.total_sum * random.random() # we generate a random number between 0 and 1
		print("target : ", target)
		i = 0
		for psum in self.prefix_sum:
			if target < psum:
				return i
			i += 1

# Your Solution object will be instantiated and called as such:
w = [1,2,3]
obj = Solution(w)
param_1 = obj.pickIndex()
print("param_1 : ", param_1)
param_2 = obj.pickIndex()
print("param_2 : ", param_2)


'''
	T(N) = 
		Construction will be O(N) we iterated N times. 
		pickIndex wiil be O(N)

	S(N) = Construction will be O(N) , pickIndex method will be O(1) we don't use any extra space in pikckIndex method.

'''
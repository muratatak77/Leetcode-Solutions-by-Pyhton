'''
	we can apply decrease & conquer alg. in this question
	I have a lazy manager and I have my sub ordinates.

	My goal bring the largest element to the right most and flip right to left in the each iterate process.

	like  arr= [3, 2, 4, 1]

		my item is first 1 and others will be my subordinates.

		first item is 1 and right most item should be largest most item so it is 4. 
		we need to bring 4 instead of 1. 
		we can match first 
			arr[i] != i+1
				i=3
				1 != 4
				that's not equal.
				we need second iterate to find matching.
					start j is 2 
						arr[j] == i+1
							4 == 4
							we found 4 we can break second iterate and we can start flips


				first flip will be start j to the left
					j = 2  , start 4 and reverse to the left : 4,2,3,1
				second flip will be staring i to the left
					i = 3 , start 1 and reverse : 1,3,2,4



Logs : 

ARRAY :  [3, 2, 4, 1]
 i :  3
   arr[i] : 1  / i+1 : 4
      j : 2
         arr[j] : 4  / i+1: 4
			BREAK
						J+1 flip : [4, 2, 3, 1]
						I+1 flip : [1, 3, 2, 4]
-------------------------------------------------------
 i :  2
   arr[i] : 2  / i+1 : 3
      j : 1
         arr[j] : 3  / i+1: 3
			BREAK
						J+1 flip : [3, 1, 2, 4]
						I+1 flip : [2, 1, 3, 4]
-------------------------------------------------------
 i :  1
   arr[i] : 1  / i+1 : 2
      j : 0
         arr[j] : 2  / i+1: 2
			BREAK
						J+1 flip : [2, 1, 3, 4]
						I+1 flip : [1, 2, 3, 4]
-------------------------------------------------------


'''


from typing import List
class Solution:
	def pancakeSort(self, arr: List[int]) -> List[int]:

		n = len(arr)
		result = []
		for i in range(n-1,-1,-1):
			if arr[i] != i+1:
				for j in range(i-1,-1,-1):
					if arr[j] == i+1:
						break


				#flips j and i
				arr[:j+1] = arr[:j+1][::-1]
				arr[:i+1] = arr[:i+1][::-1]

				result.append(j+1)
				result.append(i+1)

		return result

arr = [3,2,4,1]
res = Solution().pancakeSort(arr)
print("res : ", res)


'''
	T(N) = O(N^2) We have looops inside flips operation
	S(N) = O(1) there is no extra space
'''
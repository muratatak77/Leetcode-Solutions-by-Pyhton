'''
	We can solve to seperate 2 parts in solving. 
		1 - We try to get ideal list (almost sorting list but not exactly sorted list) from original list
		2 - find missing item
	
		1 - we can iterate all list
			as logic ideal list should be like :  [1,2,3,4,5,6,7....n] , so means nums[i] ,nums[i+1] .... 
			we can check as first logic next item is usefull  for ideal list.

				for i range 0,n
					while nums[i] != i+1

						if we have an usefull case we need a destination :
							
							d = nums[i] - 1

							meaning we need to swap current item and destination or right place item.
								swap(nums[i], nums[d])


		2 - We got a ideal list to solve and we can find missing numbers
			for i in 0, n
				if nums[i] !+ i+1
					result.append(i+1)

'''

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

    	n = len(nums)
    	for i in range(0,n):
    		print("i : ", i)
    		while nums[i] != i+1:

    			d = nums[i]-1
    			print("	d : ", d)

    			if  nums[d] != nums[i]:
    				nums[d], nums[i] = nums[i], nums[d]
    				print("		After swap :" , nums)
    			else:
    				print("		Break...")
    				break
    	print("nums 2: ", nums)

    	result = []
    	for i in range(0,n):
    		print("nums[i] != i+1  / " , nums[i], " != ", i+1)
    		if nums[i] != i+1:
    			result.append(i+1)

    	return result



nums = [4,3,2,7,8,2,3,1]
# nums = [1,2,9,2,8,7,3,2,6]

res = Solution().findDisappearedNumbers(nums)
print("res : ", res)


'''
	T(N) = O(N) iterate all list
	S(N) = O(1) we have result as a extra space. If we think worst case, we never loop all list. 
'''
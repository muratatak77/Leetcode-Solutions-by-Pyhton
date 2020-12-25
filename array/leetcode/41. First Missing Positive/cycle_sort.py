'''
	we can apply cycle sort approach in this question.
	we have 2 parts:
	first parts : 
		try to get ideal nums list. Means get a almost sorting list.
		we can walk trough in a loop 
			if we have a difference expect list items.
				we need a expect value we can say destination and we can call 'd'
				if this destination beetween 0 and n  and expect value is not same
				we can swap to put a right place current item.

	second part:
	classic loops and check current item is not equal expect item (i+1)
		if we have a different items we can return i + 1

	no we can return n+1

'''

from typing import List

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		i = 0
		n = len(nums)
		for i in range(n):

			#expect value for ideal list
            #if we have [1,2,0] we need a ideal list : [1,2,0]
            #so destination value nums[i]-1
        
			while nums[i] != i+1:
				print(" i :", i)
				d = nums[i] - 1
				# sanity check - duplicate check
				# put num[i] to the correct place if nums[i] in the range [1, n]
				print("	d : ", d)
				
				try:
					print("		check to swap, nums[i] :", nums[i], " - nums[d] :", nums[d] )
				except Exception as e:
					print("")

				if 0 <= d < n and nums[i] != nums[d]:
					print("			start swap, nums[i] :", nums[i], " - nums[d] :", nums[d] )
					nums[i], nums[d] = nums[d], nums[i]
					print("			AFTER swap, nums :", nums)

				else:
					break

		print("nums : ", nums)

		# so far, all the integers that could find their own correct place 
		# have been put to the correct place, next thing is to find out the
		# place that occupied wrongly
		for i in range(n):
			print(" i : ", i)
			if nums[i] != i + 1:
				print("we will return i + 1 : ", i+1)
                # if we have [1,2,0] case we need return 3 = i+1
				return i + 1

		print("we will return n + 1 : ", n+1)
		#in [1,2,3] case our answer will be 4. n = 3 + 1 = 4
		return n + 1



nums = [7,8,9,11,12]
nums = [3,4,-1,1]
# nums = [1,2,3]
# nums = [1,2,0]
res = Solution().firstMissingPositive(nums)
print("res : ", res)

'''
	T(N) = O(N) Just 1 while and 1 for loop
	S(N) = O(1) No extra space using
'''
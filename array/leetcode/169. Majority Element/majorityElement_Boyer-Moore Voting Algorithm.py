class Solution:
	def majorityElement(self, nums):
		count = 0
		candidate = None

		for num in nums:
			print("num : ", num)
			if count == 0:
				candidate = num
				print("	candidate:", candidate)
				
			if num == candidate:
				count += 1
				print("		Inc count : " , count)
			else:
				count += -1
				print("		Dec count : " , count)
			print("----------------------------------------")


			count += (1 if num == candidate else -1)

		return candidate


#As per the question, there always exists a majority element in an array whose count is always greater than n/2(n - being the size of the array). Not even equal to n/2.
nums = [2,2,1,1,1,2,2]
nums = [2,2,2,2,2,2,4,4,4,4,4]
res = Solution().majorityElement(nums)
print("res : ", res)

'''
	T(N) = O(N)
	S(N) = O(1)
'''
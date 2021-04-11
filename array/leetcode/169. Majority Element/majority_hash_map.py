class Solution:
	def majorityElement(self, nums):
		count = {}

		for num in nums:
			if num in count:
				count[num] += 1
			else:
				count[num] = 1

		print("count :", count)

		max_item = 0
		result = 0

		for key in count.keys():
			print("	key : ", key)
			if count[key] > max_item:
				max_item = count[key]
				result = key

		return result



#As per the question, there always exists a majority element in an array whose count is always greater than n/2(n - being the size of the array). Not even equal to n/2.
nums = [2,2,1,1,1,2,2]
nums = [2,2,2,2,2,2,5,6,7,8,4,3,3,5,64,4,4,5,6,8,9,9,5,4,4,4,4]
res = Solution().majorityElement(nums)
print("res : ", res)

'''
	T(N) = O(N)
	S(N) = O(N)
'''
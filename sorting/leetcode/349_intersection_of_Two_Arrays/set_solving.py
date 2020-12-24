class Solution(object):

	def intersection(self, nums1, nums2):

		nums1 = set(nums1)
		nums2 = set(nums2)

		res = []
		if len(nums1) < len(nums2):
			res = self.helper(nums1, nums2)
		else:
			res = self.helper(nums2, nums1)
		return res

	def helper(self, set1, set2):
		res = []
		for i in set1:
			if i in set2:
				res.append(i)
		return res
		


nums1 = [1,2,2,1]
nums2 = [2,2]


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

arr  = Solution().intersection(nums1, nums2)
print("Result : " + str(arr))


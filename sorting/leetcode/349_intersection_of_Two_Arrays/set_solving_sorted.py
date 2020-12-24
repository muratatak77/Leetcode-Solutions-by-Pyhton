class Solution(object):

	def intersection_sorted(self, nums1, nums2):

		hmap = {}
		i = 0 
		j = 0
		n = len(nums1)
		m = len(nums2)

		while i < n-1 and j < m-1:
			if nums1[i] == nums2[j]:
				hmap[nums1[i]] = i
				i += 1
				j += 1
			elif nums1[i] > nums2[j]:
				j += 1
			else:
				i += 1

		return [*hmap]

nums1 = [1,1,2,2,3,6,9,78]
nums2 = [2,2,3,4,4,5,6,6,7]

arr  = Solution().intersection_sorted(nums1, nums2)
print("Result : " + str(arr))


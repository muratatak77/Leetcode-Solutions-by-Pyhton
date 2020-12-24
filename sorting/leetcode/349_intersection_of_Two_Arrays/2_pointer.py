class Solution(object):

	def intersection_sorted(self, nums1, nums2):

		nums1.sort()
		nums2.sort()

		i = 0 
		j = 0
		
		n = len(nums1)
		m = len(nums2)

		print("nums1 : ", nums1)
		print("nums2 : ", nums2)

		res = []
		while i < n and j < m:

			if nums1[i] == nums2[j]:
				same = nums1[i]
				res.append(same)
				print("same : ", same)
				print("i : ", i)
				print("j : ", j)
				while i < n and nums1[i] == same:
					i += 1
					print("i increment : ", i)

				while j < m and nums2[j] == same:
					j += 1
					print("j increment : ", j)

			elif nums1[i] > nums2[j]:
				j += 1
			else:
				i += 1

		return res

nums1 = [1,1,2,2,3,6,9,78]
nums2 = [2,2,3,4,4,5,6,6,7]

arr  = Solution().intersection_sorted(nums1, nums2)
print("Result : " + str(arr))


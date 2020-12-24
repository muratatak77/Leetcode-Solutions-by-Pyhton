def merge(nums1, m, nums2, n):
	"""
	:type nums1: List[int]
	:type m: int
	:type nums2: List[int]
	:type n: int
	:rtype: void Do not return anything, modify nums1 in-place instead.
	"""
	print("nums1[:m] : " + str(nums1[:m]))
	print("nums2 : " + str(nums2))

	nums1 = sorted(nums1[:m] + nums2[:n])
	print("nums1 : " + str(nums1))


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6,7,8,9,12,4,6,6,7]      
n = 3
merge(nums1, m, nums2, n)



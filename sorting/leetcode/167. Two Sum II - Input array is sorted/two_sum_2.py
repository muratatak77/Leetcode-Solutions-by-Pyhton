class Solution(object):
	def twoSum(self, arr, target):
		i = 0
		j = len(arr)-1

		while i<j:
			total = arr[i] + arr[j]
			if total == target:
				return {i+1, j+1}
			elif total < target:
				i += 1
			else:
				j -= 1
		return []		

print(Solution().twoSum([2,3,4], 6))
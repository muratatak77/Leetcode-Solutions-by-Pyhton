from typing import List
class Solution:
	def checkSubarraySum(self, nums: List[int], k: int) -> bool:
		
		if len(nums) < 2:
			return False

		#edge cases k = 0 
		if k == 0:
			#we don;t need check all array. Just 1 and 2 item will be enough
			#should divisible first and second item.
			print("Special CASE ")
			for i in range(1,len(nums)):

				print("nums[i-1] == nums[i]" , nums[i-1] ,"==", nums[i])
				if nums[i-1] == nums[i] == 0:
					return True
			return False

				
		hmap = {}
		hmap[0] = True

		prefixsum = nums[0]
		oldsum = 0
		for i in range(1,len(nums)):

			oldsum = prefixsum
			print("	OLD sum :", oldsum)
			# [i...j] = [0...i][0...j-1]
			# 0<= j <=  i-2
			print("	OLD prefixsum :", prefixsum)
			print("	nums[i] :", nums[i])
			prefixsum = (prefixsum + nums[i]) % k
			print("	New prefixsum : ", prefixsum)
			#is there a prefix summing up to the same remainder?
			if prefixsum in hmap:
				print("		prefixsum in hmap : ", hmap)
				return True
			hmap[oldsum%k] = True
			print("		Hmap updated :", hmap)
			print("------------------------------")

		return false


nums = [23, 2, 4, 6, 7]
nums = [0,0]
k=0

res = Solution().checkSubarraySum(nums, k)
print("res : ", res)
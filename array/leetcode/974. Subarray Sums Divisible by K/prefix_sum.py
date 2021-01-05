from typing import List
class Solution:
	def subarraysDivByK(self, A: List[int], K: int) -> int:
		nums = A
		total = 0
		prefix_sum = 0
		hmap = {} # given a number in the mod K system, how many prefixes add up to it?
		hmap[0] = 1 #initialy, given 0 , at least 1 prefixsum even and more which 0.

		for i in range(len(nums)):
			print("Nums[i] : ", nums[i] )
			print("	old prefix_sum : ", prefix_sum)
			prefix_sum = (prefix_sum + nums[i])%K
			print("	new prefix_sum : ", prefix_sum)

			#Like : How many yellow prefixes add up to prefixsum?
			if prefix_sum in hmap:
				print("		prefix_sum in hmap :  prefix_sum: ", prefix_sum)
				total += hmap[prefix_sum]
				print("		Total : ", total)

			#hash map update
			#I am a subordinate. My boss gets the updated version. Containing information about all the prefixes including the prefix ending at me.
			#The last prefix has not been added. We will add.
			#hmap new = hmap old will be augmented with prefix sum new info.
			if prefix_sum in hmap:
				hmap[prefix_sum] += 1
			else:
				hmap[prefix_sum] = 1



			print("			HMAP : ", hmap)
			print("----------------------------------------")

		return total


A = [4,5,0,-2,-3,1]
K = 5
res = Solution().subarraysDivByK(A, K)
print("res : ", res)

			 
		
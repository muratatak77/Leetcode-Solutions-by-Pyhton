'''

 [ 1, -1, 5, -2,  3]
 [yellow prefix][red prefix]
 0           j-1 j         i




We have to try, constant time. Prefix sum.

Our problem in the red suffix, max length adding up to K. Because the sum here can be written has P-K again. P is something that is fixed. We are interested in yellow prefixes that add up to P-K. 

Since the Yellow prefix is complementary to red suffixes we want to maximum if we want a red suffix which adds up to  'K' and has the highest maximum possible length we are looking for a yellow prefix that's up to 'P - K' a has the smallest possible length.

Yellow prefix = Min length adding up to P-K. What is the min length prefix that adds up to that value? The note is the difference between earlier problems. Earlier problems need a count. Here we don't need counts. Here we need the smallest size such as a prefix which adds up to the given value. 

Given a value, we want to smallest size yellow prefix adding up to it that's what we need to store a hash table.

Given a value, what is the smallest prefix adding up to that value?
'''

from typing import List
class Solution:
	def maxSubArrayLen(self, nums: List[int], k: int) -> int:
		#Given any value , what is the smallest prefix adding up to that value.
		hmap={}

		#When we look at the empty prefix when we look at the empty prefix clearly some is 0.
		#Length of the empty subarray = 0
		#Value is not a count this value smallest prefix lenght,
		#empty prefix has a length of 0
		#This value not going to change in our hmap[0]= 0. 
		#Because we are looking at prefixes increasing order of size length any time we write a value into the this kind of hash table is gonna stay here.
		hmap[0] = 0
		prefixsum = 0
		globalmax = 0 
		for i in range(len(nums)):
			prefixsum += nums[i]
			print("prefixsum : ", prefixsum)
			#we have to lookup find the local answer
			#We find out find the smallest lenght yellow prefix adding up to longest red suffix thats add up to K
			#Find the smallest lenght yellow prefix adding up to prefixsum(new) - K
			
			if prefixsum-k in hmap:
				print("		prefixsum-k in hmap : prefixsum-k : ", prefixsum-k)
				globalmax = max(globalmax, (i+1)-hmap[prefixsum-k]) 
				print("		globalmax : ", globalmax)
			#means we have seen before yellow prefix that add up to this value 
			# and we will get the smallest such value from there.
			# Doesnt exists in hmap there is no such yellow prefix which means we dont have a red suffix thats adds up to key.
			# hmap[prefixsum-k] = lenght of shortest such prefix
			# We know the lenght of hash map tells up the yellow prefix path. (0... j-1) look at the image2
			# Total lenght i+1 we have to substract yellow prefix value. Smallest such value. Which tells who is largest red suffix adds up to key.
			# length of the red part is going to be total len : i+2 - map[prefixsum-k]
			# we have a global max 
				



			#hash map update with info about [0....i]
			#We have to tell us boses augmented information
			#information about prefix that adds up our number
			#we will storing what is the smallest prefix adding up to that value
			#we know that value that is the prefixsum.
			#prefixsum already exists in the hash map, means already shortest prefix
			#that added up to same prefix sum.
			
			#in case our hash map should not change, because suppose the record 
			#the smallest prefix adding up to value. Only hash map update prefixsum 
			#not seen before. If not seen this before , 
			#means our prefix is the sortest such prefix adding up to that value.

			if prefixsum not in hmap:
				hmap[prefixsum] = i+1
				print("Update hmap : ", hmap)
			print("========================================")



		return globalmax

nums = [1, -1, 5, -2, 3]
k = 3

nums = [-2, -1, 2, 1]
k= 1
res = Solution().maxSubArrayLen(nums, k)
print("res : ", res)



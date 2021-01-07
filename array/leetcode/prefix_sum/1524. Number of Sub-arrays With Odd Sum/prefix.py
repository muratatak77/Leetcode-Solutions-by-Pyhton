'''
	
	we can look first main_process.png 

	and 

	prefixsum is even we have to ask this question:
		
		Psi is even = How many yellow prefixes with an odd sum?
					  How many red suffixes will get odd?
					  every red suffix complemantary suffix. 


		Psi is odd = How many yellow prefixes with an even sum?
  		
  		we are only odd numbers. 
		because even + odd = odd
				odd + odd = even
	
	complemantary should be odd.


	Total is odd : We want to find out how many red suffixes are there  which are odd?
	Equalevant yellow prifes that are even. Because even + odd = will be odd.


'''

from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

    	prefixsum = 0

    	hmap = {}
    	hmap["odd"] = 0
    	hmap["even"] = 1

    	total = 0
    	nums = arr
    	for i in range(len(nums)):
    		prefixsum += nums[i]
    		print("prefixsum : ", prefixsum)
    		print("hmap[odd] : ", hmap["odd"])
    		print("hmap[even] : ", hmap["even"])

    		if prefixsum % 2 == 0:
    			total += hmap["odd"]
    			print("	 Prefixsum is even update Total : ", total)
    		else:
    			total += hmap["even"]
    			print("  Prefixsum is odd. update Total : ", total)
    		
    		total = total % 1000000007
    		print("    TOTAL :", total)

    		if prefixsum % 2 == 0:
    			hmap["even"] += 1
    			print("		prefixsum even update. hmap[even] : ", hmap)
    		else:
    			hmap["odd"] += 1
    			print("		prefixsum odd update. hmap[odd] : ", hmap)

    		print("========================================")

    	return total


arr = [1,3,5]

res = Solution().numOfSubarrays(arr)
print("res : ", res)




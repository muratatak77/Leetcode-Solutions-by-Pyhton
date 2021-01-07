'''

	
	nums  = [0,1,0]

	in the process , we can seperate 
	0,1 > prefix > should be smallest length of prefix having it
	
	Given, A certain amount of imbalance, what is the length of the smallest  prefix that has it?
	A number of the prefixes with the same excess/deficiency of 1s.

	0 > suffix > longest suffix

	We will track [#1s - #s0] 

	we can keep to extract from our sum variable if we crooss 0
	else
	we can increment our sum variable. 
	our goal is to find out equivalent values beetween the previous sums. 
	So, we need hash map. we given a value , what is the smallest item for ec


'''


from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
    	print("nums : ", nums)
    	hmap = {} #given an excess , smallest lenght of prefix having it
    	hmap[0] = 0
    	prefixexcess = 0
    	globalmax = 0

    	for i in range(len(nums)):
    		if nums[i] == 0:
    			prefixexcess -= 1
    		else:
    			prefixexcess += 1

    		print("prefixexcess : ", prefixexcess)
    		if prefixexcess in hmap:
    			print("	  prefixexcess in hmap :" , hmap)
    			globalmax = max(globalmax, i+1 - hmap[prefixexcess])
    			print("		globalmax : ", globalmax)
    			# hmap[prefixexcess] = shortest prefix
    			# i+1 - hmap[prefixexcess] = longest suffix
    		
    		#update hash map
    		if prefixexcess not in hmap:
    			print("			prefixexcess not in hmap. We will update.")
    			hmap[prefixexcess] = i+1
    			print("			After update hmap ; ", hmap)
    		print("-------------------------------")

    	return globalmax


nums = [0,1,0]
res = Solution().findMaxLength(nums)
print("res : ", res)
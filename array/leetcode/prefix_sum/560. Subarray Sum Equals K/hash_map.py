'''
	nums = [1,1,1]
	hmap[0] = 1

	pre_sum = 1
	hmap[1] = 1

	pre_sum = 2
	pre_sum - k in hmap
		count = 1
	hmap[2] = 1


	pre_sum = 3
	pre_sum - k in hmap
		count = 2

	hmap[3] = 1

--------------------------------

	nums = [1,2,3] , k = 3

	hmap[0] = 1
	presum = 1
	presum - k in hmap
		count = 0
	hmap[1] = 1

	presum = 3
	presum - k in hmap
		count = hmap[presum-k]
		count = 1
	hmap[3] = 1
	
	presum = 6
	presum - k in hmap
		count = hmap[presum-k]
		count = 2
	hmap[6] = 1



-----------------

	we nnderstant this method is prefix sum approach.

	nums = 1,2,3 , k =3 

	1 + 2 + 3 

	we can consider the last sum depends on the hmap value.

	 hmap 
	K   V
	0 : 1
	1 : 1
	3 : 1
	6 : 1 

	1+2 = 3 
	and we can increment count by the hmap value 

	3+3 = 6
	6-k = 3 
	meaning is there any prefix already?
	again we can increment count by the hamp value


 ----------
 	nums = [1,2,0,3] , k = 5

 	2+0+3 = 5 
 	1+2+0 =  3  + 3 = 6

 	6-k = 1

 	meanswe have 1 , remain should be 5

	hmap 
	0 > 1
	1 > 1
	3 > 2

	result will be 1

	---------

	nums = [5,5,5,1] , k = 1

	As Lazy Manager I am asking how does the last element contribute to the answer?
	How does this element change it?
	What is the total number of sub-arrays ending at index n-1 which add up to k?
	That’s my part of the answer. That’s my contribution or my numbers contribute to the answer.


'''

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


    	hmap = {}
    	hmap[0] = 1 # initaly there is  no prefix

    	count = 0
    	pre_sum = 0

    	print("hmap : ", hmap)
    	print("count : ", count)
    	print("----------------------------")

    	for i in range(len(nums)):
    		
    		pre_sum += nums[i]
    		print("	pre_sum : ", pre_sum)
    		#how many prefix sum to prefix-k ?
    		#k'ye kadar olan her kırmızı sonek için, p-k'ye kadar eklenen sarı bir önek vardır.
    		#look image main_idea.png
    		if pre_sum - k in hmap:
    			print("		pre_sum - k in hmap :  pre_sum - k : ", pre_sum - k)
    			count += hmap[pre_sum-k]
    			print("		count : ", count)


    		#update hmap
    		if pre_sum in hmap:
    			print("		>pre_sum in hmap : pre sum : ", pre_sum)
    			hmap[pre_sum] += 1
    			print("		hmap update : ", hmap)
    		else:
    			print("		pre_sum in not hmap : pre sum : ", pre_sum)
    			hmap[pre_sum] = 1
    			print("		hmap update : ", hmap)


    		print("------------------")

    	return count


nums = [1,1,1]
nums = [1,2,3]
nums = [3,4,7,2,-3,1,4,2]
k = 7
res  = Solution().subarraySum(nums, k)
print("res : ", res)
        
'''
 T(N) = O(N) we have just one iterate
 O(N) = O(N) using hmap 
'''
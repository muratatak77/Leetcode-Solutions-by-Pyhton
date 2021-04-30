=begin
	

	[4,3,2,7,8,2,3,1]
	
	First 
	we try to get ideal list from nums array = [1,2,3,4,3,2,7,8] or [2,3,1,2,3,4,7,8]

	we can apply a sorting alg. But if we can apply directy sorting T(N) will be O(NlogN).
	ideal list increment 1 so we can match nums item and i+1. why i+1 because of index of nums.

		for i in range(0,n)
			while nums[i] != i+1

				if doesn't match we can try to swap and change item place by the index
				we can determine a destination item and if this item is not equal current nums item we can swap

				like first item is  4 , but should be 1. we can swap by the nums[4]
				
				after swap we can get : [7, 3, 2, 4, 8, 2, 3, 1]

				but we can get 7 still we need to try swaping
				
				after swap nums[7] and nums[0] : [3, 3, 2, 4, 8, 2, 7, 1]

				contuine swaping : [2, 3, 3, 4, 8, 2, 7, 1]

				finally our list will be :[1, 2, 3, 4, 3, 2, 7, 8] 
				

	In second part we can walk trough the list. 
		we can check just nums[i] != i+1.
		tracing just current item and useful solution right number.
		is not match we can add an result array.



----------- Update 
	
	iterate 0 to n
		while current nums till not matching target item (i+1)
			curent item = nums[i]-1
			if current item is not same target item
				swap(current item, target item )
			else
				break

=end


class SolutionCycleSort
	def findDuplicates(nums)
		for i in 0..nums.size-1
			while nums[i] != i+1
				target_index = nums[i]-1
				if nums[target_index] != nums[i]
					nums[target_index],nums[i] = nums[i], nums[target_index]
				else
					break
				end
			end
		end

		res = []
		for i in 0..nums.size - 1
			if nums[i] != i+1
				res << nums[i]
			end
		end

		return res
	end
end


# # from typing import List
# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#     	n = len(nums)
#     	for i in range(0,n):
#     		print(" i :", i)
#     		while nums[i] != i+1:
#     			d = nums[i]-1
#     			#sanity check
#     			#	duplication check
#     			if nums[d] != nums[i]:
#     				nums[i], nums[d] = nums[d], nums[i]
#     				print("			nums :", nums)
#     			else:
#     				break

#     	result = []
#     	for i in range(0,n):
#     		if nums[i] != i+1:
#     			result.append(nums[i])

#     	return result


nums = [4,3,2,7,8,2,3,1]
s = SolutionCycleSort.new()
res = s.findDuplicates(nums)
puts "res : #{res}"


=begin
	
	T(N) = O(N) 

		 i : 0
				swap : [7, 3, 2, 4, 8, 2, 3, 1]
				swap : [3, 3, 2, 4, 8, 2, 7, 1]
				swap : [2, 3, 3, 4, 8, 2, 7, 1]
				swap : [3, 2, 3, 4, 8, 2, 7, 1]
		 i : 1
		 i : 2
		 i : 3
		 i : 4
				swap : [3, 2, 3, 4, 1, 2, 7, 8]
				swap : [1, 2, 3, 4, 3, 2, 7, 8]
		 i : 5
		 i : 6
		 i : 7

		 as seen as program logs, 1 loop just works one pass all items. While loop just works max 4 times in this case.

	S(N) = 0(1) because we use result array for just append and result an answer.
			No extra space , just for the output list.

=end

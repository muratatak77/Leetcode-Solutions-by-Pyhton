=begin
	we can apply two pointer approach for this question.
	sorted arr
	we can start index 1 , and we can check current index item and prev index in nums
	if they are not equal we can contunie increment non dupl pointer
		and we can match like this 
			nums[non_dupl] = nums[i]
			we need to update current array 

		if they are equal we just iterate i pointer. 
		

		[2, 3, 3, 3, 6, 9, 9]
	
=end

def remove_duplicates(nums)
	if nums.nil? or nums.length == 0
		return 0
	end	

	non_dupl = 1
	i = 1

	while i < nums.length
		if nums[non_dupl - 1] != nums[i]
			nums[non_dupl] = nums[i]
			non_dupl += 1
		end
		i += 1
	end

	return non_dupl
end


# nums = [2, 3, 3, 3, 6, 9, 9]
nums = [1,1,2]
nums = []
res = remove_duplicates(nums)
puts "res : #{res}"


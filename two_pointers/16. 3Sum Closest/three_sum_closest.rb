# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
#
#  we have an array and we need to add a triplets items.
# we can pick first i item and we can do an substrack operation selecting by 2 pointers.
# Thats why we can apply 3 pointer approach.
# 
# 
#
def three_sum_closest(nums, target)
	
	n = nums.length

	return [] if n == 0

	smallest_diff = (2**(0.size * 8 - 2))
	puts "smallest_diff : #{smallest_diff}"

	nums = nums.sort

	puts "nums sorted : #{nums}"

	for i in (0..n-1)

		left = i+1
		right = n-1
		puts " >>> i : #{i}"
		puts " 	>>>start left : #{left} - right : #{right}"

		while left < right

			puts "left : #{left} - right : #{right}"

			target_diff = target - nums[i] - nums[left] - nums[right]
			puts "	target_diff : #{target_diff}"
			#eaxct match
			if target_diff == 0
				 return target - target_diff
			end

			puts "target_diff.abs() < smallest_diff.abs()  : #{target_diff.abs()} <  #{smallest_diff.abs()}"
			puts "target_diff.abs() == smallest_diff.abs()  : #{target_diff.abs()} ==  #{smallest_diff.abs()}"
			puts "target_diff > smallest_diff  : #{target_diff} >  #{smallest_diff}"
			#negative or positive any case
			check_1 = target_diff.abs() < smallest_diff.abs()
			#be sure negative case works correctly
			check_2 = target_diff.abs() == smallest_diff.abs() and target_diff > smallest_diff

			if check_1 or check_2
				smallest_diff = target_diff
				puts "		after set smallest_diff :: #{smallest_diff}"
			end

			#we need to go to the left if our diff grater than 0. because we can contunie to scan other items.
			if target_diff > 0
				left += 1
			else
				right -= 1
			end
			puts "			after put left : #{left} - right : #{right}"


			puts "=========================="

		end

	end

	return target - smallest_diff

end


# nums = [-3, -1, 1, 2]
nums = [-2, 0, 1, 2]
nums = [1, 0, 1, 1]
# target=1
# target=2

target=100
res = three_sum_closest(nums, target)
puts "res : #{res}"

=begin
	
		T(N) = Sorting will be 	O(N Log N).  For loop and inside while takes O(N^2)
			Overall the function will take O(N Log N + N^2), which is asymptotically equivalent to O(N^2)

		S(N) = O(N) , which is required for sorting.

=end

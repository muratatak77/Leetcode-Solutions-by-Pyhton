=begin
		
		nums = [-2, -1, 0, 2, 3]


=end
# @param {Integer[]} nums
# @return {Integer[]}
def sorted_squares(nums)
	n = nums.length 
	return [] if n == 0	

  quares = Array.new(n,0)
  puts "quares : #{quares}"

  highest_seq_id = n-1
  left , right = 0, n-1 

  while left <= right  	
  	left_val = nums[left] * nums[left]
  	right_val = nums[right] * nums[right]
  	if left_val > right_val
  		quares[highest_seq_id] = left_val
  		left += 1
  	else
			quares[highest_seq_id] = right_val
  		right -= 1
  	end
  	highest_seq_id -= 1
  end
  quares
end



nums = [-2, -1, 0, 2, 3]
res = sorted_squares(nums)
puts "res : #{res}"
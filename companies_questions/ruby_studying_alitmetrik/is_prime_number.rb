def is_prime(num)

	if num < 1
		return false
	end
	n = 2
	while n < num
		if num % n == 0		
			return false 
		end
		n += 1
	end
	return true

	# (2..(num-1)).each do |n|
	# 	if num % n == 0
	# 		return false
	# 	end
	# end
	# return true

end





res = is_prime(4)
print("res : ", res )
puts ""
	
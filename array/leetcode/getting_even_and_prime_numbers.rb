


def get_request_numbers(numbers)
		
	return [] if numbers.nil?

	evens = []
	primes = []

	for i in 0..numbers.length-1
		
		if numbers[i] % 2 == 0
			evens << numbers[i]
		end


		count = 2
		is_prime = true
		while count < numbers[i] # 2 < 5
			if numbers[i] % count == 0 # 5 % 2 == 3
				is_prime = false
				break
			end
			count += 1
		end
		primes << numbers[i] if is_prime

	end


	return evens, primes
end



#one contain even numbers
#one contain prime numbers


numbers = [3,5,7,4,8,11,9,13,15]
# numbers = []

res = get_request_numbers(numbers)
puts "res : #{res}"
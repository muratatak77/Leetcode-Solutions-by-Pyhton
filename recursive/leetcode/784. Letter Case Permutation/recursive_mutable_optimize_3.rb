
def overall(s)
	@result = []
	def helper(s,i)
		#leaf workers
		puts "i : #{i}"
		if i == s.size
			unless @result.include?(s.join(""))
				@result.append(s.join(""))
			end
			return
		else
			#internal node workers
			puts " 		s[i].to_i.to_s : #{ s[i].to_i.to_s}"
			puts "		s[i] : #{s[i]}"
			if s[i].is_a? Numeric
				helper(s,i+1)
			else
				s[i] = s[i].downcase
				puts "		Call s 0 : #{s}"
				helper(s, i+1)

				s[i] = s[i].upcase			
				puts "		Call s 1 : #{s}"
				helper(s, i+1)
			end
		end
	end

	helper(s.split(""),0)
	return @result
end

s = "a1b2"
res = overall(s)
puts ("res: #{res}")

#aux space is better for mutable version. Because we don't create new fresh string in every node.
#space = 
#	input O(n)
#	output = O(2^n x n)
#  			n = length of string
#  			2^n = number of all case variations

#	aux = O(n) much better rather than the immutable version

#Time : O(2^n x n)
# leaf workers : O(2^n x n)
# internal node workers : O(2^n)
# 
# 
# space comp. immutable : O(n^2)
# space comp. mutable : O(n)
# just aux space much better

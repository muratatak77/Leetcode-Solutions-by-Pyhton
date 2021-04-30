=begin
	
	combitonarial enumeration problem(permutation /combination)
	This problem is filling blank problem
	
	we can apply 
	time complexity will be exponential time compl.
	
	We process left to right and as a lazy manager, only take responsibility for filling in the first blank. 
	lazy manager - delegates the rest of the work to subordinates.
	
	 like  :

							_ _ _ _  > lazy manager 
						
						a _ _ _    A _ _ _     > sub ordinates - internal nodes (recursive case)
					
					a1 _ _				A1 _ _
				
				a1b _	 					A1b _
									
			a1b2	a1B2				A1b2		A1B2 		> leaf workers (base cases)




	 we need a global result
	 and helper method includes recursive and base cases 

=end

class Solution

	def self.letterCasePermutation(s)
		
		@result = []

		def self.helper(s,i,slate)
			puts "slate : #{slate}"

			if i == s.length
				@result << slate
				return
			else
				if s[i].to_i != 0
					helper(s,i+1,slate+s[i])
				else
					helper(s,i+1,slate+s[i].downcase)
					helper(s,i+1,slate+s[i].upcase)
				end
			end
		end

		helper(s,0,"")
		@result

	end

end


s = "a1b2"
res = Solution.letterCasePermutation(s)
print("res : ", res)



=begin
space complexity : 
	input : n
	aux space :  immutable version  O(n^2) - implicit stack space - immutable version. 
	output : O(2^n.N)  2^n = every alpha char has multiple options. 2^n  = 2^2 = 4 / N : length of string
time :  O(2^n.N)

=end

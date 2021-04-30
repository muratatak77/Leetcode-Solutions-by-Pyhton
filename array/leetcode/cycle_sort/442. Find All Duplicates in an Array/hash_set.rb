
require 'set'

class SolutionSet
	def findDuplicates(nums)
		set = Set.new
		res = []
		for num in nums
			if set.include?(num)
				res << num
			else
				set << num
			end
		end
		res
	end
end


nums = [4,3,2,7,8,2,3,1]
res = SolutionSet.new().findDuplicates(nums)
puts "res : #{res}"
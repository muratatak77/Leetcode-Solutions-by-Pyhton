# we can apply stack approcihg. 
# we can add an stack if we don't accross # mark. 
# and when we accross the # mark we can pop. Finally we will get the without # string.
# 
# @param {String} s
# @param {String} t
# @return {Boolean}
def backspace_compare(s, t)
	def build(str)
		return "" if str.nil?
		ans = []
		str.each_char { |chr|  
			if chr != "#"
				ans.append(chr)
			elsif ans
				ans.pop()
			end
		}
		return ans.join("")
	end
	
	return build(s) == build(t)
end

s = "ab#c"
t = "ad#c"

res = backspace_compare(s, t)
puts " Res : #{res}"


=begin
	T(N) = O(N+M)	 N  and M are the length of s and t respectively
	S(N) = O(N+M) 
=end
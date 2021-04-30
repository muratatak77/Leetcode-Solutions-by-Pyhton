=begin

Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).
------------------------------------------------


Solution : 

	We can apply sliding wondow fix lenght approach fot this question.
	s = "abciiidef" 
	k = 3
	
	we can store a set all vowel chars. 

	set = ('a','i','e','u','o')
	in initial we can walk trough in loop to K.

	second part :
	we can walk trough again in loop start K  to len(s)

		if s[i] include in a vowelset we can increment our local counter  label.
		for next item in sliding window if s[i-k] in vowelset, we can decrement our local label.


	T(N) = O(N)
	S(N) = O(1)

=end


require 'set'

def maxVowels(s,k)
	return 0 if s.nil?
	
	vowelset = Set.new(['a','i','u','o','e'])
	vowelnum = 0
	globalmax = 0

	#initial items
	for i in (0..k-1)
		puts "S[i] : #{s[i]}"
		if vowelset.include?(s[i])
			vowelnum += 1
		end
	end
	
	#remain items 
	for i in (k..s.length)
		vowelnum += 1 if vowelset.include?(s[i])
		vowelnum -= 1 if vowelset.include? s[i-k]
		globalmax = [globalmax,vowelnum].max
	end
	globalmax
end

		
s = "abciiidef"
# s = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"

k = 3
# k = 33


res = maxVowels(s, k)
puts "res : #{res}"

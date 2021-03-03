'''
Question : 

	In an alien language, surprisingly they also use english lowercase letters, 
	but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
	Given a sequence of words written in the alien language, and the order of the alphabet, 
	return true if and only if the given words are sorted lexicographicaly in this alien language.

	 

	Example 1:

	Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
	Output: true
	Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
	Example 2:

	Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
	Output: false
	Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
	Example 3:

	Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
	Output: false
	Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
	According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Answer:
	
	Solution: 

		we can use a hash map keeping orders chars. 
		like : 
			order = "hlabcdefgijkmnopqrstuvwxyz"
			hash_map = {h:0, l:1, a: 2, b:3 ... } so on

			and we can do one iterate to check current item  and next item in the loop.

				if word1[index] != word2[index]:
					we can check hash map order. If word1[index] in hashmap grater than word2[index] we can return False

			after iterate if we inputs like apple , app than , we need to check length of words.
			

'''
from typing import List
class Solution:
	def isAlienSorted(self, words: List[str], order: str) -> bool:

		# ordering_map = {c: i for i, c in enumerate(order)}
		ordering_map = {}
		#construct a hash map to keep order map 
		i = 0
		for char in order:
			if char not in ordering_map:
				ordering_map[char]=i
			i+=1

		print("ordering_map  ", ordering_map)

		#normally in python len(words) works but we will check words[i+1] index
		for i in range(len(words)-1):
			word1 = words[i]
			word2 = words[i+1]

			#we should get min(len(word1,word2)) because sometimes our iput would be :  'apple', 'app'. we need get just min len of words.
			#we can not go after len('app')
			for j in range(min(len(word1), len(word2))):
				if word1[j] != word2[j]:
					if ordering_map[word1[j]] > ordering_map[word2[j]]:
						return False
					break # we need to go other words
			else:
				print("We are here j : ", j)
				#if our input have 'apple' and 'app' we need to check finally length of size words.
				#if we have any char , any char eventually will be grater than nothing.
				if len(word1)>len(word2):
					return False

		return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"

# words = ["leetcode","leetcode"]
# order = "worldabcefghijkmnpqstuvxyz"


words = ["kuvp","q"]
order ="ngxlkthsjuoqcpavbfdermiywz"

# words = ["apple","app"]
# order = "abcdefghijklmnopqrstuvwxyz"

res = Solution().isAlienSorted(words, order)
print("res : ", res)


'''
	T(N) = O(C) C is all content of words.
	S(N) = O(1) 
'''


			


		

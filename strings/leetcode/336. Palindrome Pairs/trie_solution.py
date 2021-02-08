
import collections

class TrieNode:
	def __init__(self):
		self.next = collections.defaultdict(TrieNode)
		self.ending_word = -1
		self.palindrome_suffixes = []

class Solution:
	def palindromePairs(words):

		# Create the Trie and add the reverses of all the words.
		trie = TrieNode()
		for i, word in enumerate(words):
			print("start word: ", word, " i : ", i)
			word = word[::-1] # We want to insert the reverse.
			print("reversed word: ", word, " i : ", i)
			
			current_level = trie

			for j, c in enumerate(word):
				print("enumerate j  :" , j,  " - c : ", c)
				# Check if remainder of word is a palindrome.
				print("word[j:] == word[j:][::-1] >> " , word[j:], " == ",  word[j:][::-1])
				if word[j:] == word[j:][::-1]:# Is the word the same as its reverse?
					current_level.palindrome_suffixes.append(i)
					# print("append palindrome_suffixes : ", current_level.palindrome_suffixes)
					print(" ------ current_level palindrome_suffixes : ", current_level.palindrome_suffixes, " -current_level : ", current_level.__dict__)
					print(" 1 ------ current_level : ", current_level)
				# Move down the trie.
				current_level = current_level.next[c]
				# print("c : ", c , "current_level : ", current_level.__dict__)
				print(" 2 ------ current_level : ", current_level)
			
			current_level.ending_word = i
			print("3 current_level : ", current_level.__dict__)
			print("3 ------ current_level : ", current_level)
			# print("current_level.ending_word : ", current_level.ending_word)
			# print("current_level.palindromePairs : ", current_level.palindrome_suffixes)			
			

			print("------------   end j  ------------")
		print("---------------------   end i  ----------------------")

		# Look up each word in the Trie and find palindrome pairs.
		solutions = []
		for i, word in enumerate(words):
			print("1 start word : ", word , " - i : ", i)
			current_level = trie
			for j, c in enumerate(word):
				print("2 start word : ", word , " - j : " ,  j, " - c :", c)

				# Check for case 3.
				# Case 3 is the one where the first word is longer than the second word.  
				# We have a palindrome left on the word and are on a word end node (case 3). 
				# In terms of our Trie, it would come up where we get to a ending word node and still have some letters left from our current word. 
				# If those letters that are left form a palindrome, then we have a case 3 palindrome pair.
				if current_level.ending_word != -1:
					print("0 current_level : ", current_level)
					print("current_level.ending_word : ", current_level.ending_word)
					print("we have in case 3")
					print("word[j:] == word[j:][::-1] >> " , word[j:], " == ",  word[j:][::-1])
					if word[j:] == word[j:][::-1]: # Is the word the same as its reverse?
						solutions.append([i, current_level.ending_word])
						print("solutions append i : ", i , " - current_level.ending_word : ", current_level.ending_word )
				if c not in current_level.next:
					print("BREAK")
					break
				# print(" ------ current_level ending_word : ", current_level.ending_word, " - next items : ", current_level.next.items())
				current_level = current_level.next[c]
				print("1 current_level : ", current_level)
			else: # Case 1 and 2 only come up if whole word was iterated.

				# Check for case 1.
				# We have no letters left on the word and are at a word end node 
				print("solutions i : ", i , " - current_level.ending_word : ", current_level.ending_word )
				if current_level.ending_word != -1 and current_level.ending_word != i:
					print("we have in case 1")
					print("solutions append i : ", i , " - current_level.ending_word : ", current_level.ending_word )
					solutions.append([i, current_level.ending_word])
					print("Solution : ", solutions)

				# Check for case 2.
				# We have no letters left on the word and there are indexes in the list attached to the node (case 2).
				print(" current_level.palindrome_suffixes : ", current_level.palindrome_suffixes )
				for j in current_level.palindrome_suffixes:
					print("we have in case 2")
					print("solutions append i : ", i , " -  j : ", j )
					solutions.append([i, j])
			print("------------   end j  ------------")
		print("---------------------   end i  ----------------------")
		return solutions


# words = ["bat","tab","cat"]
# words = ["abcd","dcba","lls","s","sssll"]
# words = [ "A", "B", "BAN", "BANANA", "BAT", "LOLCAT", "MANA", "NAB", "NANA", "NOON", "ON", "TA", "TAC"]
# words = [ "A", "B", "BAN", "BANANA", "NAB"]
words = ["B", "BANA"]
res = Solution.palindromePairs(words)
print(res)
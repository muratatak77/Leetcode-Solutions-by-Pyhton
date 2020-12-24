class TrieNode():
	def __init__(self):
		self.children = dict()
		self.words = list()
		self.n = 0

class Trie():
	def __init__(self):
		self.root = TrieNode()
		self.node = self.root

	def add_word(self, word):
		node = self.root
		for c in word:
			if c not in node.children:
				node.children[c] = TrieNode()
			node = node.children[c]
			if node.n < 3:
				node.words.append(word)
				node.n += 1

	def find_word_by_prefix(self, c):
		if self.node and c in self.node.children:
			self.node = self.node.children[c]
			return self.node.words
		else:
			self.node = None
			return []

class Solution:
	def suggestedProducts(A, searchWord):
		A.sort()
		trie = Trie()
		for word in A:
			trie.add_word(word)
		res = []
		for c in searchWord:
			res.append(trie.find_word_by_prefix(c))
		return res


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

res = Solution.suggestedProducts(products, searchWord)
print(res)
class TrieNode():
	def __init__(self):
		self.children = dict()
		self.isWord = False
		self.n = 0

class Trie():

	def __init__(self):
		self.root = TrieNode()
		self.node = self.root
		self.result = []
		self.result_words = []


	def _print(self, node):
		if not node:
			return

		if node.children:
			for child in node.children.values():
				self._print(child)

	def buildTrie(self, words):
		root = self.root
		for word in words:
			self.insertTie(root, word)

		return self.list_words(root)

	def list_words(self,trie):

		if trie.children:

			for k,v in trie.children.items():
				
				print("k: " , k, " - value : ", v)
				self.result.append(k)

				if v.isWord:
					print("self.result : " , self.result)
					print(' '.join(self.result))

					self.result_words.append(' '.join(self.result))
					self.result = []

				
				self.list_words(v)
		
				

				# for el in self.list_words(v):
					# print("el: " , el)
					# my_list.append(k+el)
				# else:
					# my_list.append('')
			
		return self.result_words
		

	def insertTie(self, node, word):

		print("word :" , word)

		for c in word:
			print("node char : ", node.isWord, "- c : ", c)
			if node.isWord:
				return
			if c not in node.children:
				node.children[c] = TrieNode()
			node = node.children[c]
			# print(c)
			# if node.children:
				# print(*node.children.items(), sep='\n')

		node.isWord = True
		print("node.isWord : ", node.isWord, "- word : ", word)

		# node.children = None
		if word =="pi":
			print("1 PI geldi.")
			print(node.children)




# words = ["pizza", "pie", "hut", "hulu", "pi", "hutch" ]
words = ["hut", "hulu", "hutch" ]
# words = ["pizza", "pie", "pi"]

t = Trie()
res = t.buildTrie(words)
print(res)


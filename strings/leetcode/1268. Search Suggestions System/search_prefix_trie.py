class TrieNode():
	"""docstring for TrieNode"""
	def __init__(self):
		self.children = {}
		self.endOfWord = False


class Trie(object):

	def __init__(self):
		self.root = TrieNode()

	def _print(self, node):
		if not node:
			return
		print(node.children)
		for child in node.children.values():
			self._print(child)

	def insert(self, word):
		current = self.root
		n = len(word)
		for ch in word:
			if ch in current.children:
				node = current.children[ch]
			else:
				node = TrieNode()
				current.children[ch] = node
			current = node

		current.endOfWord  = True
		# self._print(self.root)

	def search(self, word):
		current = self.root
		for ch in word:
			if ch in current.children:
				current = current.children[ch]
			else:
				return False

		return current is not None and current.endOfWord

	def delete():
		pass


keys = ["the","a","there","anaswe","any", "by","their"] 
# keys = ["the","a","there"]

output = ["Not present in trie", "Present in trie"]
 
# Trie object 
t = Trie()
# Construct trie 
for key in keys: 
	t.insert(key)

print("{} ---- {}".format("the",output[t.search("the")])) 
print("{} ---- {}".format("these",output[t.search("these")])) 
print("{} ---- {}".format("their",output[t.search("their")])) 
print("{} ---- {}".format("thaw",output[t.search("thaw")])) 


		
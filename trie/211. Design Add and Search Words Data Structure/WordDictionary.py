'''
	If we will make an Word Dictionary we can use Trie Data Structure
	First we can add to a Trie Data Structure 

	like : 
	
	{o:{a:{t:{h:{'$': True}}}}}, 

	{d:{b:{c:{'$': True}}}}

	And trie works with the recursive

	
'''

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
       	self.trie = {}

    def addWord(self, word: str) -> None:
    	node = self.trie

    	for ch in word:
    		if not ch in node:
    			node[ch] = {}
    		node = node[ch]
    	node['$'] = True
        

    def search(self, word: str) -> bool:
    	def helper(word, node):

    		print("		word : ", word)

    		for i,ch in enumerate(word):
    			if not ch in node:
    				if ch == ".":
    					for x in node:
    						print("x : ", x)
    						if x != '$' and helper(word[i+1:],node[x]):
    							return True
    				return False
    			else:
    				node = node[ch]
    				print("		valid node : ", node)

    		return '$' in node

    	return helper(word, self.trie)
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("oath")
obj.addWord("dig")
obj.addWord("dog")
obj.addWord("dogs")
obj.addWord("dig")
# param_2 = obj.search("oath")
# param_3 = obj.search(".og")
param_4 = obj.search("..t")

# print("param_2  :", param_2)
# print("param_3  :", param_3)
print("param_4  :", param_4)


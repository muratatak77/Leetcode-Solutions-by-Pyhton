class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word):
        node = self.trie
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
        """
        def search_in_node(word, node):
            for i, ch in enumerate(word):
                print("iterator ch : ", ch)
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node
            
        return search_in_node(word, self.trie)


word = ""
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
s1 = wordDictionary.search("pad")
s2 = wordDictionary.search("bad") 
s3 = wordDictionary.search(".ad")
s4 = wordDictionary.search("b..")

print("s1 : ", s1)
print("s2 : ", s2)
print("s3 : ", s3)
print("s4 : ", s4)


'''
M is a length of the word to find, and N is the number of words

Time complexity: O(M) for the "well-defined" words without dots , and O(M⋅N) for the "undefined" words.
Space complexity: O(1) for the search of "well-defined" words without dots, and up to O(M) for the "undefined" words.
'''


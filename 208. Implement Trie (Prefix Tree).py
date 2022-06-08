class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        n = len(word)
        node = self.root
        i = 0
        
        # go over each char in word
        while i < n:
            
            # if charNode != None:
                # this char exists in a branch already
                # directly go down a level to check the next char
            # else: # charNode == None
            
            # this char and remaining chars don't exist in a branch already
            if node.children[self.charToIndex(word[i])] == None:
                # insert a new trie node to represent the next char
                node.children[self.charToIndex(word[i])] = TrieNode()
            
           # go down a level
            node = node.children[self.charToIndex(word[i])] 
            i += 1 
                
        # label the end of word
        node.isEndOfWord = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        n = len(word)
        i = 0
        while i < n:
            charNode = node.children[self.charToIndex(word[i])]
            # this char doesn't exist in trie
            if charNode == None:
                return False
            # this char exists. continue 
            else:
                node = charNode
                i += 1
        
        # all chars in word exist in trie
        
        # check if the word ends here in trie
        if node.isEndOfWord: 
            return True
        else:
            return False        
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        n = len(prefix)
        i = 0
        
        # go over each char in prefix
        while i < n:
            charNode = node.children[self.charToIndex(prefix[i])]
            # this char doesn't exist in trie
            if charNode == None:
                return False
            # this char exists. continue 
            else:
                node = charNode
                i += 1
        
        # all chars in prefix exist in trie
        return True
        
    def charToIndex(self, char):
        """
        :type char: str
        :rtype: int
        return the index of char in the list of children
        """
        return ord(char) - ord("a")
    

class TrieNode():
    
    def __init__(self, children = [None] * 26, isEndOfWord = False):
        self.children = children
        self.isEndOfWord = isEndOfWord


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
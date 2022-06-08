class TrieNode {
    
    TrieNode[] children;
    Boolean isEndOfWord;        
    
    public TrieNode() {
        children = new TrieNode[26];
        isEndOfWord = false;            
    }
}

class Trie {
    
    TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        int n = word.length();
        
        // pointers
        TrieNode node = root;
        int i = 0;
        
        // go over each char in word
        while (i < n) {
            // this char and remaining chars don't exist in a branch already
            if (node.children[charToIndex(word.charAt(i))] == null) {
                // insert a new trie node to represent the next char
                node.children[charToIndex(word.charAt(i))] = new TrieNode();
            } // else: this char already exists in a branch. go down a level directly to check the next char      
            // go down a level
            node = node.children[charToIndex(word.charAt(i))];
            i += 1;
        }
        
        // label the end of word
        node.isEndOfWord = true;
        
    }
    
    public boolean search(String word) {
        int n = word.length();
        // pointers
        TrieNode node = root;
        int i = 0;
        while (i < n) {
            TrieNode charNode = node.children[charToIndex(word.charAt(i))];
            // this char doesn't exist in trie
            if (charNode == null) {
                return false;
            // this char exists. continue to check the next char
            } else {
                node = charNode;
                i += 1;                    
            }
        }
        // all chars in word exist in trie
        
        // check if the word ends here in trie
        if (node.isEndOfWord) {
            return true;
        } else {
            return false;
        }
        
    }
    
    public boolean startsWith(String prefix) {
        int n = prefix.length();
        // pointers
        TrieNode node = root;
        int i = 0;
        while (i < n) {
            TrieNode charNode = node.children[charToIndex(prefix.charAt(i))];
            // this char doesn't exist in trie
            if (charNode == null) {
                return false;
            // this char exists. continue to check the next char
            } else {
                node = charNode;
                i += 1;                    
            }
        }
        // all chars in prefix exist in trie  
        return true;
    }
    
    public int charToIndex(Character c) {
        return c - 'a';
    }
}



/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
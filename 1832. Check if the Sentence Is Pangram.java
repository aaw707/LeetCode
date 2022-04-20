import java.util.*;
class Solution {
    public boolean checkIfPangram(String sentence) {
        // create a hashtable to store unique chars in sentence
        Hashtable<Character, Integer> t = new Hashtable<>();
        // for each character in sentence
        for (char c : sentence.toCharArray()) {
            // if this character is not in the hash table, put it in
            if (!t.containsKey(c)) {
                t.put(c, 1);
            }
        }
        // if the hash table contains 26 unique characters, return true
        return t.size() == 26;
    }
}
import java.util.*;
class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        // create morse code alphabet reference
        String[] alphabet = new String[] {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        // create a hash table to store unique transformations
        Hashtable<String, Integer> t = new Hashtable<>();
        // loop over each word from input
        for (String word : words) {
            StringBuilder m = new StringBuilder("");
            // loop each char in word
            for (char c : word.toCharArray()) {
                // get the corresponding morse code by ASCII value, append to new string
                m.append(alphabet[(int) c - 97]);
            }
            // re-built word in morse code
            String ms = m.toString();
            // store this tranformation in a hash table, if not existed already
            if (!t.containsKey(ms)) {
                t.put(ms, 1);
            }
        }
        
        // return the size of hash table i.e. num of unique transformations
        return t.size();
    } 
}
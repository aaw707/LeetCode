import java.util.*;
class Solution {
    // solve with a sliding window
    public int lengthOfLongestSubstring(String s) {
        // base case
        int len = s.length();
        if (len == 0) {
            return 0;
        }
        
        // create a hashtable to store chars in current substring
        Hashtable<Character, Integer> t = new Hashtable<>();
        // left pointer
        int j = 0;
        int maxLen = 0;
        // loop over each char with the right pointer
        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);
            // if c not in hash table, put it in
            if (!t.containsKey(c)) {
                t.put(c, 1);
            // if c already in hash table, in order to keep the chars in substring unique
            } else {
                // move the left point to the right
                while (j <= i) {
                    // if j points at a char same as c
                    if (s.charAt(j) == c) {
                        // move j one step more to the left, to exclude the repeating char
                        j++;
                        break;
                    // j hasn't reached the repeating char
                    } else {
                        // remove the char at j from hash table, as it's no longer in the substring
                        t.remove(s.charAt(j));
                        // move one step to the right
                        j++;
                    }
                }
            }
            // substring (j, i) now contains only unique chars. update maxLen if needed
            maxLen = Math.max(maxLen, i - j + 1);
        }
        return maxLen;
    }
}
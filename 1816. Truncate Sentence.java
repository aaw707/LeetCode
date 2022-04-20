class Solution {
    public String truncateSentence(String s, int k) {
        // length of string s
        int len = s.length();
        // num of spaces encountered
        int space_count = 0;
        // loop over each char in s
        for (int i = 0; i < len; i++) {
            // if char is a space, add 1 to space count
            if (s.charAt(i) == ' ') {
                space_count++;
                // if space count == k, return the words before this space
                if (space_count == k) {
                    return s.substring(0, i);
                }
            }
        }
        // space count never reached k -> all words are included
        return s;
    }
}
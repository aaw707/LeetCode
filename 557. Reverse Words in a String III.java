class Solution {
    public String reverseWords(String s) {
        // split the input string into a list of words by spaces
        String[] words = s.split(" ");
        StringBuilder res = new StringBuilder("");
        
        // for each word in words (in order)
        for (String word : words) {
            // add each char in word to res backwards
            for (int i = word.length() - 1; i >= 0; i--) {
                res.append(word.charAt(i));
            }
            // add a space at the end of the word
            res.append(' ');
        }
        // return res without the extra space at the end
        return res.substring(0, s.length()).toString();
    }
}
class Solution {
    public int mostWordsFound(String[] sentences) {
        int max_spaces = 0;
        // loop over each sentence
        for (String sentence : sentences) {
            // loop over each character, count the num of spaces
            int num_chars = sentence.length();
            int num_spaces = 0;
            for (int j = 0; j < num_chars; j++) {
                if (sentence.charAt(j) == ' ') {
                    num_spaces++;
                }
            }
            // record max spaces
            if (num_spaces > max_spaces) {
                max_spaces = num_spaces;
            }
        }
        // num of words = num of spaces + 1
        return max_spaces + 1;
    }
}
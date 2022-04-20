class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        // keep count of consistent strings
        int count = 0;
        // mark outer loop for continue keyword
        outerloop:
        // loop over each word
        for (String word : words) {
            // loop over each char in word
            for (char c : word.toCharArray()) {
                // if char doesn't exist in allowed, continue to the next word
                if (allowed.indexOf(c) == -1) {
                    continue outerloop;
                }
            }
            // if all chars in this word are in allowed, add 1 to count
            count++;
        }
        return count;        
    }
}
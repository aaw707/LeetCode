class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int count = 0;
        // go over each pattern, check if it appears in word
        for (String pattern : patterns) {
            if (word.contains(pattern)) {
                count++;
            }
        }
        return count;
    }
}
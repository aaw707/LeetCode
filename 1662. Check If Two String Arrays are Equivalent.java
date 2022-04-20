class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        // concat word1 to s1, word2 to s2
        StringBuilder s1 = new StringBuilder("");
        StringBuilder s2 = new StringBuilder("");
        for (String word : word1) {
            s1.append(word);
        }
        for (String word : word2) {
            s2.append(word);
        }
        // compare s1 and s2
        String w1 = s1.toString();
        String w2 = s2.toString();
        return w1.equals(w2);
    }
}
class Solution {
    public String sortSentence(String s) {
        // split s into words
        String[] words = s.split(" ");
        // number of words
        int n = words.length;
        // create a new list for ordered words
        String[] ordered = new String[n];
        // put ordered words into the new list
        for (String word : words) {
            int order = Integer.parseInt(word.substring(word.length() - 1));
            ordered[order - 1] = word.substring(0, (word.length() - 1));
        }
        // build the original string
        StringBuilder org_s = new StringBuilder("");
        // for each ordered word, append to the original string with a space in between
        for (String word : ordered) {
            org_s.append(word);
            org_s.append(" ");
        }
        // return the original string, with the ending space removed
        return org_s.toString().substring(0, (org_s.length() - 1));
        
    }
}
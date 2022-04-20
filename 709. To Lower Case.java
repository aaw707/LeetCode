class Solution {
    public String toLowerCase(String s) {
        // build a new string as result
        StringBuilder res = new StringBuilder("");
        // for each character in string s
        for (char c : s.toCharArray()) {
            // if c is an upper case letter by ASCII, add it to res as the lower case
            if (64 < (int) c && (int) c < 91) {
                res.append((char) ((int) c + 32));
            // if not, add c itself
            } else {
                res.append(c);
            }
        }
        return res.toString();
    }
}
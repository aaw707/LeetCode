class Solution {
    public String replaceDigits(String s) {
        StringBuilder res = new StringBuilder("");
        int len = s.length();
        // go over each char in s
        for (int i = 0; i < len; i++) {
            // for even indices, add letter to res
            if (i % 2 == 0) {
                res.append(s.charAt(i));
            // for odd indices, shift the prev letter with digit
            } else {
                res.append(shift(s.charAt(i - 1), s.charAt(i)));
            }
        }
        return res.toString();
    }
    
    Character shift(Character c, Character n) {
        return (char) (((int) c) + Character.getNumericValue(n));
    }
}
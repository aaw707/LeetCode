class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        int len = s.length();
        for (int n = 0; n < len; n++) {
            // odd length palindrome
            String odd = findPalindrome(s, n, n);
            // even length palindrome
            String even = findPalindrome(s, n, n + 1);
            // store longest palindrome into res
            if (odd.length() > res.length() && odd.length() > even.length()) {
                res = odd;
            } else if (even.length() > res.length() && even.length() > odd.length()) {
                res = even;
            }
        }
        return res;
    }
    String findPalindrome(String s, int i, int j) {
        int len = s.length();
        // move outwards to check for palindromes
        while (i >= 0 && j < len && s.charAt(i) == s.charAt(j)) {
            i--;
            j++;
        }
        return s.substring(i + 1, j); // (i, j) is the last palindrome moved one step more outwards
    }
}
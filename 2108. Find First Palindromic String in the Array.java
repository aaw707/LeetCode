class Solution {
    public String firstPalindrome(String[] words) {
        // loop over each word
        for (String word : words) {
            // check if it's palindrome
            if (isPalindrome(word)) {
                // reurn the first palindrome and end function
                return word;
            }
        }
        // no palindrome is found. return empty string
        return "";
    }
    
    boolean isPalindrome(String word) {
        // length of word
        int len = word.length();
            
        // if empty string or only one char in string, it is palindrome
        if (len == 0 || len == 1) {
            return true;
            
        // if first char == last char, check the middle part
        } else if (word.charAt(0) == word.charAt(len - 1)){            
            return isPalindrome(word.substring(1, len - 1));
            
        // fist char != last char, not palindrome
        } else {
            return false;
        }
    }
}
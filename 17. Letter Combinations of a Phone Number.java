import java.util.*;
class Solution {
    // store the refs
    Hashtable<Character, Character[]> t = new Hashtable<>() {
        {
            put('2', new Character[] {'a', 'b', 'c'});
            put('3', new Character[] {'d', 'e', 'f'});
            put('4', new Character[] {'g', 'h', 'i'});
            put('5', new Character[] {'j', 'k', 'l'});
            put('6', new Character[] {'m', 'n', 'o'});
            put('7', new Character[] {'p', 'q', 'r', 's'});
            put('8', new Character[] {'t', 'u', 'v'});
            put('9', new Character[] {'w', 'x', 'y', 'z'});            
        }
    };

    public List<String> letterCombinations(String digits) {
        // res to store combinations
        List<String> res = new ArrayList<>();
        // base case: empty input
        if (digits.length() == 0) {
            return res;
        }
        
        // get the combinations from the substring of digits, excluding the first digit
        List<String> later_combinations = letterCombinations(digits.substring(1, digits.length()));
        // if results coming back for later combinations is empty (i.e. no more digits after the current one)
        // add an empty string to avoid skipping the nested for loop below
        if (later_combinations.size() == 0) {
            later_combinations.add("");
        }
        // get the first digit of input
        char first_digit = digits.charAt(0);
        // for each character this digit represents
        for (char c : t.get(first_digit)) {
            // for each combination returned from the remaining substring of digits
            for (String s : later_combinations) {
                // create a new combination
                res.add(new StringBuilder()
                        .append(c)
                        .append(s)
                        .toString());
            }
        }
        return res;
    }
}

// time complexity: O(4^n * 3^m)
// space: O(4^n * 3^m)
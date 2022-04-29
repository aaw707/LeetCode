import java.util.*;

class Solution {
    public boolean isValid(String s) {
        // hash table for ref
        Hashtable<Character, Character> t = new Hashtable<>();
        t.put(')', '(');
        t.put(']', '[');
        t.put('}', '{');
        // stack to store parentheses
        Stack<Character> st = new Stack<>();
        for (char c : s.toCharArray()) {
            // check if c balances out with the top item on stack
            if (!st.empty() && t.get(c) == st.peek()) {
                // if yes, pop the top item
                st.pop();
            } else {
                // if not, put c onto stack
                st.push(c);
            }
        }
        // if stack is empty, all parentheses have been balanced out i.e. valid
        return st.empty();
    }
}
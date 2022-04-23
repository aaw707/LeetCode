class Solution {
    public boolean backspaceCompare(String s, String t) {
        // use stack to transform the 2 strings into when the backspace takes effect
        Stack<Character> s1 = inStack(s);
        Stack<Character> s2 = inStack(t);
        // compare the 2 strings
        return s1.equals(s2);
    }
    
    Stack<Character> inStack(String s) {
        Stack<Character> st = new Stack<>();
        // for each char in string
        for (char c : s.toCharArray()) {
            // if it's a back space char
            if (c == '#') {
                // if the stack is not empty, remove the last char
                if (!st.empty()) {
                    st.pop();
                }
                // if the stack is empty, do nothing
            // if the char is not a back space
            } else {
                // put the char onto stack
                st.push(c);
            }            
        }
        return st;
    }    
}


class Solution {
    public String makeGood(String s) {
        Stack<Character> st = new Stack<>();
        // for each char in s
        for (char c : s.toCharArray()) {
            // if stack is empty, put char onto stack
            if (st.empty()) {
                st.push(c);
            // if stack is not empty, compare char with the top of stack
            } else {
                char t = st.peek();
                // if they are the same letter, upper & lower case
                if (Math.abs(((int) t) - ((int) c)) == 32) {
                    // remove the top of stack
                    st.pop();
                // if they are not, put char onto stack
                } else {
                    st.push(c);
                }
            }
        }
        // convert chars in stack into a string
        StringBuilder res = new StringBuilder("");
        for (char c : st) {
            res.append(c);
        }
        return res.toString();
    }
}
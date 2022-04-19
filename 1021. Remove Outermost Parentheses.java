class Solution {
    public String removeOuterParentheses(String s) {
        Stack<Character> stack = new Stack<>();
        int ptr = 0;
        int len = s.length();
        StringBuilder res = new StringBuilder("");
        
        // go over each char in s
        for (int i = 0; i < len; i++) {
            if (s.charAt(i) == ')') {
                stack.pop();
            } else {
                stack.push(s.charAt(i));
            }
            // if stack empty, just popped the outermost parentheses
            if (stack.empty()) {
                // append the content inside the outermost parentheses to res
                res.append(s.substring(ptr + 1, i));
                ptr = i + 1;
            }
        }
        return res.toString();
    }
}
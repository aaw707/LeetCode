class Solution {
    public int balancedStringSplit(String s) {
        // create a stack to store chars
        Stack<Character> stack = new Stack<>();
        int len = s.length();
        // keep count of balanced strings
        int count = 0;
        // loop over each char in string
        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);
            // if stack is empty, push c onto stack
            if (stack.empty()) {
                stack.push(c);
            // if stack not empty
            } else {
                char top = stack.peek();
                // if c balances with the top of stack, pop off top of stack
                if ((top == 'L' && c == 'R') || (top == 'R' && c == 'L')) {
                    stack.pop();
                    // if stack is empty after popping, there was one balanced string
                    if (stack.empty()) {
                        count++;
                    }
                // if c doesn't balance with the top of stack, push c to the stack
                } else {
                    stack.push(c);
                }
            }
        }
        return count;
    }
}
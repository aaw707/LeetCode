class Solution {
    public int maxDepth(String s) {
        
        int depth = 0;
        int max_depth = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                depth += 1;
                max_depth = Math.max(depth, max_depth);
            } else if (s.charAt(i) == ')') {
                depth -= 1;
            }
        }
        return max_depth;
    }
}
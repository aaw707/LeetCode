class Solution {
    public String interpret(String command) {
        String res = "";
        int idx = 0;
        int len = command.length();
        // loop over each char to parse the words
        while (idx < len) {
            if (command.charAt(idx) == 'G') {
                res += "G";
                idx++;
            } else if (command.charAt(idx + 1) == ')') {
                res += "o";
                idx += 2;
            } else {
                res += "al";
                idx += 4;
            }
        }
        return res;        
    }
}
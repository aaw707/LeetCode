class Solution {
    public String restoreString(String s, int[] indices) {
        int len = indices.length;
        // new arr of chars as the shuffled string
        char[] arr = new char[len];
        // shuffle each char
        for (int i = 0; i < len; i++) {
            arr[indices[i]] = s.charAt(i);
        }
        // transform into a string
        String res = new String(arr);
        return res;
    }
}
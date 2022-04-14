class Solution {
    public String defangIPaddr(String address) {
        String defanged = "";
        int l = address.length();
        for (int i = 0; i < l; i++) {
            Character c = address.charAt(i);
            if (c == '.') {
                defanged += "[.]";
            } else {
                defanged += c;
            }
        }
        return defanged;
    }
}
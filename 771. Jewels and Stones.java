class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count = 0;
        // for each stone, check if it equals to one of the jewels
        for (char s : stones.toCharArray()) {
            for (char j : jewels.toCharArray()) {
                if (s == j) {
                    // if yes, keep the count and then check the next stone
                    count++;
                    break;
                }
            }
        }
        return count;    
    }
}
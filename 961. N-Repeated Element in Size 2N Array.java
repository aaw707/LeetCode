import java.util.*;
class Solution {
    public int repeatedNTimes(int[] nums) {
        Hashtable<Integer, Integer> t = new Hashtable<>();
        // go over each num 
        for (int num : nums) {
            // if num in t, increase count by 1
            if (t.containsKey(num)) {
                return num;
            // if num not in t, add it with count = 1
            } else {
                t.put(num, 1);
            }
        }
        // this line should not be executed
        return -1;
    }
}
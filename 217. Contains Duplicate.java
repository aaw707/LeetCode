import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Hashtable<Integer, Integer> t = new Hashtable<>();
        // use hashtable to check for duplicates
        for (int num : nums) {
            if (t.containsKey(num)) {
                return true;
            } else {
                t.put(num, num);
            }
        }
        return false;
    }
}
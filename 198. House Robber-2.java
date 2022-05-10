import java.util.*;
class Solution {
    public int rob(int[] nums) {
        
        int n = nums.length;
        
        // hash table to store refs
        // key: length of sub array, val: maximum amount of money to rob
        Hashtable<Integer, Integer> t = new Hashtable<>();
        // when 0 house left, $0 to rob
        t.put(n, 0);
        // when 1 house left, rob it
        t.put(n - 1, nums[n - 1]);
        
        // go over each house backwards
        for (int i = n - 2; i >= 0; i--) {
            // rob
            int r1 = nums[i] + t.get(i + 2);
            // not rob
            int r2 = t.get(i + 1);
            // best decision for this house
            t.put(i, Math.max(r1, r2));            
        }

        // return 
        return t.get(0);
    }
}

// dp backwards
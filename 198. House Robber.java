import java.util.*;
class Solution {
    
    // hash table to store refs
    // key: length of sub array, val: maximum amount of money to rob
    Hashtable<Integer, Integer> t = new Hashtable<>();
    
    public int rob(int[] nums) {
        
        int n = nums.length;
        
        // base cases
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return nums[0];
        }
        
        // check hash table for cache
        if (t.containsKey(n)) {
            return t.get(n);
        }
        
        // choose to rob the first house
        int r1 = nums[0] + rob(Arrays.copyOfRange(nums, 2, n));

        // choose not to rob
        int r2 = rob(Arrays.copyOfRange(nums, 1, n));
        
        // save res in hash table
        t.put(n, Math.max(r1, r2));
        
        // return 
        return t.get(n);
        
        
    }
}
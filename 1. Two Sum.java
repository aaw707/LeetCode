import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // create a hashtable to record the num and the complementary val
        Hashtable<Integer, Integer> t = new Hashtable<>();
        // res to return
        int[] res = new int[2];
        // length of input array
        int len = nums.length;
        
        // loop over each num in nums
        for (int i = 0; i < len; i++) {
            // if num in hash table as a recorded num's complementary val
            if (t.containsKey(nums[i])) {
                // return those indices
                res[0] = i;
                res[1] = t.get(nums[i]);
                return res;
            // else, put the num (index) into the table as val, and the complementary val as key
            } else {
                t.put(target - nums[i], i);
            }
        }
        // this line will not be executed since a valid solution is guaranteed
        return res;
    }
}

/*


, 

*/
import java.util.*;
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int len = nums.length;
        // base case
        if (len < 3) {
            return new ArrayList<>();
        }
        // arraylist to store res
        List<List<Integer>> res = new ArrayList<>();
        // sort nums to avoid duplicate
        Arrays.sort(nums);
        
        // fix x first, look for the other idxs
        for (int i = 0; i < len - 2; i++) {
            // skip duplicates by only process i with the same value once
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int first = nums[i];
            // 2 pointers from left & right
            int L = i + 1;
            int R = len - 1;
            while (L < R) {
                int threeSum = first + nums[L] + nums[R];
                if (threeSum > 0) {
                    R--;
                } else if (threeSum < 0) {
                    L++;
                } else {
                    res.add(Arrays.asList(first, nums[L], nums[R]));
                    // move left pointer to the right to check for other triplets
                    L++;
                    // avoid duplicates by skipping same value of L
                    while (nums[L] == nums[L - 1] && L < R) {
                        L++;
                    }
                }
            }
        }
        return res;
    }
}
class Solution {
    public int maxSubArray(int[] nums) {
        
        int n = nums.length;
        int current_sum = 0;
        int max_sum = Integer.MIN_VALUE;
        
        // base case
        // only one num in nums
        if (n == 1) {
        // return num
            return nums[0];
        }
        
        // go over each num in nums, left to right
        for (int num : nums) {
            // current sum += num
            current_sum += num;
            // check if current sum > max sum we recorded
            if (current_sum > max_sum) {
                max_sum = current_sum;
            }
            // if current sum < 0
            if (current_sum <= 0) {
                // discard the prev nums, since they are not contributing to the sum in the future
                current_sum = 0;
            }
        }
        
        // return max sum
        return max_sum;
    }
}
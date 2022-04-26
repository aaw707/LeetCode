class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        // length of input array
        int len = nums.length;
        // sum of current sub array
        int sum = 0;
        // current minimum length
        int minLen = len + 1;
        // left pointer
        int j = 0;
        // right pointer
        for (int i = 0; i < len; i++) {
            sum += nums[i];
            // try shrinking the subarray from left while keeping the sum >= target to get a smaller length           
            while (sum >= target) {
                minLen = Math.min(minLen, i - j + 1);
                sum -= nums[j++];
            }
        }
        // if minLen is not updated, no valid subarray found. return 0
        if (minLen > len) {
            return 0;
        } else {
            return minLen;            
        }
    }
}

/*
2 pointers

*/
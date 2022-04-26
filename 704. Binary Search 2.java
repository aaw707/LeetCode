class Solution {
    
    public int search(int[] nums, int target) {
        // 2 pointers, start and end idx of sub array
        int start = 0;
        int end = nums.length - 1;
        int mid;
        // binary search for target
        while (start <= end) {
            mid = (end + start) / 2;
            // update pointers
            if (nums[mid] < target) {
                start = mid + 1;
            } else if (nums[mid] > target) {
                end = mid - 1;
            } else {
                return mid;
            }
        }
        // target not found
        return -1;
    }
}
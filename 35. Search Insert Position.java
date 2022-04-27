class Solution {
    public int searchInsert(int[] nums, int target) {
        // base cases
        if (target < nums[0]) {
            return 0;
        } else if (target > nums[nums.length - 1]) {
            return nums.length;
        }
        // 2 pointers
        int start = 0;
        int end = nums.length - 1;
        int mid = 0;
        // binary search for target
        while (end >= start) {
            mid = (end + start) / 2;
            if (nums[mid] < target) {
                start = mid + 1;
            } else if (nums[mid] > target) {
                end = mid - 1;
            } else {
                return mid;
            }
        }
        // position to insert
        if (target > nums[mid]) {
            return mid + 1;
        } else {
            return mid;
        }
    }
}


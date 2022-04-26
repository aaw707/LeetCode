class Solution {
    int start = 0;
    
    public int search(int[] nums, int target) {
        int len = nums.length;
        // target not found
        if (len == 0) {
            return -1;
        }
        int mid = len / 2;
        // recursively find the target
        if (nums[mid] < target) {
            start = start + mid + 1;
            return search(Arrays.copyOfRange(nums, mid + 1, len), target);
        } else if (nums[mid] > target) {
            return search(Arrays.copyOfRange(nums, 0, mid), target);
        } else {
            return mid + start;
        }
    }
}
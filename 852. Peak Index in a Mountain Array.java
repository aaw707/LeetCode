class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        // O(n)
        int len = arr.length;
        for (int i = 1; i < len; i++) {
            if (arr[i] < arr[i - 1]) {
                return i - 1;
            }
        }
        // will not be executed
        return 0;
    }
}
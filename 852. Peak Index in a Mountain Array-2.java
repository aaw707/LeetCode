class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        // O(log(n))
        // 2 pointers
        int start = 0;
        int end = arr.length - 1;
        int mid = 0;
        while (start <= end) {
            mid = (start + end) / 2;
            // increasing
            if (arr[mid - 1] < arr[mid] && arr[mid] < arr[mid + 1]) {
                start = mid;
            // decreasing
            } else if (arr[mid - 1] > arr[mid] && arr[mid] > arr[mid + 1]) {
                end = mid;
            // peaking
            } else {
                return mid;
            }
        }
        return mid;
    }
}
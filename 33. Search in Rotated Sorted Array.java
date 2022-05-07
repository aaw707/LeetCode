        /*
        [0,1,2,3,4]
        [4,0,1,2,3]
        [2,3,4,0,1]
        ...
        [1,2,3,4,0]
        */ 



        class Solution {
            public int search(int[] nums, int target) {
                
                // base case: only one num in nums
                if (target == nums[0]) {
                    return 0;
                } else if (nums.length == 1) {
                    return -1;
                }
                
                
                // find the pivot
                int L = 0;
                int R = nums.length - 1;
                
                if (nums[R] > nums[L]) { // not pivoted
                    L = R;
                } else { // array is pivoted
                    
                    while (L < R) {
                        int mid = (L + R) / 2;
                        if (nums[mid] < nums[R]) {
                            R = mid;
                        } else if (nums[mid] > nums[L]) {
                            L = mid;
                        } else {
                            break; // nums[mid] == nums[R] or nums[L]
                        }
                    } // after this while loop, L: idx the largest num in the array
                    
                    if (target > nums[L] || target < nums[L + 1]) {
                        return -1;
                    }
                }
                // after the above steps, L points to the idx of largest element
               
                // set the range for search
                if (target < nums[0]) {
                    L = L + 1;
                    R = nums.length - 1;
                } else if (target > nums[0]) {
                    R = L;
                    L = 1;
                } // target == nums[0] is checked in the base case
                
                // binary search to find the idx of target in pivoted array
                while (L <= R) {
                    int mid = (L + R) / 2;
                    if (nums[mid] < target) {
                        L = mid + 1;
                    } else if (nums[mid] > target) {
                        R = mid -1;
                    } else {
                        return mid;  // return if found
                    }
                }
                
                // target is not found
                return -1;
                
            }
        }
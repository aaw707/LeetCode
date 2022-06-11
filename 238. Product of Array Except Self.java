class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        // length of nums
        int n = nums.length;
        
        // create helper arr L
        int[] L = new int[n];
        // create helper arr R
        int[] R = new int[n];
        // create an array containing the products to be returned
        int[] res = new int[n];
        
        
        // fill arr L
        L[0] = 1;
        for (int i = 1; i < n; i++) {
            L[i] = L[i - 1] * nums[i - 1];
        }        
        
        // fill arr R
        R[n - 1] = 1;
        for (int j = n - 2; j >= 0; j--) {
            R[j] = R[j + 1] * nums[j + 1];
        }
        
        // fill the return array by multiplying left and right side of each element
        for (int k = 0; k < n; k++) {
            res[k] = L[k] * R[k];
        }
        
        
        
        // return arr
        return res;
    }
}
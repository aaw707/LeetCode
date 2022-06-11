class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        // length of nums
        int n = nums.length;
        
        // create an array containing the products to be returned
        int[] res = new int[n];
        
        // fill with the left sub-product
        res[0] = 1;
        for (int i = 1; i < n; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }        
        
        // update with the right sub-product
        int R = 1;
        for (int j = n - 1; j >= 0; j--) {
            res[j] = res[j] * R;
            R = nums[j] * R;
        }        
        
        // return arr
        return res;
    }
}
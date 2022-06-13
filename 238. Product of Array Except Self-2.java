class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        // length of nums
        int n = nums.length;
        
        // create an array to be returned
        int[] res = new int[n];
        
        // go over and fill the array from left to right
        // res[i]: the product of all elements on the left of nums[i]
        res[0] = 1; // there's no element on the left of nums[0]
        for (int i = 1; i < n; i++) {
            // use prefix sum (product) to save time: every element is calculated based on the previous element
            res[i] = res[i - 1] * nums[i - 1];
        }        
        
        // go over the array from right to left
        // update the array: multiply the existing value (the product of all elements on the left of nums[i]) with the product of all elements on the right of nums[i]
        int R = 1; // there's no element on the right of nums[n - 1] (last element)
        for (int j = n - 1; j >= 0; j--) {
            res[j] = res[j] * R; // res[j] (on the right) = left products, R = right products, res[j] (on the left) = product of all elements in num except nums[j]
            R = nums[j] * R; // update R so it's the right products of the next element to process 
        }        
        
        // return arr
        return res;
    }
}
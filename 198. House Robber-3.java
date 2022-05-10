class Solution {
    public int rob(int[] nums) {
        
        int n = nums.length;
        
        // base case
        if (n == 0) {
            return 0;
        }
        
        int house3 = 0;
        int house2 = nums[n - 1];
        
        // go over each house backwards
        for (int i = n - 2; i >= 0; i--) {
            // best decision for this house
            int house1 = Math.max(nums[i] + house3, house2); // rob or not rob
            
            house3 = house2;
            house2 = house1;
        }

        // return 
        return house2;
    }
}

// dp backwards
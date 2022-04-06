class Solution {
    public int threeSumMulti(int[] arr, int target) {
        
        // create an array to store the counts of appearance of each number in arr        
        long[] counts = new long[101];
        // loop over arr, increase the count for each item when it appears
        for (int a : arr) counts[a]++;
        // total number of tuples
        long total = 0;
            
        // i, j, k are the nums, not idx of arr
        // 0-100 is the range of nums given
        for (int i = 0; i <= 100; i++) {
            for (int j = i; j <= 100; j++) {
                int k = target - i - j;
                
                if (k < 0 || k > 100) {
                    continue; // k is invalid 
                }
                    
                if (i == j && j == k) {
                    total += counts[i] * (counts[i] - 1) * (counts[i] - 2) / (3 * 2 * 1); // choose 3 from n
                } else if (i == j && j != k) {
                    total += counts[i] * (counts[i] - 1) / (2 * 1) * counts[k];
                } else if (j < k) { // i < j < k
                    total += counts[i] * counts[j] * counts[k];
                }
            }
        }
        
        
        return (int) (total % (1e9 + 7));
    }
}
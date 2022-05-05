class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        current_sum = 0
        max_sum = float('-inf')
        
        # base case
        if n == 1:
            return nums[0]
        
        for i in range(n):
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
            # prev mums don't contribute to the sum
            if current_sum <= 0:
                # discard the prev nums
                current_sum = 0

        

        return max_sum
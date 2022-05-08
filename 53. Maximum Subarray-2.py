class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        current_sum = 0
        max_sum = nums[0]
        
        # dp
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            # if current_sum < 0, all prev items will not contribute to a larger subarray sum
            if current_sum < 0:
                # start counting again from the next num
                current_sum = 0
        
        return max_sum
                
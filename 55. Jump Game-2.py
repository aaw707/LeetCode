class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)
        last_idx = n - 1
        
        # dp
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= last_idx:
                last_idx = i
                
        return last_idx == 0
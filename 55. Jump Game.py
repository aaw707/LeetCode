class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)
        # last position that can reach the end 
        last_pos = n - 1
        
        # from right to left, find the pos able to reach the end
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
    
        # time: O(n)
        # space: O(1)
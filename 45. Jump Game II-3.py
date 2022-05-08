class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        jumps = 0
        furthest = 0
        current_jump_end = 0
        
        n = len(nums)
        
        # dp
        for i in range(n - 1): # exclude the last num
            furthest = max(furthest, nums[i] + i)
            if current_jump_end == i:
                jumps += 1
                current_jump_end = furthest
                
        return jumps
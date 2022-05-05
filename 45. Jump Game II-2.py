class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_jump_end = 0
        furthest = 0
        n = len(nums)
        
        for i in range(n - 1): # exclude the last num 
            # update the furthest
            furthest = max(furthest, nums[i] + i)
            
            # if have come to the end of the furthest jump
            if i == current_jump_end:
                # update the number of jumps
                jumps += 1
                # set the current jump end to the furthest pos
                current_jump_end = furthest
        
        return jumps
            
                  
            
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        current_max = nums[0]
        current_min = nums[0]
        res = current_max
        
        for i in range(1, n):
            num = nums[i]
            
            tmp_max = max(num, # num is larger than preceding products e.g. zero or negative numbers
                          current_max * num, # current_max and num are both positive
                         current_min * num) # current_min is negative, num is negative. their negativities cancel out 
            
            current_min = min(num, 
                             current_max * num,
                             current_min * num)
            
            current_max = tmp_max
            
            res = max(current_max, res)
            
        return res
            
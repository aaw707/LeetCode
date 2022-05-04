class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        n = len(nums) 
        
        # base case
        if n == 1:
            return nums
        
        idx = 0
        for i in range(n):
            if nums[i] % 2 == 0:
                # swap nums[i], nums[j]
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1
                
        return nums
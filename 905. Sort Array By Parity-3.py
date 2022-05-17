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
        
        # 2 pointer
        i = 0
        j = n - 1
        
        while i < j:
            while i < n and nums[i] % 2 == 0:
                i += 1
            # i is odd
            while j >= 0 and nums[j] %2 == 1:
                j -= 1
            # j is even
            
            if i < j:
                # swap
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        return nums
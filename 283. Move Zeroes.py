class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        pos = 0
        num_zeros = 0
        n = len(nums)
        
        # move the non-zero digits to the left
        for i in range(n):
            if (nums[i] != 0):
                nums[pos] = nums[i]
                pos += 1
            else:
                num_zeros += 1
                
        # fill the remaining right part with zeros
        for j in range(n - num_zeros, n):
            nums[j] = 0
            
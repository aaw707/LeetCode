class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bit manipulation
        a = 0
        for num in nums:
            a ^= num
            
        return a
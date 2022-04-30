class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return the difference between sum of nums and sum of nums without the missing number
        return sum(range(len(nums) + 1)) - sum(nums)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        # one pass, constant space
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
                
        # reassign the values
        for i in range(zeros):
            nums[i] = 0
        for j in range(zeros, zeros + ones):
            nums[j] = 1
        for k in range(zeros + ones, len(nums)):
            nums[k] = 2
        return nums
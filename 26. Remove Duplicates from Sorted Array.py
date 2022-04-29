class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        removed = 0
        i = 0
        s = set()
        # pop the duplicates
        while i < length - removed:
            if nums[i] in s:
                nums.pop(i)
                removed += 1
            else:
                s.add(nums[i])
                i += 1
        return length - removed
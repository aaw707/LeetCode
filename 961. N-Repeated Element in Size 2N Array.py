class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = {}
        for num in nums:
            if num in t:
                t[num] += 1
            else:
                t[num] = 1
                
        n = len(nums) / 2
        for key in t:
            if t[key] == n:
                return key
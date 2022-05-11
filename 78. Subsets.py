class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = [[]]
        
        # backtracking
        for i in range(n):
            com = [nums[i]]
            ss = self.subsets(nums[i + 1:])
            for s in ss:
                res.append(com + s)
        return res
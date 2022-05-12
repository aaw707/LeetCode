class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)        
        res = []
        
        # base case
        if n == 1:
            res.append(nums)
            return res
        
        # for num in nums, use backtracking to get the permutations of remaining nums
        for i in range(n):
            num = nums[i]
            backtracking = self.permuteUnique(nums[i + 1:] + nums[:i]) # the remaining of nums excluding nums[i]
            for bt in backtracking:
                bt.append(num)
                # exclude duplicates
                if bt not in res:
                    res.append(bt)
        
        return res
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        n = len(nums)
        
        # base case
        if n == 1:
            res.append([nums[0]])
            return res
        
        # backtracking for combinations from subarray
        for i in range(n):
            subarray = nums[:i] + nums[i + 1:] # nums excluding nums[i]
            backtracking = self.permute(subarray)
            
            # then append current num
            for combination in backtracking:
                combination.append(nums[i])
                res.append(combination)
        
        return res
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # key: house idx in nums
        # val: max amount to rob
        t = {}
        
        n = len(nums)
        
        
        def helper(idx):
            
            # base case: idx out of range
            if idx >= n:
                return 0
            
            # ref the hash table
            if idx in t:
                return t[idx]
            
            # for each house there are 2 options

            # rob (and therefore can't rob the next one)
            m1 = nums[idx] + helper(idx + 2)

            # not rob
            m2 = helper(idx + 1)
            
            # record in hash table
            t[idx] = max(m1, m2)
            
            return t[idx]
        
        # call helper to calculate
        return helper(0)
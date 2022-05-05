class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # base case
        if n == 1:
            return 0
        
        # key: idx
        # val: minimum jumps to the end
        memo = {
            n - 1: 0
        }
        
        # go over the nums backwards (excluding the last one)
        for i in range(n - 2, -1, -1):
            # limit the furthest jump to the last idx of nums
            furthest_jump = min(nums[i] + i, n - 1)
            # record the min steps from j
            min_j = float('inf')
            for j in range(furthest_jump, i, -1):
                if j in memo:
                    min_j = min(min_j, memo[j])
            # steps from i = (steps from j) + 1
            memo[i] = min_j + 1
        
        return memo[0]
                    
            
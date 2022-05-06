class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # key: n = number of stairs given
        # val: number of ways to climb
        memo = {
            1: 1, # 1 step for 1 stair
            2: 2, # 1 step + 1 step, or 2 steps for 2 stairs
        }
        
        # base case
        if n <= 2:
            return memo[n]
        
        # for n > 2, there are 2 possible starting points: n - 1 and n - 2
        
        # when starting at n - 1, we have ways = memo[n - 1] to reach n - 1 stairs 
        # and for each way we climb 1 more stair to reach the top
        
        
        # when starting at n - 2, we have ways = memo[n - 2] to reach n - 2 stairs
        # and for each way we climb 2 more stairs at once to reach the top
        
        
        # we don't count the way that we reach stair n - 2, then we climb 1 stair, and then another 1 stair to reach the top
        # this will create duplicate ways like starting from n - 1
        
        def getWays(n):
            if n not in memo:
                memo[n] = getWays(n - 1) + getWays(n - 2)
            return memo[n]   
        
        return getWays(n)

        # time: O(n) save in each spot of memo
        # space: O(n)
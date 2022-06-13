class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # a triangle with the same structure of the given triangle
        # at each pos it contains the min path sum from the top to that pos
        dp = []
        
        # num of levels
        m = len(triangle)
        
        # construct the first level of dp      
        n = 1 # num of nums in this level
        dp.append([triangle[0][0]])  
        
        # loop over each level of triangle
        for i in range(1, m):
            
            # num of nums in this level
            n += 1
            
            # add this level to dp
            dp.append([0 for j in range(n)])
            
            # fill the first & last pos of this level
            dp[i][0] = dp[i - 1][0] + triangle[i][0] # first
            dp[i][-1] = dp[i - 1][-1] + triangle[i][-1] # last
            
            # loop over the remaining nums in this level
            for j in range(1, n - 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            
            
        return min(dp[-1])
            
            
            
            
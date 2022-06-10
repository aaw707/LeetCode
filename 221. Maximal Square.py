class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        # duplicate a dp matrix with the same size, filled with 0
        dp = [[0 for j in range(n)] for i in range(m)]
        
        # keep record of the maximum square we can find
        max_side_length = 0
        
        # for each 1 we find
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    
                    # store the side length of the largerst SQUARE we can get by having this cell as the bottom right corner
                    dp[i][j] = min(
                                    dp[i - 1][j],
                                    dp[i][j - 1],
                                    dp[i - 1][j - 1]
                                    ) + 1
                    max_side_length = max(dp[i][j], max_side_length)

        # return the area of max square            
        return max_side_length * max_side_length
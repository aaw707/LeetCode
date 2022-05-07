class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # for each pos on the top row: 1 way to reach (move to right only)
        if m == 1: # only 1 row
            return 1
        
        # for each pos on the left most column: 1 way to reach (move down only)
        if n == 1: # only 1 col
            return 1     
                
        # for every other pos: can be reached from the top pos down, or from left pos to the right
        # ways = ways to reach the pos above + ways to reach the pos on the left
        
        # construct a matrix
        matrix = [[0 for i in range(n)] for j in range(m)]
        # fill the matrix with num of ways
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        
        # return the bottom right corner value
        return matrix[m - 1][n - 1]
        
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # base case: starting point is obstacle
        if obstacleGrid[0][0] == 1:
            return 0
        
        # base case: starting point is the ending point (can reach)
        if m == n == 1:
                return 1
        
        # matrix to record how many ways there is to get to pos i, j
        ways = [[0 for j in range(n)] for i in range(m)]
        
        # since robot can only go right or go down, there's only 1 way for it to get to any pos on the top tow or the leftmost column
        
        # [0, 0] is the starting point
        
        # top row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                ways[0][j] = 1
            else:
                # when encounter an obstacle, can't go right anymore
                break
                
        # leftmost col
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                ways[i][0] = 1
            else:
                # when encounter an obstacle, can't go down anymore
                break
                
        # fill the rest of the cells
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    # can reach this grid from top or left 
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
                else:
                    ways[i][j] = 0
                    
        # for way in ways:
        #     print(way)
        
        # ways to reach the end
        return ways[m - 1][n - 1]
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # create a matrix for min path sum
        grid_sum = [["0" for j in range(n)] for i in range(m)]
        
        # go over each cell in grid
        for i in range(m):
            for j in range(n):
                # top left corner
                if i == 0 and j == 0:
                    grid_sum[0][0] = grid[0][0] 
                # top row. min path can only be accessed from the left cell
                elif i == 0:
                    grid_sum[i][j] = grid_sum[i][j - 1] + grid[i][j]
                # left most row. min path can only be accessed from the top cell
                elif j == 0:
                    grid_sum[i][j] = grid_sum[i - 1][j] + grid[i][j]
                # min path can be accessed from the top cell or the left cell
                else:
                    grid_sum[i][j] = min(grid_sum[i - 1][j], grid_sum[i][j - 1]) + grid[i][j]
                    
        return grid_sum[m - 1][n - 1]
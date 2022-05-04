class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        starting_idx = 0
        
        # checking each row, from bottom to top
        for m in range(rows - 1, -1, -1):
            # checking each element in the row, from left to right:
            for n in range(starting_idx, cols):
                if grid[m][n] < 0:
                    res += cols - n
                    starting_idx = n
                    break
        
        return res